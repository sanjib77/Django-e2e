# Day 10: SQL Practice - Write 10 SQL Queries 📝

## Instructions
Practice your SQL skills by completing these 10 exercises. Each exercise builds on the concepts from today's lesson.

---

## Sample Database Schema

Use these tables for your practice:

### EMPLOYEES Table
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE,
    manager_id INT
);

-- Sample data
INSERT INTO employees VALUES
(1, 'John Smith', 'Engineering', 85000.00, '2020-03-15', NULL),
(2, 'Sarah Johnson', 'Engineering', 75000.00, '2021-06-01', 1),
(3, 'Mike Brown', 'Marketing', 65000.00, '2019-08-20', NULL),
(4, 'Emily Davis', 'Marketing', 55000.00, '2022-01-10', 3),
(5, 'David Wilson', 'Sales', 70000.00, '2020-11-05', NULL),
(6, 'Lisa Anderson', 'Sales', 60000.00, '2021-09-15', 5),
(7, 'James Taylor', 'Engineering', 90000.00, '2018-04-22', 1),
(8, 'Emma Martinez', 'HR', 50000.00, '2023-02-28', NULL),
(9, 'Robert Garcia', 'Sales', 72000.00, '2020-07-12', 5),
(10, 'Jennifer Lee', 'Engineering', 82000.00, '2021-03-08', 1);
```

### PROJECTS Table
```sql
CREATE TABLE projects (
    id INT PRIMARY KEY,
    project_name VARCHAR(100),
    employee_id INT,
    budget DECIMAL(12, 2),
    start_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Sample data
INSERT INTO projects VALUES
(1, 'Website Redesign', 2, 50000.00, '2023-01-15', 'Completed'),
(2, 'Mobile App', 7, 150000.00, '2023-03-01', 'In Progress'),
(3, 'Marketing Campaign', 4, 30000.00, '2023-04-10', 'In Progress'),
(4, 'CRM Implementation', 1, 200000.00, '2022-06-01', 'Completed'),
(5, 'Sales Dashboard', 6, 25000.00, '2023-05-20', 'Not Started'),
(6, 'Data Migration', 10, 75000.00, '2023-02-15', 'In Progress'),
(7, 'Security Audit', 7, 40000.00, '2023-06-01', 'Not Started');
```

---

## Practice Exercises

### Exercise 1: Basic SELECT
**Task:** Select all employees' names and their salaries.

```sql
-- Your answer here:

```

<details>
<summary>💡 Click to see solution</summary>

```sql
SELECT name, salary FROM employees;
```
</details>

---

### Exercise 2: WHERE Clause
**Task:** Find all employees in the Engineering department.

```sql
-- Your answer here:

```

<details>
<summary>💡 Click to see solution</summary>

```sql
SELECT * FROM employees WHERE department = 'Engineering';
```
</details>

---

### Exercise 3: Multiple Conditions
**Task:** Find all employees who earn more than $60,000 AND work in Sales.

```sql
-- Your answer here:

```

<details>
<summary>💡 Click to see solution</summary>

```sql
SELECT * FROM employees 
WHERE salary > 60000 AND department = 'Sales';
```
</details>

---

### Exercise 4: ORDER BY
**Task:** List all employees ordered by salary from highest to lowest.

```sql
-- Your answer here:

```

<details>
<summary>💡 Click to see solution</summary>

```sql
SELECT * FROM employees ORDER BY salary DESC;
```
</details>

---

### Exercise 5: LIMIT with ORDER BY
**Task:** Find the 3 highest-paid employees.

```sql
-- Your answer here:

```

<details>
<summary>💡 Click to see solution</summary>

```sql
SELECT * FROM employees 
ORDER BY salary DESC 
LIMIT 3;
```
</details>

---

### Exercise 6: INSERT
**Task:** Add a new employee: "Alex Thompson" in "Finance" department, salary $68,000, hired today.

```sql
-- Your answer here:

```

<details>
<summary>💡 Click to see solution</summary>

```sql
INSERT INTO employees (id, name, department, salary, hire_date, manager_id)
VALUES (11, 'Alex Thompson', 'Finance', 68000.00, CURRENT_DATE, NULL);
```
</details>

---

### Exercise 7: UPDATE
**Task:** Give all employees in the Sales department a 10% raise.

```sql
-- Your answer here:

```

<details>
<summary>💡 Click to see solution</summary>

```sql
UPDATE employees 
SET salary = salary * 1.10 
WHERE department = 'Sales';
```
</details>

---

### Exercise 8: DELETE
**Task:** Delete all projects with status 'Not Started'.

```sql
-- Your answer here:

```

<details>
<summary>💡 Click to see solution</summary>

```sql
DELETE FROM projects WHERE status = 'Not Started';
```
</details>

---

### Exercise 9: INNER JOIN
**Task:** List all employees and their project names (only employees with projects).

```sql
-- Your answer here:

```

<details>
<summary>💡 Click to see solution</summary>

```sql
SELECT e.name, p.project_name
FROM employees e
INNER JOIN projects p ON e.id = p.employee_id;
```
</details>

---

### Exercise 10: LEFT JOIN
**Task:** List ALL employees and their project names (include employees without projects).

```sql
-- Your answer here:

```

<details>
<summary>💡 Click to see solution</summary>

```sql
SELECT e.name, p.project_name
FROM employees e
LEFT JOIN projects p ON e.id = p.employee_id;
```
</details>

---

## Bonus Challenges 🌟

Try these extra queries if you want more practice:

### Bonus 1: Complex Query
**Task:** Find the total salary expense per department, ordered by expense (highest first).

<details>
<summary>💡 Click to see solution</summary>

```sql
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
ORDER BY total_salary DESC;
```
</details>

### Bonus 2: Multiple JOINs with Aggregation
**Task:** Find each employee's name and total budget of their projects.

<details>
<summary>💡 Click to see solution</summary>

```sql
SELECT e.name, SUM(p.budget) AS total_project_budget
FROM employees e
LEFT JOIN projects p ON e.id = p.employee_id
GROUP BY e.id, e.name
ORDER BY total_project_budget DESC;
```
</details>

### Bonus 3: Subquery
**Task:** Find employees who earn more than the average salary.

<details>
<summary>💡 Click to see solution</summary>

```sql
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```
</details>

---

## Practice Complete! ✅

Great work on completing the SQL practice exercises!

**Scoring Guide:**
- ✅ 10/10 queries correct: SQL Master! Ready for the test!
- ✅ 7-9 queries correct: Great job! Review missed concepts.
- ✅ 5-6 queries correct: Good progress! Practice more.
- ❌ Below 5: Review the lesson and try again!

**Next Step:** Take the daily test in `Day10_Test.md`!
