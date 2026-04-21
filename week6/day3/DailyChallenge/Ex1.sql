-- You are going to practice tables relationships

-- Part I

--1     Create 2 tables : Customer and Customer profile. They have a One to One relationship.
--         A customer can have only one profile, and a profile belongs to only one customer
--         The Customer table should have the columns : id, first_name, last_name NOT NULL
CREATE TABLE customer (
id SERIAL PRIMARY KEY,
first_name VARCHAR(30),
last_name VARCHAR(30) NOT NULL
)
--         The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean),
--customer_id (a reference to the Customer table)
CREATE TABLE customer_profile (
id SERIAL PRIMARY KEY,
isLoggedIn BOOLEAN DEFAULT FALSE,
customer_id INT REFERENCES customer(id)
);
--2     Insert those customers
--         John, Doe
--         Jerome, Lalu
--         Lea, Rive
INSERT INTO customer (first_name, last_name) VALUES
	('John','Doe'),
	('Jerome', 'Lalu'),
	('Lea', 'Rive');
--3     Insert those customer profiles, use subqueries
--         John is loggedIn
--         Jerome is not logged in
INSERT INTO customer_profile (isLoggedIn, customer_id) VALUES
	(TRUE,(SELECT id FROM customer WHERE first_name = 'John')),
	(FALSE,(SELECT id FROM customer WHERE first_name = 'Jerome'))
--4     Use the relevant types of Joins to display:
--         The first_name of the LoggedIn customers
SELECT c.first_name FROM customer c
JOIN customer_profile cp
ON c.id = cp.customer_id
WHERE cp.isLoggedIn = TRUE
--         All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
SELECT c.first_name, cp.isLoggedIn FROM customer c
LEFT JOIN customer_profile cp
ON c.id = cp.customer_id

--         The number of customers that are not LoggedIn
SELECT count(c.id)  FROM customer c
LEFT JOIN customer_profile cp
ON c.id = cp.customer_id
WHERE cp.isLoggedIn = FALSE