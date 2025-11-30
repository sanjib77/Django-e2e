# Day 10: SQL Essentials 🗃️

## Quick Recap from Day 9 (2 minutes)
Yesterday we covered Git Version Control:
- Git basics: init, add, commit, push, pull
- Branching and merging
- GitHub workflow
- .gitignore usage

Today we dive into **SQL** - the language that powers every database!

---

## Today's Learning Objectives 🎯
By the end of today, you will be able to:
1. Understand what databases are and why we need them
2. Write basic CRUD operations (SELECT, INSERT, UPDATE, DELETE)
3. Filter and sort data with WHERE, ORDER BY, LIMIT
4. Join tables together with INNER JOIN and LEFT JOIN
5. Write practical SQL queries for real-world scenarios

---

## 1. Database Basics (10 minutes) 📊

### What is a Database?
A **database** is an organized collection of structured data stored electronically. Think of it like a super-powered Excel spreadsheet!

### Relational Databases
In relational databases, data is stored in **tables** (also called relations):

```
USERS TABLE
+----+----------+----------------------+-----+
| id | name     | email                | age |
+----+----------+----------------------+-----+
| 1  | Alice    | alice@email.com      | 25  |
| 2  | Bob      | bob@email.com        | 30  |
| 3  | Charlie  | charlie@email.com    | 28  |
+----+----------+----------------------+-----+
```

### Key Concepts
- **Table**: A collection of related data (like a spreadsheet)
- **Row/Record**: A single entry in the table
- **Column/Field**: A specific attribute (name, email, age)
- **Primary Key**: Unique identifier for each row (usually `id`)
- **Foreign Key**: Links to another table's primary key

### Popular SQL Databases
| Database   | Best For                    |
|------------|----------------------------|
| SQLite     | Learning, small apps       |
| PostgreSQL | Production, complex apps   |
| MySQL      | Web applications           |
| SQL Server | Enterprise applications    |

---

## 2. SELECT - Reading Data (15 minutes) 📖

The `SELECT` statement retrieves data from tables.

### Basic Syntax
```sql
SELECT column1, column2 FROM table_name;
```

### Examples

**Select all columns:**
```sql
SELECT * FROM users;
```

**Select specific columns:**
```sql
SELECT name, email FROM users;
```

**Select with alias:**
```sql
SELECT name AS user_name, email AS user_email FROM users;
```

### Pro Tip 💡
Avoid `SELECT *` in production code - it's slower and returns unnecessary data. Always specify the columns you need!

---

## 3. INSERT - Creating Data (10 minutes) ➕

The `INSERT` statement adds new records to a table.

### Basic Syntax
```sql
INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);
```

### Examples

**Insert a single row:**
```sql
INSERT INTO users (name, email, age)
VALUES ('Diana', 'diana@email.com', 26);
```

**Insert multiple rows:**
```sql
INSERT INTO users (name, email, age)
VALUES 
    ('Eve', 'eve@email.com', 24),
    ('Frank', 'frank@email.com', 32),
    ('Grace', 'grace@email.com', 29);
```

### Pro Tip 💡
Always specify column names explicitly - it makes your code more readable and protects against table structure changes!

---

## 4. UPDATE - Modifying Data (10 minutes) ✏️

The `UPDATE` statement modifies existing records.

### Basic Syntax
```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

### Examples

**Update a single record:**
```sql
UPDATE users
SET email = 'newalice@email.com'
WHERE id = 1;
```

**Update multiple columns:**
```sql
UPDATE users
SET name = 'Alice Smith', age = 26
WHERE id = 1;
```

**Update multiple records:**
```sql
UPDATE users
SET age = age + 1
WHERE age < 30;
```

### ⚠️ CRITICAL WARNING
**ALWAYS use WHERE clause with UPDATE!** Without it, you'll update ALL records:
```sql
-- DANGEROUS! Updates everyone!
UPDATE users SET age = 25;

-- SAFE! Only updates user with id = 1
UPDATE users SET age = 25 WHERE id = 1;
```

---

## 5. DELETE - Removing Data (5 minutes) ❌

The `DELETE` statement removes records from a table.

### Basic Syntax
```sql
DELETE FROM table_name WHERE condition;
```

### Examples

**Delete a specific record:**
```sql
DELETE FROM users WHERE id = 3;
```

**Delete multiple records:**
```sql
DELETE FROM users WHERE age > 40;
```

### ⚠️ CRITICAL WARNING
**ALWAYS use WHERE clause with DELETE!**
```sql
-- DANGEROUS! Deletes ALL users!
DELETE FROM users;

-- SAFE! Only deletes specific user
DELETE FROM users WHERE id = 3;
```

---

## 6. WHERE - Filtering Data (10 minutes) 🔍

The `WHERE` clause filters records based on conditions.

### Comparison Operators
| Operator | Description              |
|----------|--------------------------|
| =        | Equal to                 |
| <>  or != | Not equal to            |
| >        | Greater than             |
| <        | Less than                |
| >=       | Greater than or equal    |
| <=       | Less than or equal       |

### Examples

**Basic comparison:**
```sql
SELECT * FROM users WHERE age > 25;
SELECT * FROM users WHERE name = 'Alice';
SELECT * FROM users WHERE age != 30;
```

### Logical Operators (AND, OR, NOT)

**Using AND:**
```sql
SELECT * FROM users 
WHERE age > 25 AND name = 'Bob';
```

**Using OR:**
```sql
SELECT * FROM users 
WHERE age < 25 OR age > 35;
```

**Using NOT:**
```sql
SELECT * FROM users 
WHERE NOT age = 30;
```

### Special Operators

**BETWEEN:**
```sql
SELECT * FROM users WHERE age BETWEEN 25 AND 30;
```

**IN:**
```sql
SELECT * FROM users WHERE name IN ('Alice', 'Bob', 'Charlie');
```

**LIKE (pattern matching):**
```sql
-- Names starting with 'A'
SELECT * FROM users WHERE name LIKE 'A%';

