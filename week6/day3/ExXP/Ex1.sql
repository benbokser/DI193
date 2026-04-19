-- 🌟 Exercise 1: DVD Rental
-- Instructions

--1     Get a list of all the languages, from the language table.
SELECT name FROM language
--2     Get a list of all films joined with their languages – select the following details :
--film title, description, and language name.
SELECT f.title, f.description, l.name
FROM film f
JOIN language l
ON f.language_id = l.language_id
--3     Get all languages, even if there are no films in those languages– select the following details :
--film title, description, and language name.
SELECT f.title, f.description, l.name
FROM language l
LEFT JOIN film f
ON f.language_id = l.language_id

--4     Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE TABLE new_film (
id SERIAL,
name VARCHAR(255),
PRIMARY KEY(id)
);
INSERT INTO new_film (name)
VALUES
	('The Lion King'),
	('The Dark Knight'),
	('Batman Returns');
--confirming:
SELECT * FROM new_film
--5     Create a new table called customer_review, which will contain film reviews that customers will make.
--     Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
--     It should have the following columns:
--         review_id – a primary key, non null, auto-increment.
--         film_id – references the new_film table. The film that is being reviewed.
--         language_id – references the language table. What language the review is in.
--         title – the title of the review.
--         score – the rating of the review (1-10).
--         review_text – the text of the review. No limit on the length.
--         last_update – when the review was last updated.
CREATE TABLE customer_review (
review_id SERIAL,
film_id INT,
language_id INT,
title VARCHAR(50),
score INT,
review_text TEXT,
last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (review_id),
FOREIGN KEY (film_id) REFERENCES new_film (id) ON DELETE CASCADE,
FOREIGN KEY (language_id) REFERENCES language (language_id) ON DELETE CASCADE
)
--     Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review (film_id, language_id, title, score, review_text) 
VALUES
	(1, 1, 'Great Movie', 10, 'Wow! What an amazing movie. I loved it.'),
	(2, 1, 'Enjoyable Film', 9, 'A very enjoyable film. Highly recommended.');

--     Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film WHERE id=1;
SELECT * FROM customer_review
--The customer_review table is updated; the review of the deleted film is deleted.