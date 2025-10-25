SELECT 'Общая выручка' AS metric, SUM(o.quantity * p.price)::text AS value
FROM orders o
JOIN products p ON o.product_id = p.id

UNION ALL

SELECT 'Средний чек', ROUND(AVG(o.quantity * p.price), 2)::text
FROM orders o
JOIN products p ON o.product_id = p.id

UNION ALL

SELECT 'ТОП-1 пользователь (по выручке)', 
       (SELECT u.name || ' — ' || SUM(o.quantity*p.price)
        FROM users u
        JOIN orders o ON u.id = o.user_id
        JOIN products p ON o.product_id = p.id
        GROUP BY u.name
        ORDER BY SUM(o.quantity*p.price) DESC
        LIMIT 1)::text

UNION ALL

SELECT 'Выручка по городам (топ-1)', 
       (SELECT u.city || ' — ' || SUM(o.quantity*p.price)
        FROM users u
        JOIN orders o ON u.id = o.user_id
        JOIN products p ON o.product_id = p.id
        GROUP BY u.city
        ORDER BY SUM(o.quantity*p.price) DESC
        LIMIT 1)::text

UNION ALL

SELECT 'Период данных', 
       TO_CHAR(MIN(order_date), 'YYYY-MM-DD') || ' — ' || TO_CHAR(MAX(order_date), 'YYYY-MM-DD')
FROM orders;
