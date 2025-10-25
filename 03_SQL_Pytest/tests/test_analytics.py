# tests/test_analytics.py
#тесты для аналитических SQL-запросов по продажам.
#проверяем общую выручку, средний чек, ТОП-3 пользователей и месячную выручку.

def test_total_revenue(cur):
    """
    проверяем общую сумму выручки
    считается как сумма (количество * цена) по всем заказам
    """
    cur.execute("""
        SELECT COALESCE(SUM(o.quantity * p.price), 0)
        FROM orders o
        JOIN products p ON p.id = o.product_id
    """)
    total = cur.fetchone()[0]
    #проверяем, что сумма совпадает с ожидаемой (по тестовым данным)
    assert total == 493500, f"Ожидали 493500, получили {total}"


def test_avg_order_amount(cur):
    """
    проверяем среднюю сумму заказа
    формула: среднее значение (quantity * price) по всем заказам
    """
    cur.execute("""
        SELECT ROUND(AVG(o.quantity * p.price), 2)
        FROM orders o
        JOIN products p ON p.id = o.product_id
    """)
    avg = float(cur.fetchone()[0])
    assert avg == 49350.00, f"Ожидали 49350.00, получили {avg}"


def test_top3_users_count(cur):
    """
    проверяем, что аналитика по ТОП-3 пользователям возвращает ровно 3 строки
    """
    cur.execute("""
        SELECT u.name, SUM(o.quantity * p.price) AS revenue
        FROM orders o
        JOIN users u ON u.id = o.user_id
        JOIN products p ON p.id = o.product_id
        GROUP BY u.name
        ORDER BY revenue DESC
        LIMIT 3
    """)
    rows = cur.fetchall()
    assert len(rows) == 3, f"Должно быть 3 строки, получили {len(rows)}"


def test_monthly_revenue(cur):
    """
    проверяем распределение выручки по месяцам.
    должен быть один месяц и общая сумма 493500 (по тестовым данным).
    """
    cur.execute("""
        SELECT to_char(o.order_date, 'YYYY-MM') AS ym,
               SUM(o.quantity * p.price) AS revenue
        FROM orders o
        JOIN products p ON p.id = o.product_id
        GROUP BY ym
        ORDER BY ym
    """)
    rows = cur.fetchall()

    # rows — список кортежей вида [('2025-01', 493500)]
    assert len(rows) == 1 and rows[0][1] == 493500, f"Неожиданный результат: {rows}"
