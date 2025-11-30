#!/bin/bash
# ===========================================
# Git Commands Quick Reference Script
# Day 9: Git Version Control
# ===========================================
# This script demonstrates common Git commands
# Run each section separately to practice

# ===========================================
# SECTION 1: INITIAL SETUP
# ===========================================

echo "=== Git Configuration ==="

# Configure username (required for commits)
# git config --global user.name "Your Name"

# Configure email (required for commits)
# git config --global user.email "your.email@example.com"

# View all configurations
# git config --list

# ===========================================
# SECTION 2: REPOSITORY BASICS
# ===========================================

echo "=== Repository Commands ==="

# Initialize a new repository
# git init

# Clone an existing repository
# git clone https://github.com/username/repo.git

# Check repository status
# git status

# ===========================================
# SECTION 3: STAGING AND COMMITTING
# ===========================================

echo "=== Staging and Committing ==="

# Stage a single file
# git add filename.py

# Stage multiple files
# git add file1.py file2.py file3.py

# Stage all changes in current directory
# git add .

# Stage all changes including deletions
# git add -A

# Commit with a message
# git commit -m "Your commit message here"

# Stage and commit tracked files in one command
# git commit -am "Your commit message"

# ===========================================
# SECTION 4: VIEWING HISTORY
# ===========================================

echo "=== History Commands ==="

# View commit history
# git log

# View condensed history (one line per commit)
# git log --oneline

# View last 5 commits
# git log -5

# View history with graph
# git log --oneline --graph --all

# View changes in a specific commit
# git show <commit-hash>

# ===========================================
# SECTION 5: BRANCHING
# ===========================================

echo "=== Branching Commands ==="

# List all branches
# git branch

# List all branches including remote
# git branch -a

# Create a new branch
# git branch feature-name

# Switch to a branch
# git checkout branch-name

# Create and switch to new branch (shortcut)
# git checkout -b new-feature

# Modern alternative (Git 2.23+)
# git switch branch-name
# git switch -c new-branch

# Delete a branch (safe - only if merged)
# git branch -d branch-name

# Force delete a branch
# git branch -D branch-name

# ===========================================
# SECTION 6: MERGING
# ===========================================

echo "=== Merging Commands ==="

# Merge branch into current branch
# git merge branch-to-merge

# Merge with commit message
# git merge branch-name -m "Merge message"

# Abort a merge (if conflicts)
# git merge --abort

# ===========================================
# SECTION 7: REMOTE OPERATIONS
# ===========================================

echo "=== Remote Commands ==="

# Add a remote repository
# git remote add origin https://github.com/username/repo.git

# View remotes
# git remote -v

# Push to remote
# git push origin main

# Push and set upstream
# git push -u origin main

# Pull from remote
# git pull origin main

# Fetch without merging
# git fetch origin

# ===========================================
# SECTION 8: UNDOING CHANGES
# ===========================================

echo "=== Undo Commands ==="

# Discard changes in working directory
# git checkout -- filename.py

# Unstage a file (keep changes)
# git reset HEAD filename.py

# Undo last commit (keep changes staged)
# git reset --soft HEAD~1

# Undo last commit (keep changes unstaged)
# git reset HEAD~1

# Undo last commit (discard changes) - DANGEROUS
# git reset --hard HEAD~1

# ===========================================
# SECTION 9: STASHING
# ===========================================

echo "=== Stash Commands ==="

# Save changes temporarily
# git stash

# Save with a message
# git stash save "Work in progress on feature X"

# List all stashes
# git stash list

# Apply most recent stash
# git stash pop

# Apply specific stash
# git stash apply stash@{2}

# Delete a stash
# git stash drop stash@{0}

# ===========================================
# SECTION 10: VIEWING DIFFERENCES
# ===========================================

echo "=== Diff Commands ==="

# View unstaged changes
# git diff

# View staged changes
# git diff --staged

# View changes between branches
# git diff main feature-branch

# View changes in a file
# git diff filename.py

# ===========================================
# COMMON WORKFLOWS
# ===========================================

echo "=== Common Workflows ==="

# Workflow 1: Daily Development
# -----------------------------
# git pull                    # Get latest changes
# git checkout -b feature/x   # Create feature branch
# # ... make changes ...
# git add .                   # Stage changes
# git commit -m "Add feature" # Commit
# git push -u origin feature/x # Push branch
# # Create Pull Request on GitHub
# git checkout main           # Switch back to main
# git pull                    # Get merged changes

# Workflow 2: Quick Fix
# -----------------------------
# git checkout -b hotfix/bug-123
# # ... fix the bug ...
# git commit -am "Fix critical bug #123"
# git push -u origin hotfix/bug-123
# # Create PR and merge
# git checkout main
# git pull

echo "=== Script Complete ==="
echo "Uncomment commands to practice them!"
