CREATE DATABASE public;

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL);
INSERT INTO items (item_id, item_name, price)
VALUES 
    (1, 'Small Desk', 100),
    (2, 'Large Desk', 300),
    (3, 'Fan', 80);
INSERT INTO customers (customer_id, first_name, last_name)
VALUES 
    (1, 'Greg', 'Jones'),
    (2, 'Sandra', 'Jones'),
    (3, 'Scott', 'Scott'),
    (4, 'Trevor', 'Green'),
    (5, 'Melanie', 'Johnson');

	
--Queries:

--1: All the items.
SELECT * FROM items;

--2: All the items with a price above 80 (80 not included).
SELECT * FROM items
WHERE price > 80;

--3: All the items with a price below 300. (300 included)
SELECT * FROM items
WHERE price < 300;

--4: All customers whose last name is ‘Smith’ (What will be your outcome?).
SELECT * FROM customers
WHERE last_name = 'Smith';
--Outcome is empty.

--5: All customers whose last name is ‘Jones’.
SELECT * FROM customers
WHERE last_name = 'Jones';

--6: All customers whose firstname is not ‘Scott’.
SELECT * FROM customers
WHERE first_name <> 'Scott';