--🌟 Exercise 1: Building a Comprehensive Dataset for Employee Analysis
--
--1    Create a temporary table that join all tables and create a new one using LEFT JOIN.
--2    Create an unique identifier code between the columns ‘employee_id’ and ‘date’ and call it ‘id’.
--3    Convert the column ‘date’ to DATE type because it was previously configured as TIMESTAMP.
--4    Transform this new table into a dataset “df_employee” for analysis.
CREATE TEMPORARY TABLE emp_dataset AS
SELECT
c.company_name, c.company_city, c.company_state, c.company_type, c.const_site_category,
s.comp_code, s.employee_id, s.employee_name, DATE(s.date) AS date, s.func_code, s.func, s.salary,
f.function_group,
e."GEN(M_F)" AS gender, e.age

FROM companies c
LEFT JOIN salaries s ON company_name = s.comp_name
LEFT JOIN functions f ON s.func_code = f.function_code
LEFT JOIN employees e ON s.employee_id = e.employee_code_emp

--Hint :
--
--CREATE TABLE df_employee AS
--SELECT 
--    employee_id || '_' || CAST(date AS TEXT) AS id,  -- Use || for concatenation and CAST date to TEXT
--    DATE(date) AS month_year,  -- Use DATE() function to cast the timestamp to a DATE format
--    employee_id, 
--    ..., 
--    `...` AS gender,  
--    ...,
--    ...,
--    ..., 
--    ..., 
--    ..., 
--    ..., 
--    ..., 
--    ...
--FROM emp_dataset;
--
--
--You should get a new df-employee table with the following columns :id, month_year, employee_id, employee_name, gender,
--age, salary, function_group, company_name, company_city, company_state,
--company_type, and const_site_category.
CREATE TABLE df_employee AS
SELECT 
    employee_id || '_' || CAST(date AS TEXT) AS id,  -- Use || for concatenation and CAST date to TEXT
    DATE(date) AS month_year,  -- Use DATE() function to cast the timestamp to a DATE format
    employee_id, 
    employee_name, 
    gender AS gender,
    age, salary, function_group, company_name, company_city, company_state,
company_type, const_site_category
FROM emp_dataset;
COMMIT
--
--
--🌟 Exercise 2: Cleaning Data for Consistency and Quality


--1. run the following SQLite request and observe your new table.
--
SELECT * FROM df_employee;
--
--
--2. Remove all unwanted spaces from all text columns using TRIM
--
--Hint :
--
--UPDATE df_employee
--SET
--id = TRIM(id),
--...
--...;
--
UPDATE df_employee
SET
id = TRIM(id),
employee_name = TRIM(employee_name), 
gender = TRIM(gender),
salary = TRIM(salary),
function_group = TRIM(function_group),
company_name = TRIM(company_name),
company_city = TRIM(company_city),
company_state = TRIM(company_state),
company_type = TRIM(company_type),
const_site_category = TRIM(const_site_category)


--3. Check for NULL values and empty values.
--
--SELECT *
--FROM df_employee
--WHERE id IS NULL
--OR month_year IS NULL
--OR employee_id IS NULL
--...
SELECT *
FROM df_employee
WHERE id IS NULL
OR month_year IS NULL
OR employee_id IS NULL
OR employee_name IS NULL
OR gender IS NULL
OR age IS NULL
OR salary IS NULL
OR function_group IS NULL
OR company_name IS NULL
OR company_city IS NULL
OR company_state IS NULL
OR company_type IS NULL
OR const_site_category IS NULL

OR id = ''
--OR month_year = ''
--OR employee_id = ''
OR employee_name = ''
OR gender = ''
--OR age = ''
OR salary = ''
OR function_group = ''
OR company_name = ''
OR company_city = ''
OR company_state = ''
OR company_type = ''
OR const_site_category = ''
--I commented out non-text columns, which can't be empty.
--Results: One line with many null values. And several lines with almost all information except const_site_category
--is empty but not null. I won't delete those rows because it is a lot of rows and they have valid information for all
--other columns.

--4. Delete rows of the detected missing values.
--
--Hint :
--
--DELETE FROM df_employee
--WHERE salary = ' '
--;
--
--
DELETE FROM df_employee
WHERE employee_id IS NULL;

