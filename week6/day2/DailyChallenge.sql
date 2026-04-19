-- DailyChallenge
-- Questions

-- Q1. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
--My guess: COUNT
--			1
--Guess was correct
Q2. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
--My guess:
--COUNT
--3
--Guess was wrong. I assume this is because instances of NULL are not counted.
--Testing this:
SELECT COUNT(1) FROM FirstTab WHERE id <> 6 -- ALSO returns 2.

Q3. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
--My guess: (count rows in first tab where id is not 5, NULL)
--COUNT
--2
--Guess was wrong. Answer is 0! Consulting with Gemini explained that this is because NOT IN (5, NULL) translates to
--id != 5 AND id != NULL, and id != NULL is always Unknown, so the whole condition becomes Unknown,
--andd the entire table vanishes, leading to a count of 0.

Q4. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
--My guess: (count rows in FirstTab where id is not 5: 6, 7, Unknown (unknown whether NULL is not 5), so 2
--COUNT
--2
--Now having learned this idea, I was right.
