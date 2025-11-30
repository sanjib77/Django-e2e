# Day 9 Daily Test: Git Version Control 📝

## Test Instructions

- **Total Questions**: 10
- **Time Limit**: 15 minutes
- **Passing Score**: 70% (10 out of 14 points)
- **Scoring**:
  - MCQs/True-False: 1 point each (6 questions = 6 points)
  - Short Coding Challenges: 2 points each (3 questions = 6 points)
  - Conceptual Question: 2 points (1 question = 2 points)

---

## Section A: Multiple Choice & True/False (6 points)

### Question 1 (1 point)
What command initializes a new Git repository?

A) `git start`
B) `git init`
C) `git new`
D) `git create`

---

### Question 2 (1 point)
Which command stages all changes in the current directory for commit?

A) `git commit .`
B) `git stage .`
C) `git add .`
D) `git push .`

---

### Question 3 (1 point)
True or False: `git pull` downloads changes from a remote repository and merges them into your current branch.

A) True
B) False

---

### Question 4 (1 point)
What does `git log --oneline` do?

A) Shows commits with full details
B) Shows commits in a condensed one-line format
C) Shows only the last commit
D) Shows uncommitted changes

---

### Question 5 (1 point)
True or False: A `.gitignore` file tells Git which files to track.

A) True
B) False

---

### Question 6 (1 point)
Which command creates a new branch AND switches to it?

A) `git branch new-feature && git switch new-feature`
B) `git checkout -b new-feature`
C) `git new-branch new-feature`
D) `git create new-feature`

---

## Section B: Short Coding Challenges (6 points)

### Question 7 (2 points)
Write the Git commands to:
1. Configure your Git username as "John Doe"
2. Configure your Git email as "john@example.com"

**Your Answer:**
```bash
# Write your commands here



```

---

### Question 8 (2 points)
You have made changes to `app.py` and `utils.py`. Write the commands to:
1. Stage only `app.py`
2. Commit with the message "Fix login bug in app"

**Your Answer:**
```bash
# Write your commands here



```

---

### Question 9 (2 points)
Write a `.gitignore` entry that would ignore:
1. All Python bytecode files (`.pyc` extension)
2. The `venv` folder
3. Any file named `.env`

**Your Answer:**
```gitignore
# Write your .gitignore entries here



```

---

## Section C: Conceptual Question (2 points)

### Question 10 (2 points)
Explain the difference between `git pull` and `git push`. When would you use each command?

**Your Answer:**
```
Write your explanation here (3-5 sentences):




```

---

## Answer Key (For Self-Assessment)

<details>
<summary>Click to reveal answers after completing the test</summary>

### Section A Answers:

1. **B) `git init`** - This command initializes a new Git repository in the current directory.

2. **C) `git add .`** - The dot (.) represents the current directory, staging all changes.

3. **A) True** - `git pull` fetches and merges changes from the remote repository.

4. **B) Shows commits in a condensed one-line format** - Each commit appears on one line with abbreviated SHA and message.

5. **B) False** - `.gitignore` tells Git which files to IGNORE (not track).

6. **B) `git checkout -b new-feature`** - The `-b` flag creates a new branch and switches to it in one command.

### Section B Answers:

7. **Git Configuration (2 points)**
```bash
git config --global user.name "John Doe"
git config --global user.email "john@example.com"
```

8. **Staging and Committing (2 points)**
```bash
git add app.py
git commit -m "Fix login bug in app"
```

9. **.gitignore Entries (2 points)**
```gitignore
*.pyc
venv/
.env
```

### Section C Answer:

10. **Git Pull vs Push (2 points)**

Sample answer:
"`git pull` downloads changes from a remote repository (like GitHub) and merges them into your local branch. It's used when you want to get the latest changes that others have pushed. `git push` uploads your local commits to the remote repository. It's used when you want to share your changes with others or back up your work to the cloud. In a typical workflow, you `pull` before starting work to get latest changes, and `push` after committing your work."

**Scoring Guide for Q10:**
- 2 points: Correctly explains both commands and when to use them
- 1 point: Partially correct explanation
- 0 points: Incorrect or no answer

</details>

---

## Score Calculation

| Section | Your Score | Max Score |
|---------|------------|-----------|
| A (Q1-6) | ___ | 6 |
| B (Q7-9) | ___ | 6 |
| C (Q10) | ___ | 2 |
| **Total** | ___ | **14** |

**Passing Score: 10/14 (70%)**

---

## What's Next?

- **Score ≥ 70%**: Great job! You're ready for Day 10: SQL Essentials 🎉
- **Score < 70%**: Review the Day 9 README and retake the test tomorrow

---

## Self-Reflection

After completing the test, ask yourself:
1. Which Git commands do I need more practice with?
2. Have I successfully created and pushed a repository to GitHub?
3. Do I understand the branching workflow?

**Remember**: Practice makes perfect! The more you use Git, the more natural it becomes. 💪