-- Names ending with 'e'
SELECT * FROM users WHERE name LIKE '%e';

-- Names containing 'li'
SELECT * FROM users WHERE name LIKE '%li%';
```

**IS NULL / IS NOT NULL:**
```sql
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;
```

---

## 7. ORDER BY - Sorting Data (5 minutes) 📊

The `ORDER BY` clause sorts the result set.

### Basic Syntax
```sql
SELECT * FROM table_name ORDER BY column_name ASC|DESC;
```

### Examples

**Ascending order (default):**
```sql
SELECT * FROM users ORDER BY age;
SELECT * FROM users ORDER BY name ASC;
```

**Descending order:**
```sql
SELECT * FROM users ORDER BY age DESC;
```

**Multiple columns:**
```sql
SELECT * FROM users ORDER BY age DESC, name ASC;
```

---

## 8. LIMIT - Restricting Results (5 minutes) 🔢

The `LIMIT` clause restricts the number of records returned.

### Basic Syntax
```sql
SELECT * FROM table_name LIMIT number;
```

### Examples

**Get first 5 records:**
```sql
SELECT * FROM users LIMIT 5;
```

**Pagination with OFFSET:**
```sql
-- Get records 6-10 (skip first 5)
SELECT * FROM users LIMIT 5 OFFSET 5;
```

**Combined with ORDER BY:**
```sql
-- Get top 3 oldest users
SELECT * FROM users ORDER BY age DESC LIMIT 3;
```

---

## 9. JOINs - Combining Tables (15 minutes) 🔗

JOINs combine rows from two or more tables based on a related column.

### Sample Tables for Examples

**USERS table:**
```
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 2  | Bob      |
| 3  | Charlie  |
+----+----------+
```

**ORDERS table:**
```
+----+---------+------------+--------+
| id | user_id | product    | amount |
+----+---------+------------+--------+
| 1  | 1       | Laptop     | 1200   |
| 2  | 1       | Mouse      | 25     |
| 3  | 2       | Keyboard   | 75     |
| 4  | 4       | Monitor    | 300    |
+----+---------+------------+--------+
```

### INNER JOIN
Returns records that have matching values in **both** tables.

```sql
SELECT users.name, orders.product, orders.amount
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

**Result:**
```
+-------+----------+--------+
| name  | product  | amount |
+-------+----------+--------+
| Alice | Laptop   | 1200   |
| Alice | Mouse    | 25     |
| Bob   | Keyboard | 75     |
+-------+----------+--------+
```
Note: Charlie is not included (no orders), and the Monitor order is not included (user_id 4 doesn't exist).

### LEFT JOIN (LEFT OUTER JOIN)
Returns **all** records from the left table, and matched records from the right table. Returns NULL for non-matching right side.

```sql
SELECT users.name, orders.product, orders.amount
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

**Result:**
```
+---------+----------+--------+
| name    | product  | amount |
+---------+----------+--------+
| Alice   | Laptop   | 1200   |
| Alice   | Mouse    | 25     |
| Bob     | Keyboard | 75     |
| Charlie | NULL     | NULL   |
+---------+----------+--------+
```
Note: Charlie is now included with NULL values for order fields.

### Visual Representation

```
INNER JOIN:      LEFT JOIN:
    ┌───┐           ┌───┐
  ┌─┼───┼─┐       ┌─────┐
  │ │███│ │       │█████│
  │ │███│ │       │█████│ 
  └─┼───┼─┘       └─────┘
    └───┘           
  A   B           A   B
  
Returns only     Returns all A,
matching         matching B
records          (or NULL)
```

### Table Aliases
Make your queries more readable:

```sql
SELECT u.name, o.product, o.amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

### Multiple JOINs
```sql
SELECT u.name, o.product, c.category_name
FROM users u
INNER JOIN orders o ON u.id = o.user_id
INNER JOIN categories c ON o.category_id = c.id;
```

---

## Summary Cheat Sheet 📝

```sql
-- SELECT: Read data
SELECT column1, column2 FROM table_name;
SELECT * FROM table_name WHERE condition;

-- INSERT: Create data
INSERT INTO table_name (col1, col2) VALUES (val1, val2);

-- UPDATE: Modify data
UPDATE table_name SET col1 = val1 WHERE condition;

-- DELETE: Remove data
DELETE FROM table_name WHERE condition;

-- Filter, Sort, Limit
SELECT * FROM table_name 
WHERE condition 
ORDER BY column DESC 
LIMIT 10;

-- JOINs
SELECT * FROM table1 
INNER JOIN table2 ON table1.id = table2.foreign_id;

SELECT * FROM table1 
LEFT JOIN table2 ON table1.id = table2.foreign_id;
```

---

## What's Next? 🚀

Tomorrow (Day 11), we'll start **Django Part 1 - Setup & Basics**:
- Django installation and project structure
- Creating apps
- URL routing
- Views (function-based)
- Templates basics
- Quick project: Hello World Django app

Great job completing SQL Essentials! 🎉

Now head over to `Day10_Practice.md` to write 10 SQL queries and then take your daily test in `Day10_Test.md`!
