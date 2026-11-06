
BEGIN;

DO $$
DECLARE
-- Definicion de factura, producto y cantidad a retornar
    v_bill_id INTEGER := 4;
    v_product_ids INTEGER[] := ARRAY[1, 5];
    v_quantities INTEGER[] := ARRAY[1, 1];

-- Variables de almacenamiento
    v_purchased_qty INTEGER;
    v_status VARCHAR(25);
    i INTEGER;

BEGIN

-- Factura existe?
    
    SELECT status
    INTO v_status
    FROM "Transactions".bills
    WHERE id = v_bill_id
    FOR UPDATE;
    
    
    IF NOT FOUND THEN
        RAISE EXCEPTION 'La factura con ID % no existe', v_bill_id;
    END IF;

    IF v_status = 'RETURNED' THEN
        RAISE EXCEPTION 'La factura con ID % ya fue retornada', v_bill_id;
    END IF;



    FOR i IN 1..array_length(v_product_ids, 1)
    LOOP

-- Producto existe en la factura?--

        SELECT qty
        INTO v_purchased_qty
        FROM "Transactions".bill_products
        WHERE bill_id = v_bill_id
        AND product_id = v_product_ids[i]
        FOR UPDATE;

        IF NOT FOUND THEN
            RAISE EXCEPTION
                'El producto con ID % no pertenece a la factura %',
                v_product_ids[i],
                v_bill_id;
        END IF;

    -- Cantidad a retornar es valida?
        IF v_quantities[i] IS NULL OR v_quantities[i] <= 0 THEN
            RAISE EXCEPTION 'La cantidad a retornar debe ser mayor a 0';
        END IF;

    -- Cantidad a retornar no puede superar la cantidad comprada
        IF v_quantities[i] > v_purchased_qty THEN
            RAISE EXCEPTION
                'No se pueden retornar % unidades. Solo quedan % pendientes',
                v_quantities[i],
                v_purchased_qty;
        END IF;

    END LOOP;
    --------


    FOR i IN 1..array_length(v_product_ids, 1)
    LOOP
-- Aumentar el stock con la cantidad retornada
        UPDATE "Transactions".products
        SET qty = qty + v_quantities[i]
        WHERE id = v_product_ids[i];

-- Reducir la cantidad del producto en la factura
        UPDATE "Transactions".bill_products
        SET qty = qty - v_quantities[i]
        WHERE bill_id = v_bill_id
        AND product_id = v_product_ids[i];

    END LOOP;

-- Cambio de estado de factura

    IF NOT EXISTS (
        SELECT 1
        FROM "Transactions".bill_products
        WHERE bill_id = v_bill_id
        AND qty > 0
    ) THEN
        UPDATE "Transactions".bills
        SET status = 'RETURNED'
        WHERE id = v_bill_id;
    ELSE
        UPDATE "Transactions".bills
        SET status = 'PARTIALLY_RETURNED'
        WHERE id = v_bill_id;
    END IF;

    -- Obtener el status
    SELECT status
    INTO v_status
    FROM "Transactions".bills
    WHERE id = v_bill_id;

-- Resumen de lo realizado
    RAISE NOTICE 'Devolucion realizada correctamente';
    RAISE NOTICE 'Factura: %', v_bill_id;
    RAISE NOTICE 'Estado de la factura: %', v_status;

END;
$$ LANGUAGE plpgsql;

COMMIT;
