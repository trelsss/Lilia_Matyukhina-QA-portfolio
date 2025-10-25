--пользователи без заказов
SELECT u.id, u.name
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE o.id IS NULL;

--user_id / product_id (проверка связей)
SELECT o.id AS order_id, o.user_id
FROM orders o LEFT JOIN users u ON u.id=o.user_id
WHERE u.id IS NULL;

SELECT o.id AS order_id, o.product_id
FROM orders o LEFT JOIN products p ON p.id=o.product_id
WHERE p.id IS NULL;

--невалидные значения
SELECT
  (SELECT COUNT(*) FROM products WHERE price    <= 0) AS bad_prices,
  (SELECT COUNT(*) FROM orders   WHERE quantity <= 0) AS bad_quantities;

--дубликаты email
SELECT email, COUNT(*) dup_cnt
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
