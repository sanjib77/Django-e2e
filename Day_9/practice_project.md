# Day 9 Practice Project: Create and Push Your First Repository 🚀

## Project Objective

By the end of this practice, you will have:
- Created a local Git repository
- Made multiple commits
- Worked with branches
- Created a proper `.gitignore` file
- Pushed your repository to GitHub

---

## Part 1: Project Setup (10 minutes)

### Step 1: Create Your Project

Open your terminal and run:

```bash
# Create project directory
mkdir python-git-practice
cd python-git-practice

# Initialize Git
git init

# Verify Git is initialized
ls -la  # You should see .git folder
```

### Step 2: Configure Git (if not done already)

```bash
# Set your identity
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Step 3: Create Initial Files

Create the following files:

**README.md**
```markdown
# Python Git Practice

A simple Python project to practice Git version control.

## Features
- Basic Python calculator
- Practice with Git commands

## How to Run
```bash
python main.py
```

## Author
Your Name
```

**main.py**
```python
#!/usr/bin/env python3
"""
Simple Calculator - Git Practice Project
Day 9 of Python Bootcamp
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    """Main function to demonstrate calculator"""
    print("=== Simple Calculator ===")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")

if __name__ == "__main__":
    main()
```

**.gitignore**
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment
.env
*.local

# Logs
*.log
```

### Step 4: Make Your First Commit

```bash
# Check status
git status

# Stage all files
git add .

# Commit
git commit -m "Initial commit: Add calculator project"

# View your commit
git log --oneline
```

---

## Part 2: Working with Branches (15 minutes)

### Step 5: Create a Feature Branch

```bash
# Create and switch to new branch
git checkout -b feature/add-power-function

# Verify you're on the new branch
git branch
```

### Step 6: Add New Feature

Edit `main.py` and add the power function:

```python
def power(base, exponent):
    """Raise base to the power of exponent"""
    return base ** exponent
```

Also update the `main()` function:

```python
def main():
    """Main function to demonstrate calculator"""
    print("=== Simple Calculator ===")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")
    print(f"2 ^ 8 = {power(2, 8)}")  # New line
```

### Step 7: Commit the Feature

```bash
# Check what changed
git diff

# Stage and commit
git add main.py
git commit -m "Add power function to calculator"

# View branch history
git log --oneline --graph --all
```

### Step 8: Merge Feature to Main

```bash
# Switch to main branch
git checkout main

# Merge the feature branch
git merge feature/add-power-function

# View the merged result
git log --oneline

# Delete the feature branch (optional)
git branch -d feature/add-power-function
```

---

## Part 3: Push to GitHub (10 minutes)

### Step 9: Create GitHub Repository

1. Go to [github.com](https://github.com) and log in
2. Click the **+** icon → **New repository**
3. Name it: `python-git-practice`
4. Description: "A simple Python project to practice Git"
5. **Do NOT** initialize with README (we have one)
6. Click **Create repository**

### Step 10: Connect and Push

```bash
# Add GitHub as remote
git remote add origin https://github.com/YOUR_USERNAME/python-git-practice.git

# Verify remote
git remote -v

# Push to GitHub
git push -u origin main
```

### Step 11: Verify on GitHub

1. Refresh your GitHub repository page
2. You should see all your files
3. Click on commits to see your history

---

## Part 4: Simulate Collaboration (10 minutes)

### Step 12: Make Changes on GitHub

1. On GitHub, click on `README.md`
2. Click the ✏️ pencil icon to edit
3. Add a new line under "## Features":
   ```
   - Power function for exponents
   ```
4. Scroll down and click **Commit changes**

### Step 13: Pull Changes Locally

```bash
# Pull the changes from GitHub
git pull

# View the updated README
cat README.md

# View the commit
git log --oneline
```

---

## Part 5: Advanced Practice (Optional - 15 minutes)

### Challenge 1: Create Another Feature Branch

Create a branch called `feature/add-modulo` and:
1. Add a modulo function
2. Update main() to use it
3. Commit with a good message
4. Merge to main
5. Push to GitHub

### Challenge 2: Handle a "Merge Conflict"

1. Create branch `feature/update-readme`
2. Edit README on this branch
3. Switch to main and edit the same line differently
4. Try to merge and resolve the conflict

### Challenge 3: Create a GitHub Pull Request

1. Create a new branch locally
2. Make changes and push the branch to GitHub
3. Go to GitHub and create a Pull Request
4. Review the changes
5. Merge the PR on GitHub
6. Pull the changes locally

---

## Verification Checklist ✅

Before you finish, make sure you can check all these boxes:

- [ ] Created a local Git repository
- [ ] Made at least 3 commits
- [ ] Created and merged a feature branch
- [ ] Have a proper `.gitignore` file
- [ ] Connected to GitHub remote
- [ ] Pushed all changes to GitHub
- [ ] Successfully pulled changes from GitHub

---

## Common Issues & Solutions

### Issue: "git push" rejected

```bash
# Solution: Pull first, then push
git pull --rebase
git push
```

### Issue: Can't switch branches with uncommitted changes

```bash
# Option 1: Commit your changes
git add .
git commit -m "WIP: Save progress"

# Option 2: Stash your changes
git stash
git checkout other-branch
# Later: git stash pop
```

### Issue: Accidentally committed to wrong branch

```bash
# Option 1: If not pushed yet
git reset HEAD~1 --soft  # Keeps changes staged
git checkout correct-branch
git commit -m "Your message"
```

---

## Project Complete! 🎉

Congratulations! You've successfully:

1. ✅ Created a Git repository from scratch
2. ✅ Made multiple commits with good messages
3. ✅ Worked with branches (create, switch, merge)
4. ✅ Used `.gitignore` to exclude files
5. ✅ Connected to GitHub and pushed your code
6. ✅ Pulled changes from remote

You're now ready to use Git in your daily development workflow!

---

## Next Steps

- Complete the Daily Test (`daily_test.md`)
- Keep practicing by creating more repositories
- Try contributing to an open-source project
- Tomorrow: Day 10 - SQL Essentials
