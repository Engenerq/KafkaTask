DO
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'orders') THEN
        PERFORM pg_catalog.create_database('orders');
    END IF;
END
$$;

DO
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'payment') THEN
        PERFORM pg_catalog.create_database('payment');
    END IF;
END
$$;


DO
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'shipping') THEN
        PERFORM pg_catalog.create_database('shipping');
    END IF;
END
$$;


DO
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'notification') THEN
        PERFORM pg_catalog.create_database('notification');
    END IF;
END
$$;

\c orders
DROP USER IF EXISTS orders_user;
CREATE USER orders_user WITH PASSWORD 'orders_password';
GRANT ALL PRIVILEGES ON DATABASE orders TO orders_user;

CREATE TABLE IF NOT EXISTS orders
(
    uid    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email  TEXT NOT NULL,
    status TEXT NOT NULL
);

\c payment
DROP USER IF EXISTS payment_user;
CREATE USER payment_user WITH PASSWORD 'payment_password';
GRANT ALL PRIVILEGES ON DATABASE payment TO payment_user;

CREATE TABLE IF NOT EXISTS payment
(
    uid       UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_uid UUID NOT NULL,
    email     TEXT NOT NULL,
    status    TEXT NOT NULL
);

\c shipping
DROP USER IF EXISTS shipping_user;
CREATE USER shipping_user WITH PASSWORD 'shipping_password';
GRANT ALL PRIVILEGES ON DATABASE shipping TO shipping_user;

CREATE TABLE IF NOT EXISTS shipping
(
    uid       UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_uid UUID NOT NULL,
    email     TEXT NOT NULL,
    status    TEXT NOT NULL
);

\c notification
DROP USER IF EXISTS notification_user;
CREATE USER notification_user WITH PASSWORD 'notification_password';
GRANT ALL PRIVILEGES ON DATABASE notification TO notification_user;

CREATE TABLE IF NOT EXISTS notification
(
    uid       UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_uid UUID NOT NULL,
    email     TEXT NOT NULL,
    status    TEXT NOT NULL
);