COMMIT
--🌟 Exercise 3 : Calculating Current Employee Counts by Company
--
--    How many employees do the companies have today?
SELECT
COUNT (DISTINCT employee_id)
FROM df_employee
--ANSWER: SELECT
COUNT (DISTINCT employee_id)
FROM df_employee
--ANSWER: 1156
--    Group them by company
SELECT
company_name, COUNT (DISTINCT employee_id)
FROM df_employee
GROUP BY company_name
--
--🌟 Exercise 4 : Analyzing Employee Distribution by City and Over Time
--
--    What is the total number of employees each city? Add a percentage column
SELECT company_city, COUNT(DISTINCT employee_id),
ROUND(100*COUNT(DISTINCT employee_id) / (SELECT COUNT(DISTINCT employee_id) FROM df_employee) ::numeric,2)  AS percentage
FROM df_employee
GROUP BY company_city
--    What is the total number of employees each month?
SELECT DATE(DATE_TRUNC('month', month_year)) AS month, COUNT(DISTINCT employee_id) AS monthly_employees
FROM df_employee
GROUP BY DATE(DATE_TRUNC('month', month_year)) 
--This seems unbalanced. I notice that all the dates have YYYY-01-XX. I believe the 01 here is the DD, not the MM.
--Let's fix this:
UPDATE df_employee
SET month_year = TO_DATE(TO_CHAR(month_year, 'YYYY-DD-MM'), 'YYYY-MM-DD')
WHERE month_year IS NOT NULL;
COMMIT

--Now trying again:
SELECT DATE(DATE_TRUNC('month', month_year)) AS month, COUNT(DISTINCT employee_id) AS monthly_employees
FROM df_employee
GROUP BY DATE(DATE_TRUNC('month', month_year)) 
--That looks better.
--    What is the average number of employees each month?
-- I assume this means the average among the totals per month retrieved above.
WITH month_employees AS (
SELECT DATE(DATE_TRUNC('month', month_year)) AS month, COUNT(DISTINCT employee_id) AS monthly_employees
FROM df_employee
GROUP BY DATE(DATE_TRUNC('month', month_year)) 
)
SELECT ROUND(AVG(monthly_employees),2) FROM month_employees
--
--🌟 Exercise 5 : Analyzing Employment Trends and Salary Metrics
--
--    What is the minimum and maximum number of employees throughout all the months? In which months were they?
CREATE TEMP TABLE month_employees AS
SELECT DATE(DATE_TRUNC('month', month_year)) AS month, COUNT(DISTINCT employee_id) AS monthly_employees
FROM df_employee
GROUP BY DATE(DATE_TRUNC('month', month_year)) 

--A table showing the months with the min and max number of employees:
WITH max_min AS 
(SELECT MAX(monthly_employees), MIN(monthly_employees) FROM month_employees
)
SELECT month, monthly_employees from month_employees
WHERE monthly_employees = (SELECT max FROM max_min) OR monthly_employees = (SELECT min FROM max_min)
--    What is the monthly average number of employees by function group?
WITH group_employees AS (
SELECT function_group, COUNT(DISTINCT employee_id) AS employees
FROM df_employee
GROUP BY function_group)
SELECT avg(employees) AS avg_employees_per_fn_group
FROM group_employees 

--    What is the annual average salary?
--We need to format the salary column correctly because it appears as text with commas.
--The data seems to be from Brazil and the commas generally appear before two numbers,
--so I think the salary data is formatted in European or South American format
--where the comma is equivalent to a decimal point.
ALTER TABLE df_employee 
ALTER COLUMN salary TYPE DECIMAL(15,2) 
USING (REPLACE(NULLIF(salary, ''), ',', '.')::DECIMAL(15,2));
COMMIT;

SELECT month_year, salary, employee_name FROM df_employee
ORDER BY employee_name, month_year
--Now we can find the annual average salary (which I assume means the average salary for each year):
--It appears that the salary column is showing the monthly salary paid.
--So to find the annual average salary:
--A simple calculation to find the average monthly salary multiplied by 12 to get an average annual salary:
SELECT 
    ROUND(AVG(salary * 12),2) AS avg_annual_salary
FROM df_employee;

--To calculate each employee's avg monthly salary separately and then calculate the avg employee's average annual salary:
WITH emp_avg_salaries AS (
SELECT employee_name, ROUND(AVG(salary * 12),2) as avg_annual_salary
FROM df_employee
GROUP BY employee_name)
SELECT ROUND(avg(avg_annual_salary),2) FROM emp_avg_salaries