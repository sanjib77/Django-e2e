# Day 10: SQL Essentials 🗃️

Welcome to Day 10 of the Python Web & AI/ML Developer Bootcamp!

## Today's Topics

According to the curriculum, today we cover:
- ✅ Database basics
- ✅ SELECT, INSERT, UPDATE, DELETE
- ✅ WHERE, ORDER BY, LIMIT
- ✅ JOINs (INNER, LEFT)
- ✅ Quick practice: Write 10 SQL queries

## Files in This Folder

| File | Description |
|------|-------------|
| `Day10_SQL_Essentials.md` | Main lesson with all SQL concepts |
| `Day10_Practice.md` | 10 SQL query exercises with solutions |
| `Day10_Test.md` | Daily test (14 points, 70% to pass) |

## Learning Path

1. **Read** `Day10_SQL_Essentials.md` (30-40 minutes)
2. **Practice** queries in `Day10_Practice.md` (15-20 minutes)
3. **Take the test** in `Day10_Test.md` (15 minutes)

## Key Concepts

### CRUD Operations
- **C**reate → `INSERT INTO`
- **R**ead → `SELECT`
- **U**pdate → `UPDATE`
- **D**elete → `DELETE`

### Quick Reference
```sql
-- Select with filters
SELECT * FROM users WHERE age > 25 ORDER BY name LIMIT 10;

-- Insert
INSERT INTO users (name, email) VALUES ('Alice', 'alice@email.com');

-- Update (always use WHERE!)
UPDATE users SET name = 'Bob' WHERE id = 1;

-- Delete (always use WHERE!)
DELETE FROM users WHERE id = 1;

-- INNER JOIN (matching records only)
SELECT * FROM users u INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN (all from left table)
SELECT * FROM users u LEFT JOIN orders o ON u.id = o.user_id;
```

## Next: Day 11
Tomorrow we start **Django Part 1 - Setup & Basics**!

Good luck! 🚀
