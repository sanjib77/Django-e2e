# Day 9: Git Version Control 🚀

## 📋 Today's Learning Objectives

By the end of this lesson, you will be able to:
- ✅ Understand Git fundamentals and why version control matters
- ✅ Master essential Git commands: init, add, commit, push, pull
- ✅ Work with branches and merge code
- ✅ Follow professional GitHub workflows
- ✅ Create and use .gitignore files effectively
- ✅ Create and push your own repository

---

## ⏱️ Quick Recap (2 minutes)

In Day 8, we covered Web & HTTP Fundamentals:
- Client-server architecture
- HTTP methods (GET, POST, PUT, DELETE)
- Status codes (200, 404, 500)
- REST API basics and JSON format

Today, we're learning Git - the most essential tool for any developer!

---

## 🎯 What is Git and Why Use It?

**Git** is a distributed version control system that tracks changes in your code over time.

### Why Git Matters:
- 📝 **History**: Track every change made to your code
- 🔄 **Undo mistakes**: Roll back to previous versions
- 👥 **Collaboration**: Multiple developers can work on the same project
- 🌿 **Branching**: Work on features without affecting the main code
- 💼 **Industry Standard**: Every tech company uses Git

### Git vs GitHub:
| Git | GitHub |
|-----|--------|
| Version control software | Cloud hosting platform |
| Works locally | Works online |
| Command-line tool | Web interface |
| Tracks changes | Stores repositories |

---

## 🔧 Section 1: Git Basics

### Installing Git

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install git

# macOS (with Homebrew)
brew install git

# Windows - Download from https://git-scm.com/

# Verify installation
git --version
```

### Initial Configuration

```bash
# Set your name and email (required for commits)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Check your configuration
git config --list
```

---

## 📚 Section 2: Essential Git Commands

### 1. `git init` - Initialize a Repository

Creates a new Git repository in your current directory.

```bash
# Create a new project folder
mkdir my-project
cd my-project

# Initialize Git
git init

# Output: Initialized empty Git repository in /path/to/my-project/.git/
```

### 2. `git status` - Check Repository Status

Shows the current state of your working directory.

```bash
git status

# Example output:
# On branch main
# No commits yet
# nothing to commit (create/copy files and use "git add" to track)
```

### 3. `git add` - Stage Changes

Stages files for the next commit.

```bash
# Stage a single file
git add filename.py

# Stage multiple files
git add file1.py file2.py

# Stage all changes in current directory
git add .

# Stage all changes in entire repository
git add -A
```

### 4. `git commit` - Save Changes

Saves staged changes to the repository with a message.

```bash
# Commit with a message
git commit -m "Add initial project files"

# Commit with multi-line message
git commit -m "Add login feature" -m "- Created login form
- Added validation
- Connected to database"

# Stage and commit in one command (tracked files only)
git commit -am "Update README"
```

### Good Commit Message Examples:
```
✅ "Add user authentication feature"
✅ "Fix login button not responding"
✅ "Update README with installation instructions"

❌ "fix" (too vague)
❌ "changes" (not descriptive)
❌ "asdfasdf" (meaningless)
```

### 5. `git log` - View Commit History

```bash
# View full commit history
git log

# View condensed history (one line per commit)
git log --oneline

# View last 5 commits
git log -5

# View history with graph
git log --oneline --graph --all
```

### 6. `git push` - Upload to Remote

Sends your commits to a remote repository (like GitHub).

```bash
# Push to default remote
git push

# Push to specific remote and branch
git push origin main

# Push and set upstream
git push -u origin main
```

### 7. `git pull` - Download from Remote

Downloads changes from a remote repository.

```bash
# Pull latest changes
git pull

# Pull from specific remote and branch
git pull origin main
```

### 8. `git clone` - Copy a Repository

Creates a local copy of a remote repository.

```bash
# Clone a repository
git clone https://github.com/username/repo-name.git

# Clone into a specific folder
git clone https://github.com/username/repo-name.git my-folder
```

---

## 🌿 Section 3: Branching and Merging

### Why Use Branches?
- Work on features without affecting main code
- Multiple people can work simultaneously
- Test changes before merging to main

### Branch Commands

```bash
# List all branches
git branch

# Create a new branch
git branch feature-login

# Switch to a branch
git checkout feature-login

# Create and switch in one command
git checkout -b feature-signup

# Modern alternative (Git 2.23+)
git switch feature-login
git switch -c feature-payments
```

### Merging Branches

```bash
# Switch to main branch
git checkout main

# Merge feature branch into main
git merge feature-login

# Delete branch after merging
git branch -d feature-login
```

### Practical Branching Example

```bash
# Start on main branch
git checkout main

# Create feature branch
git checkout -b add-navbar

# Make changes and commit
echo "<nav>Home | About | Contact</nav>" > navbar.html
git add navbar.html
git commit -m "Add navbar component"

# Switch back to main
git checkout main

# Merge the feature
git merge add-navbar

# Delete feature branch
git branch -d add-navbar
```

### Handling Merge Conflicts

When the same file is modified in different branches:

```bash
# Try to merge
git merge feature-branch

# If conflict occurs:
# CONFLICT (content): Merge conflict in file.txt
# Automatic merge failed; fix conflicts and then commit the result.

# Open the file and look for conflict markers:
# <<<<<<< HEAD
# Your changes
# =======
# Their changes
# >>>>>>> feature-branch

# Edit the file to resolve conflicts, then:
git add file.txt
git commit -m "Resolve merge conflict in file.txt"
```

---

## 🌐 Section 4: GitHub Workflow

### Setting Up GitHub

1. Create account at [github.com](https://github.com)
2. Create a new repository
3. Connect local repo to GitHub

### Connecting Local to GitHub

```bash
# Add remote origin
git remote add origin https://github.com/username/repo-name.git

