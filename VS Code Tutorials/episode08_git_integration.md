# Episode 8: Git Integration

## Overview
VS Code provides excellent Git integration through its Source Control panel, making version control operations intuitive and visual. This episode covers Git basics, branching workflows, conflict resolution, and advanced Git features within VS Code.

## Git Basics in VS Code

### Prerequisites
- Git installed on your system
- Basic understanding of version control concepts
- Repository initialized or cloned

### Checking Git Installation
```bash
# In VS Code terminal
git --version
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Source Control Panel
- **Access:** Click Source Control icon in Activity Bar (`Ctrl+Shift+G`)
- **Features:** View changes, stage files, commit, branch management
- **Integration:** Seamless workflow without leaving VS Code

## Repository Initialization and Cloning

### Creating a New Repository

#### Initialize Local Repository
1. Open folder in VS Code
2. Open Source Control panel
3. Click "Initialize Repository" button
4. Or use terminal: `git init`

#### Repository Structure
```
my-project/
├── .git/               # Git metadata (hidden)
├── .gitignore         # Files to ignore
├── README.md          # Project documentation
├── src/               # Source code
│   ├── index.js
│   └── utils.js
└── package.json       # Project configuration
```

### Cloning Existing Repository

#### Method 1: Command Palette
1. Press `Ctrl+Shift+P`
2. Type "Git: Clone"
3. Enter repository URL
4. Choose local directory

#### Method 2: Welcome Screen
- Click "Clone Repository" on Welcome tab
- Enter URL and select location

#### Method 3: Terminal
```bash
git clone https://github.com/username/repository.git
cd repository
code .
```

## Working with Changes

### Understanding File States

#### Git Status Indicators
- **U** - Untracked (new files)
- **M** - Modified (changes made)
- **A** - Added (staged for commit)
- **D** - Deleted (removed files)
- **R** - Renamed (moved files)
- **C** - Copied
- **?** - Ignored

#### Color Coding
- **Green** - Added/staged files
- **Red** - Modified/unstaged files
- **Gray** - Ignored files

### Staging Changes

#### Staging Individual Files
1. Open Source Control panel
2. Hover over changed file
3. Click "+" icon to stage
4. Or right-click file > "Stage Changes"

#### Staging All Changes
- Click "+" next to "Changes" section
- Or use `Ctrl+Shift+P` > "Git: Stage All Changes"

#### Unstaging Changes
- Click "-" icon next to staged file
- Or right-click > "Unstage Changes"

### Viewing Differences

#### File Diff View
- Click on modified file in Source Control panel
- Shows side-by-side comparison
- Red: removed lines, Green: added lines

#### Inline Diff
- Click gear icon in diff editor
- Toggle inline view for single-column diff

#### Gutter Indicators
- **Green bar** - Added lines
- **Red triangle** - Deleted lines
- **Blue bar** - Modified lines

### Committing Changes

#### Creating Commits
1. Stage desired changes
2. Enter commit message in message box
3. Press `Ctrl+Enter` or click checkmark icon

#### Commit Message Best Practices
```
feat: add user authentication system

- Implement login/logout functionality
- Add JWT token validation
- Create user session management
- Update API endpoints for auth

Resolves: #123
```

#### Commit Message Templates
```json
{
  "git.inputValidation": "always",
  "git.inputValidationLength": 72,
  "git.inputValidationSubjectLength": 50
}
```

### Amending Commits
- **Last commit:** `Ctrl+Shift+P` > "Git: Commit Staged (Amend)"
- Useful for fixing commit messages or adding forgotten files
- Only amend commits that haven't been pushed

## Branching and Merging

### Branch Management

#### Creating Branches
1. **Method 1:** Click branch name in status bar
2. **Method 2:** Source Control panel > "..." > "Create Branch"
3. **Method 3:** Command Palette > "Git: Create Branch"

#### Branch Naming Conventions
```
main/master           # Main development branch
develop              # Integration branch
feature/user-auth    # New features
bugfix/login-error   # Bug fixes
hotfix/security-patch # Critical fixes
release/v1.2.0       # Release preparation
```

#### Switching Branches
- Click branch name in status bar
- Select from dropdown list
- Or use Command Palette > "Git: Checkout to..."

### Branch Workflow Example

#### Feature Branch Workflow
```bash
# Create and switch to feature branch
git checkout -b feature/shopping-cart

# Make changes and commit
git add .
git commit -m "Add shopping cart functionality"

# Switch back to main
git checkout main

