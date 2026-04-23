-- 🌟 Exercise 1: Complex Subquery Analysis


-- SQL Dataset we will be using

--     Olympic Data

--     Task 1: Find the average age of competitors who have won at least one medal, grouped by the type of medal they won.
-- Use a correlated subquery to achieve this.
--Unclear if this should be done for every person who has won at least one medal once, or for each games they played in.
--Here is how to do it for every person:
SELECT 
    m.medal_name,
    (
        SELECT AVG(dist_age.age)
        FROM (
            SELECT DISTINCT gc.person_id, gc.age
            FROM games_competitor gc
            JOIN competitor_event ce ON gc.id = ce.competitor_id
            WHERE ce.medal_id = m.id
        ) AS dist_age
    ) AS avg_age
FROM medal m
WHERE m.id <> 4;

--To do the above task for every competitor (counting every person seperately for each games played in):
SELECT 
    m.medal_name,
    (
        SELECT AVG(dist_age.age)
        FROM (
            SELECT DISTINCT gc.id, gc.age
            FROM games_competitor gc
            JOIN competitor_event ce ON gc.id = ce.competitor_id
            WHERE ce.medal_id = m.id
        ) AS dist_age
    ) AS avg_age
FROM medal m
WHERE m.id <> 4;
--     Task 2: Identify the top 5 regions with the highest number of unique competitors who have participated
--             in more than 3 different events. Use nested subqueries to filter and aggregate the data.
--Again, here is the above task looking at distinct persons, assuming unique competitors means persons, who have
--participated in more than 3 different events overall.
SELECT region, count(person) AS num_competitors
FROM (--table of unique competitors who participated in more than 3 different events, w region:
SELECT gc.person_id AS person, SUM(ce.event_id) AS sum, nr.region_name AS region
FROM competitor_event ce
JOIN games_competitor gc ON ce.competitor_id = gc.id
JOIN person_region pr ON gc.person_id = pr.person_id
JOIN noc_region nr ON pr.region_id = nr.id
GROUP BY nr.region_name, gc.person_id
HAVING SUM(event_id) > 3
)
GROUP BY region
ORDER BY count(person) DESC
LIMIT 5


--Here is the above task if we are looking at unique competitors seperately for each games rather than people, counting
--only those who participated in more than 3 different events in the same games.
SELECT region, count(comp) AS num_competitors
FROM (--table of unique competitors who participated in more than 3 different events, w region:
SELECT gc.id AS comp, SUM(ce.event_id) AS sum, nr.region_name AS region
FROM competitor_event ce
JOIN games_competitor gc ON ce.competitor_id = gc.id
JOIN person_region pr ON gc.person_id = pr.person_id
JOIN noc_region nr ON pr.region_id = nr.id
GROUP BY nr.region_name, gc.id
HAVING SUM(event_id) > 3
)
GROUP BY region
ORDER BY count(comp) DESC
LIMIT 5

--     Task 3: Create a temporary table to store the total number of medals won by each competitor
--and filter to show only those who have won more than 2 medals. Use subqueries to aggregate the data.
--Again, the code below answers the above question to store the total number of medals won by each person.
CREATE TEMP TABLE career_medals AS
SELECT 
    p.id AS person_id,
    p.full_name,
    (
        SELECT COUNT(*)
        FROM competitor_event ce
        JOIN games_competitor gc ON ce.competitor_id = gc.id
        WHERE gc.person_id = p.id 
          AND ce.medal_id <> 4
    ) AS total_medals
FROM person p;
--Note: This is a very slow query. It is preferable to do a LEFT JOIN with GROUP BY.
--I only did this with a subquery because I was asked.
--The LEFT JOIN would look like this:
CREATE TEMP TABLE career_medals AS
SELECT 
    p.id AS person_id,
    p.full_name,
    COUNT(ce.medal_id) AS total_medals
FROM person p
LEFT JOIN games_competitor gc ON p.id = gc.person_id
LEFT JOIN competitor_event ce ON gc.id = ce.competitor_id AND ce.medal_id <> 4
GROUP BY p.id, p.full_name;
--Filtering to show only those who have won more than 2 medals:
SELECT * FROM career_medals 
WHERE total_medals > 2

