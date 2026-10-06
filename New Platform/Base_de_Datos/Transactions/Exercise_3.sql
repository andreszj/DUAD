
BEGIN;

DO $$
DECLARE
-- Definicion de factura, producto y cantidad a retornar
    v_bill_id INTEGER := 4;
    v_product_id INTEGER := 1;
    v_quantity INTEGER := 1;

-- Variables de almacenamiento
    v_purchased_qty INTEGER;

BEGIN

-- Factura existe?
    IF NOT EXISTS (
        SELECT *
        FROM "Transactions".bills
        WHERE id = v_bill_id
    ) THEN
        RAISE EXCEPTION 'La factura con ID % no existe', v_bill_id;
    END IF;

-- Producto existe en la factura?
    SELECT qty
    INTO v_purchased_qty
    FROM "Transactions".bill_products
    WHERE bill_id = v_bill_id
    AND product_id = v_product_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION
            'El producto con ID % no pertenece a la factura %',
            v_product_id,
            v_bill_id;
    END IF;

-- Cantidad a retornar es valida?
    IF v_quantity <= 0 THEN
        RAISE EXCEPTION
            'La cantidad a retornar debe ser mayor a 0';
    END IF;

-- Cantidad a retornar no puede superar la cantidad comprada
    IF v_quantity > v_purchased_qty THEN
        RAISE EXCEPTION
            'No se pueden retornar % unidades. Solo se compraron %',
            v_quantity,
            v_purchased_qty;
    END IF;

-- Aumentar el stock con la cantidad retornada
    UPDATE "Transactions".products
    SET qty = qty + v_quantity
    WHERE id = v_product_id;

-- Reducir la cantidad del producto en la factura
    UPDATE "Transactions".bill_products
    SET qty = qty - v_quantity
    WHERE bill_id = v_bill_id
    AND product_id = v_product_id;

-- Resumen de lo realizado
    RAISE NOTICE 'Devolucion realizada correctamente';
    RAISE NOTICE 'Factura: %', v_bill_id;
    RAISE NOTICE 'Producto retornado: %', v_product_id;
    RAISE NOTICE 'Cantidad retornada: %', v_quantity;

END;
$$ LANGUAGE plpgsql;

COMMIT;
