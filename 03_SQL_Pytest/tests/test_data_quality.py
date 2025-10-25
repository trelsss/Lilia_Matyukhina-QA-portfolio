#tests/test_db_integrity.py
#набор простых интеграционных проверок целостности БД.

def test_users_without_orders(cur):
    """
    проверяем, что нет пользователей без заказов
    если хотя бы один пользователь без заказов есть тест падает
    """
    cur.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM users u
            WHERE NOT EXISTS (
                SELECT 1
                FROM orders o
                WHERE o.user_id = u.id
            )
        )
    """)
    has_orphans = cur.fetchone()[0]  #True/False
    assert not has_orphans, "есть пользователи без заказов (несвязанная запись в users)."


def test_invalid_fk_user_in_orders(cur):
    """
    проверяем внешние ключи: каждая строка в orders.user_id должна ссылаться на users.id.
    """
    cur.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM orders o
            LEFT JOIN users u ON u.id = o.user_id
            WHERE u.id IS NULL
        )
    """)
    has_broken_fk = cur.fetchone()[0]
    assert not has_broken_fk, "найдены невалидные ссылки FK: orders.user_id - users.id."


def test_invalid_fk_product_in_orders(cur):
    """
    проверяем внешние ключи: каждая строка в orders.product_id должна ссылаться на products.id
    """
    cur.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM orders o
            LEFT JOIN products p ON p.id = o.product_id
            WHERE p.id IS NULL
        )
    """)
    has_broken_fk = cur.fetchone()[0]
    assert not has_broken_fk, "найдены невалидные ссылки FK: orders.product_id → products.id."


def test_non_negative_values(cur):
    """
    базовая бизнес-валидация:
    - цена товара должна быть>0
    - количество в заказе должно быть>0
    """
    cur.execute("SELECT COUNT(*) FROM products WHERE price <= 0")
    bad_prices = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM orders WHERE quantity <= 0")
    bad_qty = cur.fetchone()[0]

    assert bad_prices == 0 and bad_qty == 0, (
        f"невалидные значения: products.price<=0={bad_prices}, orders.quantity<=0={bad_qty}"
    )


def test_unique_emails(cur):
    """
    проверяем уникальность email в таблице users
    """
    cur.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM (
                SELECT email
                FROM users
                GROUP BY email
                HAVING COUNT(*) > 1
            ) dup
        )
    """)
    has_dupes = cur.fetchone()[0]
    assert not has_dupes, "есть дубликаты email в users."
