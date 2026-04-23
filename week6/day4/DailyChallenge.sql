-- 🌟 Exercise 1: Detailed Medal Analysis


-- SQL Dataset we will be using

--     Olympic Data

-- Task 1: Identify competitors who have won at least one medal in events spanning both Summer and Winter Olympics.
-- Create a temporary table to store these competitors and their medal counts for each season,
--and then display the contents of this table.

-- I assume this means competitors who have won at least one medal in both Summer and Winter Olympics:
CREATE TEMP TABLE sum_win_meds AS
WITH sum_meds AS
(SELECT p.id AS person_id, COUNT(medal_id) AS summer_medals
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN games g ON gc.games_id = g.id
WHERE ce.medal_id <> 4 AND g.season = 'Summer'
GROUP BY p.id),
win_meds AS
(SELECT p.id AS person_id, COUNT(medal_id) AS winter_medals
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN games g ON gc.games_id = g.id
WHERE ce.medal_id <> 4 AND g.season = 'Winter'
GROUP BY p.id)
SELECT
p.id, p.full_name, sm.summer_medals, wm.winter_medals
FROM person p
JOIN sum_meds sm ON p.id = sm.person_id
JOIN win_meds wm ON p.id = wm.person_id

--To display the results:
SELECT * FROM sum_win_meds

--By the way, if we were looking for athletes who had won in at a minimum
--Summer or Winter olympics, the code would be as follows:

CREATE TEMP TABLE sum_win_meds AS
WITH sum_meds AS
(SELECT p.id AS person_id, COUNT(medal_id) AS summer_medals
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN games g ON gc.games_id = g.id
WHERE ce.medal_id <> 4 AND g.season = 'Summer'
GROUP BY p.id),
win_meds AS
(SELECT p.id AS person_id, COUNT(medal_id) AS winter_medals
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN games g ON gc.games_id = g.id
WHERE ce.medal_id <> 4 AND g.season = 'Winter'
GROUP BY p.id)
SELECT
p.id, p.full_name, sm.summer_medals, wm.winter_medals
FROM person p
LEFT JOIN sum_meds sm ON p.id = sm.person_id
LEFT JOIN win_meds wm ON p.id = wm.person_id
WHERE (sm.summer_medals IS NOT NULL) OR (wm.winter_medals IS NOT NULL)
--To display the results:
SELECT * FROM sum_win_meds

-- Task 2: Create a temporary table to store competitors who have won medals in exactly two different sports,
--and then use a subquery to identify the top 3 competitors with the highest total number of medals across all sports.
--Display the contents of this table.

--For now processing based on competitors, not individual persons
--strategy: Do joins and groups such that COUNT(DISTINCT e.sport_id) = 2 FROM event e
--Temp table will include competitor id, total medals
CREATE TEMP TABLE top_two_sport_comps AS
SELECT * FROM
(SELECT ce.competitor_id, COUNT(ce.medal_id) AS medals
FROM competitor_event ce
JOIN event e ON e.id = ce.event_id
WHERE ce.medal_id <> 4
GROUP BY ce.competitor_id
HAVING COUNT(DISTINCT e.sport_id) = 2
)
ORDER BY medals DESC
LIMIT 3;
SELECT * FROM top_two_sport_comps

--And if we want to perform this query on the person level across games:
CREATE TEMP TABLE top_two_sport_persons AS
SELECT * FROM
(SELECT p.id, COUNT(ce.medal_id) AS medals
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN event e ON e.id = ce.event_id
WHERE ce.medal_id <> 4
GROUP BY p.id
HAVING COUNT(DISTINCT e.sport_id) = 2
)
ORDER BY medals DESC
LIMIT 3;

-- 🌟 Exercise 2: Region and Competitor Performance

-- Task 1: Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event.
--Use a subquery to determine the event with the highest number of medals for each competitor,
--and then display the top 5 regions with the highest total medals.

--I believe that this has to mean a person across his career and not a separate competitor in each games separately,
--because one can only earn one medal per event per games. But let's explore.
--subquery to determine the event with the highest number of medals for each competitor:
--first determine each competitor, event, and number of medals earned.
--columns will be person_id or competitor_id, event, number of medals (count(medal_id))
--if each competitor separate:

SELECT ce.competitor_id, ce.event_id, count(ce.medal_id) AS medals
FROM competitor_event ce
WHERE ce.medal_id <> 4
GROUP BY ce.competitor_id, ce.event_id
HAVING count(ce.medal_id) > 1 --checking if possible to earn more than 1 medal
--only retrieves 20 rows. Only 20 competitors who received more than 1 medal in the same event in the same games, and they
--all received only 2 medals. This seems like too minimal a result for what the instructions request, so I assume it is
--referring to persons across olympics. so:
--a person's medals across events:
SELECT gc.person_id, ce.event_id, COUNT(ce.medal_id) as event_medals
        FROM games_competitor gc
        JOIN competitor_event ce ON gc.id = ce.competitor_id
        WHERE ce.medal_id <> 4
        GROUP BY gc.person_id, ce.event_id

--use subquery to determine the event with the highest number of medals for each competitor:
--subquery will be:
WITH EventTotals AS (
    -- Step 1: Get person, event, and count
    SELECT gc.person_id, ce.event_id, COUNT(ce.medal_id) AS event_medals
    FROM games_competitor gc
    JOIN competitor_event ce ON gc.id = ce.competitor_id
    WHERE ce.medal_id <> 4
    GROUP BY gc.person_id, ce.event_id
),
MaxMedalsPerPerson AS (
    -- Step 2: Find the highest medal count for each person
    SELECT person_id, MAX(event_medals) AS top_count
    FROM EventTotals
    GROUP BY person_id
)
-- Step 3: Join everything together, including region info
SELECT 
    et.person_id, 
    pr.region_id,
    nr.region_name,
    et.event_id, 
    et.event_medals
FROM EventTotals et
JOIN MaxMedalsPerPerson mmp 
    ON et.person_id = mmp.person_id 
    AND et.event_medals = mmp.top_count
JOIN person_region pr ON et.person_id = pr.person_id
JOIN noc_region nr ON pr.region_id = nr.id;

--MY SOLUTION: full query with the subquery inside, displaying the top 5 regions with the highest total medals:

WITH EventTotals AS (
    -- Step 1: Get person, event, and count
    SELECT gc.person_id, ce.event_id, COUNT(ce.medal_id) AS event_medals
    FROM games_competitor gc
    JOIN competitor_event ce ON gc.id = ce.competitor_id
    WHERE ce.medal_id <> 4
    GROUP BY gc.person_id, ce.event_id
),
MaxMedalsPerPerson AS (
    -- Step 2: Find the highest medal count for each person
    SELECT person_id, MAX(event_medals) AS top_count
    FROM EventTotals
    GROUP BY person_id
),
-- Step 3: Join everything together, including region info
MaxMedalsPerPersonRegion AS (SELECT 
    et.person_id, 
    pr.region_id,
    nr.region_name,
    et.event_id, 
    et.event_medals
FROM EventTotals et
JOIN MaxMedalsPerPerson mmp 
    ON et.person_id = mmp.person_id 
    AND et.event_medals = mmp.top_count
JOIN person_region pr ON et.person_id = pr.person_id
JOIN noc_region nr ON pr.region_id = nr.id)
SELECT region_id, region_name, max(event_medals) AS max_region_event_medals
FROM MaxMedalsPerPersonRegion
GROUP BY region_id, region_name
ORDER BY max(event_medals) DESC
LIMIT 5;

-- Task 2: Create a temporary table to store competitors who have participated in more than three Olympic Games
--but have not won any medals. Retrieve and display the contents of this table,
--including their full names and the number of games they participated in.

--In this case we are clearly looking for persons, not separate games competitors.
--We want all the medal_ids to be 4, so the minimum medal id to be 4
CREATE TEMP TABLE multi_nonmedalists AS
SELECT p.id, p.full_name, count(distinct gc.games_id) AS total_games
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
GROUP BY p.id, p.full_name
HAVING count(distinct gc.games_id) > 3 AND MIN(ce.medal_id)=4;

select * from multi_nonmedalists