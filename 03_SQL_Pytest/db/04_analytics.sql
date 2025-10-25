-- Общая выручка
SELECT SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p ON p.id = o.product_id;

-- ТОП-3 пользователей по выручке
SELECT u.name, SUM(o.quantity*p.price) AS revenue
FROM orders o
JOIN users u ON u.id=o.user_id
JOIN products p ON p.id=o.product_id
GROUP BY u.name
ORDER BY revenue DESC
LIMIT 3;

-- ТОП товаров по выручке
SELECT p.name, SUM(o.quantity) AS qty, SUM(o.quantity*p.price) AS revenue
FROM orders o JOIN products p ON p.id=o.product_id
GROUP BY p.name
ORDER BY revenue DESC;

--средний чек
SELECT ROUND(AVG(o.quantity*p.price), 2) AS avg_order_amount
FROM orders o JOIN products p ON p.id=o.product_id;

--выручка по городам
SELECT u.city, u.name, COUNT(o.id) AS orders_cnt, SUM(o.quantity*p.price) AS revenue
FROM users u
LEFT JOIN orders o ON o.user_id=u.id
LEFT JOIN products p ON p.id=o.product_id
GROUP BY u.city, u.name
ORDER BY revenue DESC;

--помесячная выручка
SELECT TO_CHAR(o.order_date, 'YYYY-MM') AS month,
       SUM(o.quantity*p.price) AS revenue
FROM orders o JOIN products p ON p.id=o.product_id
GROUP BY month
ORDER BY month;
