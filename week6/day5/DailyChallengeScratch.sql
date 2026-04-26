-- Daily Challenge : Advanced Movie Data Analysis



-- 🌟 Task 1: Calculate the Average Budget Growth Rate for Each Production Company

-- Calculate the average budget growth rate for each production company across all movies they have produced.
--Use window functions to determine the budget growth rate and then calculate the average growth rate.

--TO calculate budget growth rate: A window function that calculates current budget divided by lag(1) of budget
WITH CompanyGrowth AS (
    SELECT 
        pc.company_name,
        m.title,
        m.budget,
        -- We partition by company to ensure we compare a company to its own history
        LAG(m.budget) OVER (PARTITION BY pc.company_id ORDER BY m.release_date) as prev_budget,
        -- Handle division by zero by turning 0 into NULL
        (m.budget::float / NULLIF(LAG(m.budget) OVER (PARTITION BY pc.company_id ORDER BY m.release_date), 0)) - 1 AS growth_rate
    FROM movies.movie m
    JOIN movies.movie_company mc ON m.movie_id = mc.movie_id
    JOIN movies.production_company pc ON mc.company_id = pc.company_id
)
SELECT 
    company_name,
    AVG(growth_rate) * 100 AS avg_percentage_growth
FROM CompanyGrowth
WHERE growth_rate IS NOT NULL
GROUP BY company_name
ORDER BY avg_percentage_growth DESC;

-- 🌟 Task 2: Determine the Most Consistently High-Rated Actor

-- Identify the actor who has appeared in the most movies that are rated above the average rating of all movies.
--Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.

--Assuming vote_average is the rating.
--Remember, a window function cannot be used in a WHERE.
--First: calculate average rating of all movies, either separately (CTE) or in a window function
--Then create a table with actor name, number of popular movies appeared WHERE m.rating > avg_rating, rank actors,
--and filter
WITH avg_rating AS (
SELECT AVG(vote_average) AS avg_rating FROM movie
)
SELECT p.person_name, COUNT(mc.movie_id) AS total_toprated_movies, RANK() OVER (ORDER BY COUNT(mc.movie_id) DESC)
FROM person p
JOIN movie_cast mc ON p.person_id = mc.person_id
JOIN movie m ON mc.movie_id = m.movie_id
WHERE m.vote_average > (SELECT avg_rating from avg_rating)
GROUP BY p.person_id, p.person_name
LIMIT 1

-- 🌟 Task 3: Calculate the Rolling Average Revenue for Each Genre

-- Calculate the rolling average revenue for movies within each genre, considering only the last three movies released
--in the genre. Use window functions with the ROWS frame specification to achieve this.

