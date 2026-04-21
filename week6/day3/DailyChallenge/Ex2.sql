-- Part II:

--1     Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL
CREATE TABLE Book (
book_id SERIAL PRIMARY KEY,
title VARCHAR(50) NOT NULL,
author VARCHAR(50) NOT NULL
)
--2     Insert those books :
--         Alice In Wonderland, Lewis Carroll
--         Harry Potter, J.K Rowling
--         To kill a mockingbird, Harper Lee
INSERT INTO Book (title, author) VALUES
		('Alice In Wonderland', 'Lewis Carroll'),
        ('Harry Potter', 'J.K Rowling'),
        ('To kill a mockingbird', 'Harper Lee')
--3     Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age.
--Make sure that the age is never bigger than 15 (Find an SQL method);
CREATE TABLE student (
student_id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL UNIQUE,
age INT CHECK (age <=15)
)
--4     Insert those students:
--         John, 12
--         Lera, 11
--         Patrick, 10
--         Bob, 14
INSERT INTO student (name, age) VALUES
        ('John', 12),
        ('Lera', 11),
        ('Patrick', 10),
        ('Bob', 14) 	
--5     Create a table named Library, with the columns :
--         book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
--         student_id ON DELETE CASCADE ON UPDATE CASCADE
--         borrowed_date
--         This table, is a junction table for a Many to Many relationship with the Book and Student tables :
--			A student can borrow many books, and a book can be borrowed by many children
--         book_fk_id is a Foreign Key representing the column book_id from the Book table
--         student_fk_id is a Foreign Key representing the column student_id from the Student table
--         The pair of Foreign Keys is the Primary Key of the Junction Table
CREATE TABLE library (
        book_fk_id INT REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
        student_fk_id INT REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
        borrowed_date DATE)

--6     Add 4 records in the junction table, use subqueries.
--         the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
--         the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
--         the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
--         the student named Bob, borrowed the book Harry Potter the on 12/08/2021
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date) VALUES
	((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),(SELECT student_id FROM student WHERE name = 'John'),
	'2022-02-15'),
	((SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),(SELECT student_id FROM student WHERE name = 'Bob'),
	'2021-03-03'),
	((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),(SELECT student_id FROM student WHERE name = 'Lera'),
	'2021-05-23'),
	((SELECT book_id FROM book WHERE title = 'Harry Potter'),(SELECT student_id FROM student WHERE name = 'Bob'),
	'2021-08-12')
	
--7     Display the data
--         Select all the columns from the junction table
SELECT * FROM library
--         Select the name of the student and the title of the borrowed books
SELECT s.name, b.title
FROM library l
JOIN book b ON l.book_fk_id = b.book_id
JOIN student s ON l.student_fk_id = s.student_id
--         Select the average age of the children, that borrowed the book Alice in Wonderland
SELECT AVG(s.age)
FROM library l
JOIN book b ON l.book_fk_id = b.book_id
JOIN student s ON l.student_fk_id = s.student_id
WHERE b.title = 'Alice in Wonderland' 
---This query returns null. Why? Because the title was written incorrectly. Here is it corrected:
SELECT AVG(s.age)
FROM library l
JOIN book b ON l.book_fk_id = b.book_id
JOIN student s ON l.student_fk_id = s.student_id
WHERE b.title = 'Alice In Wonderland' 
--         Delete a student from the Student table, what happened in the junction table ?
DELETE FROM student WHERE student_id = 1

SELECT * FROM library

--All rows connected to that student were deleted too, because of the CASCADE rule.
