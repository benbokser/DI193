-- 🌟 Exercise 1: Movie Rankings and Analysis


-- SQL Dataset we will be using

--     Movies Database


-- Task 1: Rank Movies by Popularity within Each Genre

-- Use the RANK() function to rank movies by their popularity within each genre.
--Display the genre name, movie title, and their rank based on popularity.
SELECT g.genre_name, m.title,
RANK() OVER(PARTITION BY mg.genre_id ORDER BY m.popularity DESC) AS genre_popularity_rank
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id


-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company
WITH company_revenue_ranks AS ( 
SELECT m.title, pc.company_name, m.revenue,
RANK() OVER(PARTITION BY mc.company_id ORDER BY m.revenue DESC) AS company_revenue_rank
FROM movie m
JOIN movie_company mc ON m.movie_id = mc.movie_id
JOIN production_company pc ON mc.company_id = pc.company_id)
SELECT * FROM company_revenue_ranks
WHERE company_revenue_rank <= 3 


-- Use the NTILE() function to divide the movies produced by each production company into quartiles based on revenue.
--Display the company name, movie title, revenue, and quartile.
SELECT pc.company_name, m.title, m.revenue,
NTILE(4) OVER(PARTITION BY mc.company_id ORDER BY m.revenue) AS company_revenue_quartile
FROM movie m
JOIN movie_company mc ON m.movie_id = mc.movie_id
JOIN production_company pc ON mc.company_id = pc.company_id


-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre

-- Use the SUM() function with the ROWS frame specification to calculate the running total
--of movie budgets within each genre. Display the genre name, movie title, budget, and running total budget

--The question did not note how the rows should be ordered, but for a running total budget to make much sense,
--there should be a time-based aspect. So I am ordering it by date.
SELECT g.genre_name, m.title, m.budget,
SUM(m.budget) OVER(PARTITION BY mg.genre_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_genre_total_budget
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id
ORDER BY m.release_date





-- Task 4: Identify the Most Recent Movie for Each Genre

-- Use the FIRST_VALUE() function to find the most recent movie within each genre based on the release date.
--Display the genre name, movie title, and release date.
WITH my_cte AS (
SELECT g.genre_name, m.title, m.release_date,
FIRST_VALUE(m.title) OVER(PARTITION BY mg.genre_id ORDER BY m.release_date DESC)
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id)
SELECT genre_name, title, release_date FROM my_cte
WHERE title = first_value



-- 🌟 Exercise 2: Cast and Crew Performance Analysis


-- Task 1: Rank Actors by Their Appearance in Movies

-- Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in.
--Display the actor’s name and their rank.

SELECT p.person_name,
DENSE_RANK() OVER(ORDER BY COUNT(mc.movie_id) DESC) AS appearances_rank
from person p
JOIN movie_cast mc ON p.person_id = mc.person_id
GROUP BY p.person_name

-- Task 2: Identify the Top Director by Average Movie Rating

-- Use a CTE and the RANK() function to find the director with the highest average movie rating.
--Display the director’s name and their average rating.

--I assume the rating is captured by vote_average.
WITH director_ratings AS (
SELECT p.person_name, AVG(m.vote_average) AS avg_rating,
RANK() OVER(ORDER BY AVG(m.vote_average) DESC)
FROM person p
JOIN movie_crew mc ON p.person_id = mc.person_id
JOIN movie m ON mc.movie_id = m.movie_id
WHERE mc.job = 'Director'
GROUP BY p.person_name
)
SELECT * FROM director_ratings
WHERE rank = 1

-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor

-- Use the SUM() function to calculate the cumulative revenue of movies acted by each actor.
--Display the actor’s name and the cumulative revenue.
SELECT p.person_name,
SUM(m.revenue) OVER(PARTITION BY p.person_id ORDER BY m.release_date ASC) AS cumulative_revenue
FROM person p
JOIN movie_cast mc ON p.person_id = mc.person_id
JOIN movie m ON mc.movie_id = m.movie_id

-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget

-- Use a CTE and a window function to find the director whose movies have the highest total budget.
--Display the director’s name and the total budget.

--CTE for director total budget:

--Actually it seems pretty unnecessary to do this with a window function, as GROUP BY and MAX)() is sufficient.
--Either way, here it is:
WITH director_total_budgets AS (
SELECT p.person_name, SUM(m.budget),
RANK() OVER(ORDER BY SUM(m.budget) DESC)
FROM person p
JOIN movie_crew mc ON p.person_id = mc.person_id
JOIN movie m ON mc.movie_id = m.movie_id
WHERE mc.job = 'Director'
GROUP BY p.person_name
)
SELECT * FROM director_total_budgets
WHERE rank = 1
