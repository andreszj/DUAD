
BEGIN;

DO $$
DECLARE
-- Usuario, prodcuto y cantidad a comprar 
    v_user_id INTEGER := 4;
    v_product INTEGER := 1;
    v_qty INTEGER := 2;

-- Variables de almacenamiento
    v_bill_id INTEGER;
    v_stock INTEGER;
    v_price NUMERIC(10,2);
    v_total NUMERIC(10,2);

BEGIN

-- Existe usuario ?
    IF NOT EXISTS (
        SELECT *
        FROM "Transactions".users
        WHERE id = v_user_id
    ) THEN
        RAISE EXCEPTION 'El usuario con ID % no existe', v_user_id;
    END IF;

-- Existe producto? 
    SELECT price, qty
    INTO v_price, v_stock
    FROM "Transactions".products
    WHERE id = v_product;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'El producto con ID % no existe', v_product;
    END IF;

-- Existencias suficientes?
    IF v_stock < v_qty THEN
        RAISE EXCEPTION
            'Stock insuficiente para producto ID %. Disponible: %, solicitado: %',
            v_product,
            v_stock,
            v_qty;
    END IF;

-- Calculo e insertar datos nuevos 

    v_total := v_price * v_qty;

    INSERT INTO "Transactions".bills (user_id, date, total, status)
    VALUES (v_user_id, CURRENT_DATE, v_total, 'COMPLETED')
    RETURNING id INTO v_bill_id;

    INSERT INTO "Transactions".bill_products
        (bill_id, product_id, qty, unit_price)
    VALUES
        (v_bill_id, v_product, v_qty, v_price);

-- Reducir el stock 

    UPDATE "Transactions".products
    SET qty = qty - v_qty
    WHERE id = v_product;

-- Resumen de lo realizado 
    RAISE NOTICE 'Compra realizada correctamente';
    RAISE NOTICE 'Factura creada: %', v_bill_id;
    RAISE NOTICE 'Producto comprado: %', v_product;
    RAISE NOTICE 'Cantidad comprada: %', v_qty;
    RAISE NOTICE 'Total de la factura: %', v_total;

END;
$$ LANGUAGE plpgsql;

COMMIT;