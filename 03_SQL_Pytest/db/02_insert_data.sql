-- FILE: 02_insert_data.sql
INSERT INTO users (name,email,age,city) VALUES
('Анна Иванова','anna@mail.ru',25,'Москва'),
('Илья Петров','ilya@mail.ru',32,'Казань'),
('Мария Смирнова','maria@mail.ru',29,'Екатеринбург'),
('Дмитрий Кузнецов','dmitriy@mail.ru',41,'Новосибирск'),
('Елена Соколова','elena@mail.ru',36,'Санкт-Петербург');

INSERT INTO products (name,category,price) VALUES
('Ноутбук Lenovo IdeaPad','Электроника',65000),
('Смартфон Samsung Galaxy','Электроника',72000),
('Наушники Sony WH-1000XM5','Аудио',32000),
('Кофемашина DeLonghi','Бытовая техника',45000),
('Книга "Чистый код"','Книги',1500);

INSERT INTO orders (user_id,product_id,quantity,order_date) VALUES
(1,1,1,'2025-09-10'),
(1,5,2,'2025-09-12'),
(2,2,1,'2025-09-15'),
(2,3,1,'2025-09-16'),
(3,4,1,'2025-09-18'),
(3,5,3,'2025-09-20'),
(4,1,2,'2025-09-22'),
(5,2,1,'2025-09-25'),
(5,3,2,'2025-09-27'),
(5,5,4,'2025-09-28');

--быстрая проверка
SELECT COUNT(*) AS users_cnt   FROM users;
SELECT COUNT(*) AS products_cnt FROM products;
SELECT COUNT(*) AS orders_cnt   FROM orders;