# Merge feature branch
git merge feature/shopping-cart

# Delete feature branch
git branch -d feature/shopping-cart
```

### Branch Visualization
- Use GitLens extension for enhanced branch visualization
- Timeline view shows branch history
- Branch graph in Source Control panel

## Remote Repository Operations

### Remote Management

#### Adding Remotes
```bash
# Add origin remote
git remote add origin https://github.com/username/repo.git

# Add upstream for forks
git remote add upstream https://github.com/original/repo.git

# View remotes
git remote -v
```

#### Remote Operations in VS Code
- **Push:** Source Control panel > "..." > "Push"
- **Pull:** Source Control panel > "..." > "Pull"
- **Fetch:** Source Control panel > "..." > "Fetch"

### Synchronizing Changes

#### Push Changes
1. Commit your changes locally
2. Click "Sync Changes" in status bar
3. Or Source Control panel > "..." > "Push"

#### Pull Changes
- Click "Sync Changes" if there are remote updates
- VS Code shows incoming/outgoing changes count
- Automatically fetches updates periodically

#### Handling Push Rejections
```bash
# If push is rejected due to remote changes
git pull --rebase origin main
# Resolve any conflicts
git push origin main
```

## Conflict Resolution

### Understanding Merge Conflicts

#### When Conflicts Occur
- Same file modified in different branches
- Conflicting changes in same lines
- File renamed/moved in different ways

#### Conflict Indicators
```javascript
<<<<<<< HEAD
const userName = "currentUser";
=======
const userName = "activeUser";
>>>>>>> feature-branch
```

### Resolving Conflicts in VS Code

#### Conflict Resolution Interface
1. VS Code opens conflict files automatically
2. Shows "Accept Current Change" and "Accept Incoming Change" options
3. Can accept both or manually edit

#### Resolution Options
- **Accept Current Change** - Keep your version
- **Accept Incoming Change** - Keep remote version
- **Accept Both Changes** - Include both modifications
- **Compare Changes** - See detailed diff

#### Manual Conflict Resolution
```javascript
// Before resolution
<<<<<<< HEAD
function calculateTotal(price, tax) {
  return price + (price * tax);
}
=======
function calculateTotal(price, taxRate) {
  return price * (1 + taxRate);
}
>>>>>>> feature-branch

// After manual resolution
function calculateTotal(price, taxRate) {
  return price * (1 + taxRate);
}
```

### Conflict Resolution Workflow
1. **Identify conflicts** - VS Code highlights conflicted files
2. **Open conflict editor** - Click on conflicted file
3. **Resolve each conflict** - Choose appropriate resolution
4. **Stage resolved files** - Add to staging area
5. **Complete merge** - Commit the resolution

## Advanced Git Features

### Git Stash

#### When to Use Stash
- Switch branches with uncommitted changes
- Temporarily save work without committing
- Pull changes when working directory is dirty

#### Stash Operations
```bash
# Stash current changes
git stash

# Stash with message
git stash push -m "Work in progress on feature"

# List stashes
git stash list

# Apply latest stash
git stash pop

# Apply specific stash
git stash apply stash@{1}

# Drop stash
git stash drop stash@{0}
```

#### Stash in VS Code
- Command Palette > "Git: Stash"
- Source Control panel > "..." > "Stash"
- View stashes in Source Control panel

### Git History and Timeline

#### File History
- Right-click file > "Open Timeline"
- Shows all commits affecting the file
- Click commit to see changes

#### Commit History
- Use GitLens extension for enhanced history
- Source Control panel shows recent commits
- Click commits to view details

### Cherry Picking

#### What is Cherry Picking?
- Apply specific commits from other branches
- Useful for backporting fixes
- Selective change integration

#### Cherry Pick in VS Code
1. View commit history
2. Right-click desired commit
3. Select "Cherry Pick Commit"
4. Resolve any conflicts

### Interactive Rebase

#### When to Use Rebase
- Clean up commit history
- Combine multiple commits
- Reorder commits
- Edit commit messages

#### Rebase Operations
```bash
# Interactive rebase last 3 commits
git rebase -i HEAD~3

