-- 🌟 Exercise 2 : DVD Rental
-- Instructions

--1     Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
SET language_id = 2
WHERE film_id IN (5,6,7)
--2     Which foreign keys (references) are defined for the customer table?
--How does this affect the way in which we INSERT into the customer table?
--In the customer table, address_id is a foreign key that references address.address_id.
--This affects the way in which we INSERT into the customer table in that the address_id in any row we add to customer
--must be an address_id that exists in address.
--3     We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE customer_review
--It is easy. It doesn't need extra checking.
--4     Find out how many rentals are still outstanding (ie. have not been returned to the store yet).

SELECT COUNT(1) FROM rental WHERE return_date IS NULL

--5     Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
--The instructions are unclear. Does this mean the 30 most expensive inventory items, or the 30 most expensive films
--(counting duplicate inventory items only once)? Because the instructions say most expensive movies, I assume it means
--films, counting duplicate inventory items only once. And does expensive mean rental_rate or replacement_cost?
--I assume it means rental_rate. But since there are more than 30 movies with a rental_rate of 4.99, I will order by both.
SELECT DISTINCT f.* FROM film f
JOIN inventory i
ON f.film_id = i.film_id
JOIN rental r
ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NULL
ORDER BY f.rental_rate DESC, replacement_cost DESC
LIMIT 30

--6     Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies,
--but he can’t remember their names. Can you help him find which movies he wants to rent?
--         The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT f.* FROM film f
JOIN film_actor fa
ON f.film_id = fa.film_id
JOIN actor a
ON fa.actor_id = a.actor_id
WHERE a.first_name = 'Penelope' AND a.last_name = 'Monroe' AND f.description ILIKE '%sumo%'
--ANSWER: 'Park Citizen'
--         The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT * FROM film
WHERE description ILIKE '%documentary%' AND length < 60 AND rating ='R'
--ANSWER: 'Crossing Divorce'
--         The 3rd film : A film that his friend Matthew Mahan rented.
--			He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT f.* FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan' AND f.rental_rate > 4 AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01'
--ANSWER: 'Sugar Wonka'
--         The 4th film : His friend Matthew Mahan watched this film, as well.
--It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT DISTINCT f.* FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan' AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY replacement_cost DESC
--It's unclear how expensive it was, but with the films ranked by replacement_cost,
--the highest replacement cost film is 'Stone Fire.'