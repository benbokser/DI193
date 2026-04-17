--Daily Challenge
--1. Count how many actors are in the table.
SELECT COUNT(*)
FROM ACTORS


--2. Try to add a new actor with some blank fields. What do you think the outcome will be ?
--If they are completely empty, I think the outcome will be an error,
-- because all the columns are set as NOT NULL.
--But if they are simply blank, they will be successfully written as blank.
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Jack','','','');