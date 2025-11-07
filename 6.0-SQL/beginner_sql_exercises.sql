CREATE DATABASE IF NOT EXISTS sql_bijles;
USE sql_bijles;
CREATE TABLE students (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(45) NOT NULL,
    `last_name` VARCHAR(45) NOT NULL,
    `email` VARCHAR(45) UNIQUE,
    `age` INTEGER
);

CREATE TABLE instructors (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    department VARCHAR(45)
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(45) NOT NULL,
    credits INTEGER NOT NULL,
    instructor_id INTEGER,
    FOREIGN KEY (instructor_id) REFERENCES instructors(id)
);

CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    grade INTEGER, -- 0-100 scale for simplicity
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- ========== Sample Data ==========
-- Instructors
INSERT INTO instructors (name, department) VALUES
  ('Dr. Anna Visser', 'Computer Science'),
  ('Mr. J. de Vries', 'Mathematics'),
  ('Ms. Lotte Peters', 'Physics');

-- Courses
INSERT INTO courses (title, credits, instructor_id) VALUES
  ('Intro to Programming', 6, 1),
  ('Calculus I', 5, 2),
  ('Physics Basics', 4, 3),
  ('Data Structures', 6, 1);

-- Students
INSERT INTO students (first_name, last_name, email, age) VALUES
  ('Sanne', 'Jansen', 'sanne.j@example.com', 19),
  ('Kees', 'Bakker', 'kees.b@example.com', 22),
  ('Miriam', 'de Jong', 'miriam.j@example.com', 21),
  ('Timo', 'Visser', 'timo.v@example.com', 20),
  ('Noah', 'Smit', 'noah.s@example.com', 18),
  ('Lies', 'Willems', 'lies.w@example.com', 23),
  ('Ravi', 'Kumar', 'ravi.k@example.com', 20),
  ('Aisha', 'Ali', 'aisha.a@example.com', 22);

-- Enrollments (student -> course with a grade)
INSERT INTO enrollments (student_id, course_id, grade) VALUES
  (1, 1, 88), -- Sanne - Intro to Programming
  (2, 1, 76), -- Kees
  (3, 2, 92), -- Miriam - Calculus I
  (4, 3, 81), -- Timo - Physics Basics
  (5, 1, 69), -- Noah
  (6, 4, 95), -- Lies - Data Structures
  (7, 4, 84), -- Ravi
  (8, 2, 73), -- Aisha - Calculus I
  (1, 4, 91), -- Sanne also takes Data Structures
  (3, 1, 85); -- Miriam also takes Intro to Programming

-- ========== Beginner Exercises ==========
-- Instructions: Load this file into SQLite (or another RDBMS with small tweaks).
-- Then attempt the queries below. Try to write each query before looking at hints.

-- 1) Select all columns for all students.
-- Expected: 8 rows from the students table.
-- 2) Select the first and last name of students who are older than 20.
-- Expected: rows for Kees (22), Lies (23), Aisha (22), Miriam (21).

-- 3) Select distinct ages that appear in the students table (no duplicates).
-- Expected: a short list of ages like 18,19,20,21,22,23 (order may vary).

-- 4) Create a result column called full_name that concatenates first and last name.
-- SQLite hint: use first_name || ' ' || last_name AS full_name
-- Expected: a column with values like 'Sanne Jansen'.

-- 5) Select all students ordered by last name ascending.
-- Expected: students sorted alphabetically by last_name.

-- 6) Count how many students are in the table.
-- Expected: 8

-- 7) What is the average age of students? (use AVG)
-- Expected: a single numeric value (may be fractional).

-- 8) For each course, count how many students are enrolled (show course title and count).
-- Hint: join courses and enrollments and use GROUP BY courses.id
-- Expected: rows with course titles and student counts.

-- 9) List student full name, course title and grade for every enrollment (order by student last name).
-- Hint: join students, enrollments and courses.
-- Expected: multiple rows showing which student took which course and the grade.

-- 10) Which students scored above 85 in any course? Show their name, course, and grade.
-- Expected: rows for Miriam, Lies, Sanne, and possibly others depending on sample data.

-- 11) Insert a new student (your own name) and then select them back.
-- Hint: INSERT INTO students (first_name, last_name, email, age) VALUES (...);

-- 12) Update a grade: set Noah's grade in Intro to Programming (student_id=5, course_id=1) to 75.
-- Hint: use UPDATE ... WHERE student_id = 5 AND course_id = 1;

-- 13) Delete a student you just inserted (undo the insert from #11) using DELETE.
-- Hint: DELETE FROM students WHERE id = <the id> OR email = '...';

-- 14) (Beginner JOIN practice) Show each course title with the instructor name.
-- Hint: join courses and instructors on instructor_id.
