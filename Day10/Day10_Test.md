# Day 10: Daily Test - SQL Essentials 📝

## Test Instructions
- **Total Questions:** 10
- **Total Points:** 14
- **Time Limit:** 15 minutes
- **Passing Score:** 70% (10 points)
- Answer all questions without looking at notes first!

---

## Section A: Multiple Choice & True/False (6 questions, 1 point each)

### Question 1 (MCQ - 1 point)
Which SQL statement is used to extract data from a database?

A) GET  
B) SELECT  
C) EXTRACT  
D) PULL

**Your Answer:** ___

---

### Question 2 (MCQ - 1 point)
What does the following SQL query return?
```sql
SELECT * FROM users WHERE age BETWEEN 20 AND 30;
```

A) Users with age exactly 20 or 30  
B) Users with age greater than 20 and less than 30  
C) Users with age 20 to 30, inclusive  
D) Users with age less than 20 or greater than 30

**Your Answer:** ___

---

### Question 3 (True/False - 1 point)
**Statement:** An INNER JOIN returns all records from the left table, even if there are no matches in the right table.

A) True  
B) False

**Your Answer:** ___

---

### Question 4 (MCQ - 1 point)
Which SQL clause is used to filter records based on a condition?

A) FILTER  
B) WHERE  
C) HAVING  
D) CONDITION

**Your Answer:** ___

---

### Question 5 (True/False - 1 point)
**Statement:** Running `DELETE FROM users;` without a WHERE clause will delete ALL records in the users table.

A) True  
B) False

**Your Answer:** ___

---

### Question 6 (MCQ - 1 point)
What is the correct syntax to add a new record to a table?

A) `ADD INTO users VALUES (...)`  
B) `INSERT INTO users VALUES (...)`  
C) `CREATE INTO users VALUES (...)`  
D) `PUT INTO users VALUES (...)`

**Your Answer:** ___

---

## Section B: Short Coding Challenges (3 questions, 2 points each)

### Question 7 (Coding - 2 points)
Write a SQL query to select all columns from a table called `products` where the `price` is greater than 100, ordered by `price` from highest to lowest.

```sql
-- Your answer here:

```

---

### Question 8 (Coding - 2 points)
Write a SQL query to update the `status` column to 'inactive' for all records in the `users` table where `last_login` is NULL.

```sql
-- Your answer here:

```

---

### Question 9 (Coding - 2 points)
Write a SQL query using LEFT JOIN to get all customers and their orders. The `customers` table has `id` and `name`. The `orders` table has `id`, `customer_id`, and `total`. Show customer name and order total.

```sql
-- Your answer here:

```

---

## Section C: Conceptual Question (1 question, 2 points)

### Question 10 (Concept - 2 points)
Explain the difference between INNER JOIN and LEFT JOIN in 2-3 sentences. When would you use each one?

**Your Answer:**
```
Write your explanation here...


```

---

## Answer Key 🔑

<details>
<summary>Click to reveal answers (only after completing the test!)</summary>

### Section A Answers:

**Q1: B) SELECT**
- SELECT is the SQL statement used to retrieve data from a database.

**Q2: C) Users with age 20 to 30, inclusive**
- BETWEEN includes both boundary values (20 and 30).

**Q3: B) False**
- INNER JOIN returns only records that have matching values in BOTH tables. LEFT JOIN returns all records from the left table.

**Q4: B) WHERE**
- WHERE clause is used to filter records based on a condition.

**Q5: A) True**
- DELETE without WHERE clause will delete ALL records. Always use WHERE with DELETE!

**Q6: B) INSERT INTO users VALUES (...)**
- INSERT INTO is the correct SQL syntax for adding new records.

### Section B Answers:

**Q7:**
```sql
SELECT * FROM products 
WHERE price > 100 
ORDER BY price DESC;
```
- 1 point for correct WHERE clause
- 1 point for correct ORDER BY DESC

**Q8:**
```sql
UPDATE users 
SET status = 'inactive' 
WHERE last_login IS NULL;
```
- 1 point for correct UPDATE/SET syntax
- 1 point for correct IS NULL condition

**Q9:**
```sql
SELECT c.name, o.total
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id;
```
- 1 point for LEFT JOIN syntax
- 1 point for correct ON condition

### Section C Answer:

**Q10:** (2 points for a complete answer)

Sample Answer:
"INNER JOIN returns only the records that have matching values in both tables, essentially showing the intersection. LEFT JOIN returns all records from the left table and matched records from the right table; if there's no match, it shows NULL for the right table columns. 

Use INNER JOIN when you only want records that exist in both tables (e.g., users WITH orders). Use LEFT JOIN when you want all records from the left table regardless of matches (e.g., all users, even those without orders)."

</details>

---

## Scoring

| Section | Points | Your Score |
|---------|--------|------------|
| A (Q1-6) | 6 | ___ / 6 |
| B (Q7-9) | 6 | ___ / 6 |
| C (Q10) | 2 | ___ / 2 |
| **Total** | **14** | ___ / 14 |

**Passing Score: 10/14 (70%)**

---

## Results

- ✅ **10+ points**: Congratulations! You passed! Move on to Day 11!
- ❌ **Below 10 points**: Review the concepts you missed and retake the test tomorrow morning.

---

## Next Steps

**If you passed:**
🎉 Great job! You now have SQL fundamentals down! Tomorrow we start **Day 11: Django Part 1 - Setup & Basics**!

**If you need to review:**
📚 Go back to `Day10_SQL_Essentials.md` and focus on:
- Questions 1-6 wrong: Review basic syntax
- Question 7 wrong: Practice SELECT with WHERE and ORDER BY
- Question 8 wrong: Practice UPDATE statements
- Question 9 wrong: Review JOINs section
- Question 10 wrong: Re-read the JOINs explanation