--To do the above task for each competitor (for each games separately, not totalling a person's medals across games):
CREATE TEMP TABLE games_medals AS
SELECT 
    gc.id AS comp_id,
    (SELECT COUNT(*)
        FROM competitor_event ce
        JOIN games_competitor gc1 ON ce.competitor_id = gc1.id
        WHERE gc.id = gc1.id 
          AND ce.medal_id <> 4
    ) AS total_medals
FROM games_competitor gc;

--An alternate way to do this with subqueries, which also is slow:
CREATE TEMP TABLE games_medals AS
SELECT gc.id,
(SELECT
count(ce.event_id) AS
FROM games_competitor gc1
LEFT JOIN competitor_event ce
ON ce.competitor_id = gc.id
WHERE ce.medal_id <> 4
AND gc.id = gc1.id) AS medals
FROM games_competitor gc
ORDER BY gc.id

SELECT gc.id,

--A better way to do this with LEFT JOIN and GROUP BY:
CREATE TEMP TABLE games_medals AS
SELECT 
    p.id AS person_id,
    p.full_name, gc.id AS competitor_id,
    COUNT(ce.medal_id) AS total_medals
FROM person p
LEFT JOIN games_competitor gc ON p.id = gc.person_id
LEFT JOIN competitor_event ce ON gc.id = ce.competitor_id AND ce.medal_id <> 4
GROUP BY p.id, p.full_name, gc.id
ORDER BY p.id, gc.id;
--And to filter this table to show only those who have won more than 2 medals:
SELECT * FROM games_medals 
WHERE total_medals > 2

--     Task 4: Use a subquery within a DELETE statement
--to remove records of competitors who have not won any medals from a temporary table created for analysis.
--Again, for the temp table showing total medals over a person's career:
DELETE FROM career_medals
WHERE total_medals = 0
--For the temp table showing a competitor's medals in each games:
DELETE FROM games_medals
WHERE total_medals = 0
--In both cases it is very simple to remove records of competitors who have not won any medals,
--and I could not find any way a subquery could be useful or used at all. I did so without a subquery.


-- 🌟 Exercise 2: Advanced Data Manipulation and Optimization

--     Task 1: Update the heights of competitors based on the average height of competitors from the same region.
-- Use a correlated subquery within the UPDATE statement.
--Again, referencing each person only once, which makes sense since counting a person several times for the regional average
--for the several games they played in wouldn't make sense for calculating the average height of competitors from a region:
UPDATE person
SET height = (
    SELECT AVG(p2.height)
    FROM person p2
    JOIN person_region pr2 ON p2.id = pr2.person_id
    WHERE pr2.region_id = (
        SELECT pr1.region_id 
        FROM person_region pr1 
        WHERE pr1.person_id = person.id
        LIMIT 1
    )
)
--     Task 2: Insert new records into a temporary table for competitors who participated in
-- more than one event in the same games and list their total number of events participated.
--Use nested subqueries for filtering.
--I assume this is referring to competitors for each games, meaning competitor_id,
--even if we list the same person several times for the several games they played in,
--because it is asking for competitors who played in multiple events in the same games.
CREATE TEMP TABLE multi_event_athletes (comp_id INT, num_events INT)
--This is easier to do with a GROUP BY and HAVING:
INSERT INTO multi_event_athletes (comp_id, num_events)
SELECT competitor_id, COUNT(event_id) AS num_events
FROM competitor_event
GROUP BY competitor_id
HAVING count(event_id) >1

--Yet we were asked to this with a nested subquery (instead of having), so this is how:
INSERT INTO multi_event_athletes (comp_id, num_events)
SELECT competitor_id, num_events FROM
(SELECT competitor_id, COUNT(event_id) AS num_events
FROM competitor_event
GROUP BY competitor_id
)
WHERE num_events > 1

--     Task 3: Identify regions where the average number of medals won per competitor is greater than the overall average.
--Use subqueries to calculate and compare averages.
--The average to calculate should include competitors with zero medals.
--Again, unclear if this means average number of medals won per person over a career or per competitor in each games.
--Per person over a career:
--Building this up:
--overall average of medals per person:
--medals per person: we have the career_medals table, but want it before the records with zero medals were deleted.
--So if those records were deleted we will drop and recreate the career_medals table so it has the zero medal records.
--overall average of medals per person:
SELECT AVG(total_medals)
FROM career_medals
--full query:
SELECT pr.region_id, nr.region_name, AVG(cm.total_medals) AS avg_medals_person
FROM person_region pr
JOIN person p ON pr.person_id = p.id
JOIN noc_region nr ON pr.region_id = nr.id
JOIN career_medals cm ON p.id = cm.person_id
GROUP BY pr.region_id, nr.region_name
HAVING AVG(cm.total_medals) > (SELECT AVG(total_medals) FROM career_medals)

--Now the query per competitor in a games:
SELECT pr.region_id, nr.region_name, AVG(cm.total_medals) AS avg_medals_person
FROM person_region pr
JOIN person p ON pr.person_id = p.id
JOIN noc_region nr ON pr.region_id = nr.id
JOIN games_medals cm ON p.id = cm.person_id
GROUP BY pr.region_id, nr.region_name
HAVING AVG(cm.total_medals) > (SELECT AVG(total_medals) FROM games_medals)

--     Task 4: Create a temporary table to track competitors’ participation across different seasons
--and identify those who have participated in both Summer and Winter games.
--Here we are clearly looking at persons.

CREATE TEMP TABLE person_seasons AS
SELECT
p.id AS person_id, p.full_name,
MAX(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) AS played_summer,
MAX(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) AS played_winter
FROM person p
LEFT JOIN games_competitor gc ON p.id = gc.person_id
LEFT JOIN games g ON gc.games_id = g.id
GROUP BY p.id, p.full_name;
--To identify those who have participated in both Summer and Winter games:
SELECT * FROM person_seasons
WHERE played_summer = 1 AND played_winter = 1