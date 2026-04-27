--Daily Challenge

--     Identify and handle any missing value.

SELECT * FROM employees
WHERE employee_id IS NULL
OR employee_name IS NULL OR employee_name = ''
OR salary IS NULL
OR hire_date IS NULL OR hire_date = ''
OR department IS NULL OR department = ''
--Query reveals one row with department NULL. The rest of the data is useful so rather than delete the row
--I will enter 'Unknown' for the department.
UPDATE employees
SET department = 'Unknown'
WHERE department IS NULL;
COMMIT
--     Check for and eliminate any duplicate rows in the dataset.
SELECT employee_id, employee_name, salary, hire_date, COUNT(*)
FROM employees
GROUP BY employee_id, employee_name, salary, hire_date
HAVING COUNT(*) > 1;
--Conclusion: No duplicate rows.

--     Correct any structural issues, such as inconsistent naming conventions or formatting errors.
UPDATE employees
SET employee_name = INITCAP(employee_name);
COMMIT
--     Ensure all columns have appropriate data types (e.g. the hire_date column).
ALTER TABLE employees 
ALTER COLUMN hire_date TYPE DATE 
USING hire_date::DATE;
COMMIT
--     Detect and address any outliers that may skew the analysis.
WITH Stats AS (
    SELECT 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salary) AS q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salary) AS q3
    FROM employees
),
Bounds AS (
    SELECT 
        q1, 
        q3, 
        (q3 - q1) AS iqr,
        (q1 - 1.5 * (q3 - q1)) AS lower_bound,
        (q3 + 1.5 * (q3 - q1)) AS upper_bound
    FROM Stats
)
SELECT e.*
FROM employees e, Bounds b
WHERE e.salary > b.upper_bound OR e.salary < b.lower_bound;
--No outliers on salary

WITH DateIntervals AS (
    -- Convert date to "days since 1900" to make it a number
    SELECT *, 
           (hire_date - '1900-01-01'::date) as date_val
    FROM employees
),
Stats AS (
    SELECT 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY date_val) AS q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY date_val) AS q3
    FROM DateIntervals
),
Bounds AS (
    SELECT 
        q1, q3,
        (q1 - 1.5 * (q3 - q1)) AS lower_bound,
        (q3 + 1.5 * (q3 - q1)) AS upper_bound
    FROM Stats
)
SELECT e.*
FROM employees e, Bounds b
WHERE (e.hire_date - '1900-01-01'::date) < b.lower_bound
   OR (e.hire_date - '1900-01-01'::date) > b.upper_bound;
--No outliers on hire_date.

--     Standardize and normalize data where applicable to ensure consistency.

--The data appears standard already. To confirm:
SELECT * FROM employees 
WHERE employee_name <> INITCAP(employee_name)
--returns nothing, good

select DISTINCT department from employees
--No inconsistencies, good

--Normalization involves organizing data to minimize redundancy.
--This is achieved by splitting data into multiple related tables.
CREATE TABLE employee AS
SELECT employee_id, employee_name
FROM employees;

CREATE TABLE employee_info AS
SELECT employee_id, salary, hire_date, department
FROM employees;
COMMIT
--Normalization could go further here to create separate tables for salary and department (with a separate
--department table matching department codes to names and only using codes elsewhere) but that seems pretty irrelevant
--here, so this seems like enough for now.