
BEGIN;

DO $$
DECLARE
-- Usuario, prodcuto y cantidad a comprar 
    v_user_id INTEGER := 4;
    v_product_ids INTEGER[] := ARRAY[1, 5, 8];
    v_quantities INTEGER[] := ARRAY[2, 1, 2];

-- Variables de almacenamiento
    v_bill_id INTEGER;
    v_stock INTEGER;
    v_price NUMERIC(10,2);
    v_total NUMERIC(10,2) := 0;

    i INTEGER;

BEGIN

-- Existe usuario ?
    IF NOT EXISTS (
        SELECT *
        FROM "Transactions".users
        WHERE id = v_user_id
    ) THEN
        RAISE EXCEPTION 'El usuario con ID % no existe', v_user_id;
    END IF;

-- validacion

    FOR i IN 1..array_length(v_product_ids, 1)
    LOOP
        SELECT price, qty
        INTO v_price, v_stock
        FROM "Transactions".products
        WHERE id = v_product_ids[i]
        FOR UPDATE;
-- Existe producto?

        IF NOT FOUND THEN
            RAISE EXCEPTION 'El producto con ID % no existe', v_product_ids[i];
        END IF;

        IF v_quantities[i] <= 0 THEN
        RAISE EXCEPTION 'La cantidad debe ser mayor a 0';
        END IF;

-- Existencias suficientes?
        IF v_stock < v_quantities[i] THEN
            RAISE EXCEPTION
                'Stock insuficiente para producto ID %. Disponible: %, solicitado: %',
                v_product_ids[i],
                v_stock,
                v_quantities[i];
        END IF;

-- Calculo e insertar datos nuevos 

        v_total := v_total + (v_price * v_quantities[i]);

    END LOOP;

    INSERT INTO "Transactions".bills (user_id, date, total, status)
    VALUES (v_user_id, CURRENT_DATE, v_total, 'COMPLETED')
    RETURNING id INTO v_bill_id;

    FOR i IN 1..array_length(v_product_ids, 1)
    LOOP
        -- Obtener el precios
        SELECT price
        INTO v_price
        FROM "Transactions".products
        WHERE id = v_product_ids[i];

        INSERT INTO "Transactions".bill_products
            (bill_id, product_id, qty, unit_price)
        VALUES
            (v_bill_id, v_product_ids[i], v_quantities[i], v_price);

-- Reducir el stock 

        UPDATE "Transactions".products
        SET qty = qty - v_quantities[i]
        WHERE id = v_product_ids[i];

    END LOOP;
-- Resumen de lo realizado 
    RAISE NOTICE 'Compra realizada correctamente';
    RAISE NOTICE 'Factura creada: %', v_bill_id;
    -- RAISE NOTICE 'Producto comprado: %', v_product;
    -- RAISE NOTICE 'Cantidad comprada: %', v_qty;
    RAISE NOTICE 'Total de la factura: %', v_total;

END;
$$ LANGUAGE plpgsql;

COMMIT;