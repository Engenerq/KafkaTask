CREATE_ORDER = """
    INSERT INTO orders (email, status)
    VALUES ($1, $2)
    RETURNING uid as order_uid, email as user_email, status;
"""