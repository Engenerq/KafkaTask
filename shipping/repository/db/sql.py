CREATE_SHIPPING = """
    INSERT INTO shipping (order_uid, email, status)
    VALUES ($1, $2, $3)
    RETURNING uid, order_uid, email, status;
"""