--I think it makes sense in this context to simply remove rows that have a budget of zero as they are faulty data
--and would mess up the rolling average.
SELECT m.title, g.genre_name, m.revenue, m.release_date,
AVG(m.revenue) OVER(PARTITION BY mg.genre_id ORDER BY m.release_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
AS rolling_avg_revenue
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id
WHERE m.revenue > 0



-- 🌟 Task 4: Identify the Highest-Grossing Movie Series

-- Identify the movie series (based on shared keywords) with the highest total revenue.
--Use window functions and CTEs to group movies by their series and calculate the total revenue.

--First figure out how we can identify movie series with shared keywords.
WITH SeriesKeywords AS (
    -- Find keywords that appear in at least 2 different movies
    SELECT 
        mk.keyword_id,
        k.keyword_name
    FROM movies.movie_keywords mk
    JOIN movies.keyword k ON mk.keyword_id = k.keyword_id
    GROUP BY mk.keyword_id, k.keyword_name
    HAVING COUNT(DISTINCT mk.movie_id) > 1 
       AND k.keyword_name ILIKE '%series%' -- focus on "series" keywords
)
SELECT * FROM SeriesKeywords;
SELECT 
    k.keyword_name AS series_name,
    m.title,
    m.release_date
FROM movies.movie m
JOIN movies.movie_keywords mk ON m.movie_id = mk.movie_id
JOIN movies.keyword k ON mk.keyword_id = k.keyword_id
WHERE k.keyword_name IN (
    -- Subquery to only get keywords that act as series connectors
    SELECT k2.keyword_name
    FROM movies.movie_keywords mk2
    JOIN movies.keyword k2 ON mk2.keyword_id = k2.keyword_id
    GROUP BY k2.keyword_name
    HAVING COUNT(DISTINCT mk2.movie_id) > 1
)
ORDER BY series_name, m.release_date;

SELECT 
    m.title,
    STRING_AGG(k.keyword_name, ', ') AS series_associations
FROM movies.movie m
JOIN movies.movie_keywords mk ON m.movie_id = mk.movie_id
JOIN movies.keyword k ON mk.keyword_id = k.keyword_id
WHERE m.title ILIKE '%part%'
GROUP BY m.title;

SELECT m.title
FROM movie m

--Experimenting with various queries using keywords didn't really help finding movie series. So I am trying
--combining looking at shared keywords with looking at shared significant words in titles, as well as markers of
--series: a colon, trailing numbers, or Roman numerals.
--Here is my answer to this task in this manner:
WITH SeriesIdentification AS (
    SELECT 
        m.movie_id,
        m.title,
        m.revenue,
        -- Using your refined logic to create the series bucket
        TRIM(BOTH ' -' FROM REGEXP_REPLACE(
            REGEXP_REPLACE(m.title, '^(The |A |An |Mr\. |Super |This is )', '', 'i'), 
            '(:.*|[ \t]+(Part|Episode)[ \t]+(I|V|X|\d)+|[ \t]+\d+|[ \t]+(I|II|III|IV|V|VI|VII|VIII|IX|X)+)$', 
            '', 'i'
        )) AS series_name
    FROM movies.movie m
    -- We only target movies that fit our series markers to define the base names
    WHERE m.title ~* '(:|Part[ \t]+(I|V|X|\d)+|Episode[ \t]+(I|V|X|\d)+|[ \t]+\d+|[ \t]+(I|II|III|IV|V|VI|VII|VIII|IX|X)+)$'
),
SeriesRevenue AS (
    SELECT 
        series_name,
        SUM(revenue) AS total_series_revenue,
        COUNT(*) AS movie_count,
        -- Window function to rank series by their total revenue
        RANK() OVER (ORDER BY SUM(revenue) DESC) as revenue_rank
    FROM SeriesIdentification
    WHERE LENGTH(series_name) > 2
    GROUP BY series_name
)
SELECT 
    revenue_rank,
    series_name,
    total_series_revenue,
    movie_count
FROM SeriesRevenue
WHERE revenue_rank = 1;

WITH SeriesCandidates AS (
    SELECT 
        m.movie_id,
        m.title,
        -- 1. Remove noise prefixes
        -- 2. Strip away Colons, 'Part', 'Episode', and trailing digits/Roman numerals
        -- 3. Clean up any trailing dashes or whitespace left over
        TRIM(BOTH ' -' FROM REGEXP_REPLACE(
            REGEXP_REPLACE(m.title, '^(The |A |An |Mr\. |Super |This is )', '', 'i'), 
            '(:.*|[ \t]+(Part|Episode)[ \t]+(I|V|X|\d)+|[ \t]+\d+|[ \t]+(I|II|III|IV|V|VI|VII|VIII|IX|X)+)$', 
            '', 'i'
        )) AS base_name
    FROM movies.movie m
    -- Filter for titles that look like installments (including Episode)
    WHERE m.title ~* '(:|Part[ \t]+(I|V|X|\d)+|Episode[ \t]+(I|V|X|\d)+|[ \t]+\d+|[ \t]+(I|II|III|IV|V|VI|VII|VIII|IX|X)+)$'
)
SELECT 
    base_name,
    COUNT(*) AS movie_count,
    STRING_AGG(title, ' | ' ORDER BY title) AS series_members
FROM SeriesCandidates
WHERE LENGTH(base_name) > 2
GROUP BY base_name
HAVING COUNT(*) > 1
ORDER BY movie_count DESC;

select m.title from movie m

where title ILIKE '%star wars%'

SELECT 
    k.keyword_name AS series_name,
    m.title,
    m.release_date
FROM movies.movie m
JOIN movies.movie_keywords mk ON m.movie_id = mk.movie_id
JOIN movies.keyword k ON mk.keyword_id = k.keyword_id
where m.title ILIKE '%star wars%'

SELECT * FROM movie
select * from movie_keywords
select * from keyword


SELECT 
    m.title,
    STRING_AGG(k.keyword_name, ', ') AS series_associations
FROM movies.movie m
JOIN movies.movie_keywords mk ON m.movie_id = mk.movie_id
JOIN movies.keyword k ON mk.keyword_id = k.keyword_id
WHERE m.title ILIKE '%return of the jedi%'
GROUP BY m.title;