# Rebase onto another branch
git rebase main feature-branch
```

## GitLens Extension Features

### Installation and Setup
```json
{
  "gitlens.blame.format": "${author}, ${agoOrDate}",
  "gitlens.blame.highlight.locations": ["gutter", "line", "overview"],
  "gitlens.codeLens.authors.enabled": false,
  "gitlens.currentLine.enabled": true
}
```

### Key GitLens Features

#### Git Blame Annotations
- Shows who changed each line and when
- Inline blame information
- Hover for detailed commit info

#### Code Lens
- Shows recent changes above functions/classes
- Quick access to file history
- Author information for code blocks

#### Git Graph
- Visual representation of repository history
- Interactive branch and commit exploration
- Merge and branch visualization

#### File Annotations
- Heat map showing recent changes
- Changes annotation for modified lines
- Toggle annotations easily

## Git Configuration in VS Code

### Git Settings
```json
{
  "git.enableSmartCommit": true,
  "git.confirmSync": false,
  "git.autofetch": true,
  "git.autoStash": true,
  "git.defaultCloneDirectory": "~/projects",
  "git.openRepositoryInParentFolders": "always"
}
```

### Commit Message Configuration
```json
{
  "git.inputValidation": "always",
  "git.inputValidationLength": 72,
  "git.inputValidationSubjectLength": 50,
  "git.useCommitInputAsStashMessage": true
}
```

### Diff Tool Configuration
```json
{
  "diffEditor.ignoreTrimWhitespace": false,
  "diffEditor.renderSideBySide": true,
  "diffEditor.wordWrap": "off"
}
```

## Common Git Workflows

### Feature Development Workflow
1. **Create feature branch** from main
2. **Make changes** and commit regularly
3. **Push branch** to remote repository
4. **Create pull request** for review
5. **Merge to main** after approval
6. **Delete feature branch**

### Hotfix Workflow
1. **Create hotfix branch** from main
2. **Fix critical issue** quickly
3. **Test thoroughly** before merge
4. **Merge to main** and develop
5. **Tag release** if needed
6. **Deploy immediately**

### Release Workflow
1. **Create release branch** from develop
2. **Finalize features** and fix bugs
3. **Update version numbers**
4. **Merge to main** and tag
5. **Merge back to develop**
6. **Deploy release**

## Troubleshooting Git Issues

### Common Problems

#### Authentication Issues
```bash
# Configure credentials
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# For HTTPS repositories
git config --global credential.helper store

# For SSH keys
ssh-keygen -t ed25519 -C "your@email.com"
```

#### Large File Issues
```bash
# Track large files with Git LFS
git lfs track "*.psd"
git lfs track "*.zip"
git add .gitattributes
```

#### Sync Issues
```bash
# Reset to match remote
git fetch origin
git reset --hard origin/main

# Force push (dangerous)
git push --force-with-lease origin feature-branch
```

### Git Recovery

#### Recovering Lost Commits
```bash
# Find lost commits
git reflog

# Recover commit
git checkout <commit-hash>
git branch recovery-branch
```

#### Undoing Changes
```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Revert commit (safe for shared branches)
git revert <commit-hash>
```

## Practical Exercises

### Exercise 1: Basic Git Workflow
1. Initialize a new repository
2. Create and modify files
3. Stage and commit changes
4. View commit history and diffs

### Exercise 2: Branching Practice
1. Create a feature branch
2. Make commits on the branch
3. Switch between branches
4. Merge feature branch to main

### Exercise 3: Conflict Resolution
1. Create conflicting changes in two branches
2. Attempt to merge branches
3. Resolve conflicts using VS Code interface
4. Complete the merge successfully

### Exercise 4: Remote Collaboration
1. Clone a repository from GitHub
2. Create a feature branch
3. Push changes to remote
4. Create a pull request

## Best Practices

### Commit Best Practices
1. **Make small, focused commits**
2. **Write clear commit messages**
3. **Commit frequently** during development
4. **Test before committing**
5. **Use conventional commit formats**

### Branch Management
1. **Use descriptive branch names**
2. **Keep branches small and focused**
3. **Delete merged branches**
4. **Regularly sync with main branch**
5. **Use pull requests for code review**

### Repository Organization
1. **Use .gitignore appropriately**
2. **Keep repository clean**
3. **Document branching strategy**
4. **Use tags for releases**
5. **Regular repository maintenance**

## Next Steps

In Episode 9, we'll explore:
- Setting up debugging configurations
- Using breakpoints and debug console
- Debugging different types of applications
- Advanced debugging techniques and troubleshooting

---

**Previous Episode:** Integrated Terminal  
**Next Episode:** Debugging Basics  
**Duration:** Approximately 35-40 minutes  
**Prerequisites:** Episodes 1-7 completed, basic Git knowledge helpful