# Verify remote
git remote -v

# Push to GitHub
git push -u origin main
```

### Standard GitHub Workflow

```
1. Fork repository (if contributing to others' project)
2. Clone to local machine
3. Create feature branch
4. Make changes and commit
5. Push branch to GitHub
6. Create Pull Request
7. Code review
8. Merge Pull Request
```

### Pull Request Workflow

```bash
# Create feature branch
git checkout -b feature/add-auth

# Make changes, add, commit
git add .
git commit -m "Add authentication system"

# Push branch to GitHub
git push -u origin feature/add-auth

# Then go to GitHub.com and create a Pull Request
```

---

## 📄 Section 5: .gitignore

### What is .gitignore?

A file that tells Git which files/folders to ignore (not track).

### Common Files to Ignore

```gitignore
# .gitignore file

# Python
__pycache__/
*.py[cod]
*.so
.Python
venv/
env/
.env

# IDE/Editor
.vscode/
.idea/
*.swp
*.swo
*~

# OS Files
.DS_Store
Thumbs.db

# Dependencies
node_modules/
vendor/

# Build outputs
dist/
build/
*.egg-info/

# Secrets (IMPORTANT!)
.env
*.pem
secrets.json
config/local.py

# Logs
*.log
logs/

# Database
*.db
*.sqlite3
```

### Creating .gitignore

```bash
# Create .gitignore file
touch .gitignore

# Add patterns
echo "venv/" >> .gitignore
echo "*.pyc" >> .gitignore
echo ".env" >> .gitignore
```

### Using .gitignore Templates

GitHub provides templates for different languages:
- [gitignore.io](https://www.toptal.com/developers/gitignore)
- [GitHub gitignore templates](https://github.com/github/gitignore)

### Stop Tracking Already Tracked Files

```bash
# Remove from tracking but keep file locally
git rm --cached filename.py

# Remove entire folder from tracking
git rm -r --cached folder_name/
```

---

## 💻 Hands-On Practice Exercises

### Exercise 1: Create Your First Repository

```bash
# Step 1: Create project folder
mkdir my-first-repo
cd my-first-repo

# Step 2: Initialize Git
git init

# Step 3: Create a file
echo "# My First Project" > README.md
echo "print('Hello, Git!')" > main.py

# Step 4: Stage files
git add .

# Step 5: Commit
git commit -m "Initial commit: Add README and main.py"

# Step 6: Check status and log
git status
git log --oneline
```

### Exercise 2: Practice Branching

```bash
# Start from Exercise 1

# Create feature branch
git checkout -b feature/add-greeting

# Modify main.py
echo "print('Welcome to my project!')" >> main.py

# Stage and commit
git add main.py
git commit -m "Add welcome message"

# Switch back to main
git checkout main

# Merge feature branch
git merge feature/add-greeting

# Delete branch
git branch -d feature/add-greeting

# View history
git log --oneline --graph
```

### Exercise 3: Push to GitHub

1. Go to GitHub.com and create a new repository
2. Don't initialize with README (we have one locally)
3. Connect and push:

```bash
# Connect to GitHub
git remote add origin https://github.com/YOUR_USERNAME/my-first-repo.git

# Push to GitHub
git push -u origin main
```

---

## 📊 Command Reference Cheat Sheet

| Command | Description |
|---------|-------------|
| `git init` | Initialize new repository |
| `git clone <url>` | Clone remote repository |
| `git status` | Check working directory status |
| `git add <file>` | Stage file for commit |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Commit with message |
| `git log` | View commit history |
| `git log --oneline` | Condensed history |
| `git branch` | List branches |
| `git branch <name>` | Create branch |
| `git checkout <branch>` | Switch branch |
| `git checkout -b <name>` | Create and switch |
| `git merge <branch>` | Merge branch |
| `git branch -d <name>` | Delete branch |
| `git remote add origin <url>` | Add remote |
| `git push` | Push to remote |
| `git push -u origin main` | Push and set upstream |
| `git pull` | Pull from remote |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |
| `git reset HEAD <file>` | Unstage file |
| `git checkout -- <file>` | Discard changes |

---

## ⚠️ Common Mistakes & Solutions

### Mistake 1: Forgetting to Configure Git
```bash
# Error: Please tell me who you are
# Solution:
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### Mistake 2: Committing Sensitive Data
```bash
# If you accidentally committed secrets:
# 1. Add to .gitignore
echo "secrets.txt" >> .gitignore

# 2. Remove from tracking
git rm --cached secrets.txt

# 3. Commit the fix
git commit -m "Remove secrets from tracking"

# Note: The secret is still in history - consider using git filter-branch or BFG Repo-Cleaner
```

### Mistake 3: Pushing to Wrong Branch
```bash
# Check current branch before pushing
git branch

# Always specify branch if unsure
git push origin feature-branch
```

---

## ✅ Today's Summary

You learned:
1. **Git Basics**: init, status, add, commit, log
2. **Remote Operations**: clone, push, pull, remote
3. **Branching**: branch, checkout, merge
4. **GitHub Workflow**: Fork → Clone → Branch → Commit → Push → PR → Merge
5. **.gitignore**: Keep sensitive and unnecessary files out of Git

---

## 📝 Next Steps

1. Complete the practice exercises
2. Take the Daily Test (see `daily_test.md`)
3. Push your practice repository to GitHub
4. Tomorrow: Day 10 - SQL Essentials

---

## 🔗 Additional Resources

- [Git Official Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet (PDF)](https://education.github.com/git-cheat-sheet-education.pdf)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)
- [GitHub Skills](https://skills.github.com/)

---

**Remember**: Git is a skill that improves with practice. The more you use it, the more natural it becomes! 💪
