# Episode 7: Integrated Terminal

## Overview
VS Code's integrated terminal is a powerful feature that allows you to run command-line tools without leaving the editor. This episode covers terminal basics, multiple terminal management, shell configuration, and productivity tips.

## Getting Started with the Integrated Terminal

### Opening the Terminal
- **Keyboard shortcut:** `Ctrl+`` (backtick)
- **Menu:** View > Terminal
- **Command Palette:** `Ctrl+Shift+P` > "Terminal: Create New Integrated Terminal"

### Terminal Panel Layout
- **Location:** Bottom panel by default
- **Resizable:** Drag the border to resize
- **Tabs:** Multiple terminals show as tabs
- **Split view:** Split terminals horizontally or vertically

### Basic Terminal Operations
```bash
# Navigate directories
cd /path/to/directory
cd ..                    # Go up one directory
cd ~                     # Go to home directory
pwd                      # Print working directory

# List files
ls                       # List files (Linux/macOS)
dir                      # List files (Windows)
ls -la                   # Detailed list with hidden files

# Create and manage files
mkdir new-folder         # Create directory
touch file.txt           # Create empty file (Linux/macOS)
echo. > file.txt         # Create empty file (Windows)
rm file.txt              # Delete file (Linux/macOS)
del file.txt             # Delete file (Windows)
```

## Terminal Configuration

### Default Shell Configuration

#### Windows PowerShell
```json
{
  "terminal.integrated.defaultProfile.windows": "PowerShell",
  "terminal.integrated.profiles.windows": {
    "PowerShell": {
      "source": "PowerShell",
      "icon": "terminal-powershell"
    },
    "Command Prompt": {
      "path": [
        "${env:windir}\\Sysnative\\cmd.exe",
        "${env:windir}\\System32\\cmd.exe"
      ],
      "args": [],
      "icon": "terminal-cmd"
    },
    "Git Bash": {
      "source": "Git Bash"
    }
  }
}
```

#### macOS/Linux
```json
{
  "terminal.integrated.defaultProfile.osx": "zsh",
  "terminal.integrated.profiles.osx": {
    "zsh": {
      "path": "zsh",
      "args": ["-l"]
    },
    "bash": {
      "path": "bash",
      "args": ["-l"]
    }
  }
}
```

### Terminal Appearance
```json
{
  "terminal.integrated.fontSize": 14,
  "terminal.integrated.fontFamily": "Consolas, 'Courier New', monospace",
  "terminal.integrated.cursorStyle": "block",
  "terminal.integrated.cursorBlinking": true,
  "terminal.integrated.scrollback": 10000
}
```

### Shell Integration Features
- **Command tracking:** Navigate between commands
- **Automatic injection:** Shell integration scripts
- **Command decorations:** Visual indicators for command status
- **Quick fixes:** Suggestions for failed commands

## Multiple Terminal Management

### Creating Multiple Terminals

#### New Terminal Instances
- **New terminal:** `Ctrl+Shift+`` (backtick)
- **From dropdown:** Click "+" in terminal panel
- **Specific shell:** Click dropdown arrow next to "+"

#### Terminal Naming
```bash
# Terminals can be renamed for better organization
Terminal 1: "Server"          # Running development server
Terminal 2: "Git"             # Git operations
Terminal 3: "Build"           # Build and compilation
Terminal 4: "Tests"           # Running tests
```

### Terminal Tabs Navigation
- **Switch tabs:** `Ctrl+PageUp/PageDown`
- **Close terminal:** `Ctrl+Shift+W`
- **Focus terminal:** `Ctrl+``
- **Focus editor:** `Ctrl+1`

### Split Terminals

#### Creating Split Views
- **Split terminal:** `Ctrl+Shift+5`
- **Split horizontally:** Default behavior
- **Split vertically:** Use terminal options

#### Managing Split Terminals
```
┌─────────────────┬─────────────────┐
│   Terminal 1    │   Terminal 2    │
│   npm run dev   │   git status    │
│                 │                 │
├─────────────────┴─────────────────┤
│            Terminal 3             │
│         npm run build             │
└───────────────────────────────────┘
```

### Terminal Groups
- Group related terminals together
- Switch between groups easily
- Organize workflows by project or task

## Development Workflows

### Node.js Development

#### Package Management
```bash
# Initialize new project
npm init -y
npm init @latest

# Install dependencies
npm install express
npm install -D nodemon eslint prettier

# Run scripts
npm run dev
npm run build
npm run test
npm start

# Check for updates
npm outdated
npm audit
```

#### Development Server
```bash
# Start development server
npm run dev

# With live reload
nodemon server.js

# With environment variables
NODE_ENV=development npm start

# Multiple processes
npm run dev & npm run test:watch
```

### Python Development

#### Virtual Environment Management
```bash
# Create virtual environment
python -m venv venv
python3 -m venv myenv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install packages
pip install requests flask
pip install -r requirements.txt

# Freeze dependencies
pip freeze > requirements.txt

# Deactivate environment
deactivate
```

#### Running Python Scripts
```bash
# Run Python files
python app.py
python -m flask run
python -m pytest tests/

# With arguments
python script.py --input data.csv --output results.json

# Interactive mode
python -i
ipython
```

### Git Operations

#### Basic Git Commands
```bash
# Repository initialization
git init
git clone https://github.com/user/repo.git

# Status and staging
git status
git add .
git add file.txt
git reset file.txt

# Committing
git commit -m "Add new feature"
git commit -am "Update and commit all changes"

# Branching
git branch
git branch feature-branch
git checkout feature-branch
git checkout -b new-feature

# Remote operations
git pull
git push
git push origin main
git fetch
```

#### Advanced Git Workflows
```bash
# Interactive rebase
git rebase -i HEAD~3

# Stashing changes
git stash
git stash pop
git stash list

# Viewing history
git log --oneline --graph
git show HEAD
git diff HEAD~1

# Merging
git merge feature-branch
git merge --no-ff feature-branch
```

### Build Tools and Task Runners

#### Webpack
```bash
# Development build
npm run webpack -- --mode development

# Production build
npm run webpack -- --mode production

# Watch mode
npm run webpack -- --watch

# Development server
npx webpack serve --mode development
```

#### Other Build Tools
```bash
# Gulp
gulp build
gulp watch
gulp clean

# Grunt
grunt build
grunt watch

# Vite
npm run dev
npm run build
npm run preview

# Parcel
parcel index.html
parcel build index.html
```

## Advanced Terminal Features

### Command History and Navigation

#### History Navigation
- **Previous command:** `Up Arrow`
- **Next command:** `Down Arrow`
- **Search history:** `Ctrl+R` (reverse search)
- **Clear screen:** `Ctrl+L` or `clear`

#### Command Editing
- **Beginning of line:** `Ctrl+A`
- **End of line:** `Ctrl+E`
- **Delete word:** `Ctrl+W`
- **Delete to end:** `Ctrl+K`

### Terminal Links
- **File links:** Click to open files in editor
- **URL links:** Click to open in browser
- **Line numbers:** Navigate to specific lines
- **Git links:** Open commit hashes or branches

### Terminal Search
- **Open search:** `Ctrl+F`
- **Find next:** `F3`
- **Find previous:** `Shift+F3`
- Works across terminal output history

## Environment Variables and Configuration

### Setting Environment Variables

#### Windows PowerShell
```powershell
# Set for current session
$env:NODE_ENV = "development"
$env:API_KEY = "your-api-key"

# Set permanently
[Environment]::SetEnvironmentVariable("NODE_ENV", "development", "User")

# Using .env files
npm install dotenv
# Then in your app: require('dotenv').config()
```

#### macOS/Linux Bash/Zsh
```bash
# Set for current session
export NODE_ENV=development
export API_KEY=your-api-key

# Set in shell profile
echo 'export NODE_ENV=development' >> ~/.bashrc
echo 'export NODE_ENV=development' >> ~/.zshrc

# Using .env files
NODE_ENV=development npm start
```

### Loading Environment Variables
```javascript
// .env file
NODE_ENV=development
DATABASE_URL=postgresql://localhost:5432/mydb
API_KEY=your-secret-key

// Loading in Node.js
require('dotenv').config();
console.log(process.env.NODE_ENV);
```

## Terminal Customization

### Custom Prompt Configuration

#### PowerShell Prompt
```powershell
# In PowerShell profile
function prompt {
    $location = Get-Location
    $gitBranch = ""
    if (Test-Path .git) {
        $gitBranch = " [$(git branch --show-current)]"
    }
    return "PS $location$gitBranch> "
}
```

#### Bash/Zsh Prompt
```bash
# In ~/.bashrc or ~/.zshrc
PS1='\u@\h:\w$(git branch 2>/dev/null | grep "^*" | cut -d" " -f2 | sed "s/.*/ [&]/")$ '
```

### Terminal Aliases

#### PowerShell Aliases
```powershell
# In PowerShell profile
Set-Alias -Name ll -Value Get-ChildItem
Set-Alias -Name grep -Value Select-String
New-Alias -Name g -Value git

function gst { git status }
function gco { git checkout $args }
function gcm { git commit -m $args }
```

#### Bash/Zsh Aliases
```bash
# In ~/.bashrc or ~/.zshrc
alias ll='ls -la'
alias la='ls -A'
alias l='ls -CF'
alias ..='cd ..'
alias ...='cd ../..'

# Git aliases
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline'
```

## Debugging and Troubleshooting

### Terminal Issues

#### Common Problems
1. **Command not found**
   - Check PATH environment variable
   - Verify software installation
   - Use full path to executable

2. **Permission denied**
   - Use appropriate permissions (chmod on Unix)
   - Run as administrator if needed
   - Check file ownership

3. **Terminal not responding**
   - `Ctrl+C` to interrupt current process
   - `Ctrl+Z` to suspend process
   - Kill terminal and create new one

#### Debugging Commands
```bash
# Check environment
echo $PATH
env | grep NODE
which node
whereis python

# Check running processes
ps aux | grep node
top
htop

# Network debugging
ping google.com
curl -I https://api.example.com
netstat -an | grep :3000
```

### Terminal Performance

#### Optimization Tips
```json
{
  "terminal.integrated.renderer": "auto",
  "terminal.integrated.smoothScrolling": false,
  "terminal.integrated.fastScrollSensitivity": 5,
  "terminal.integrated.scrollback": 1000
}
```

## Practical Exercises

### Exercise 1: Basic Terminal Setup
1. Open integrated terminal
2. Navigate to different directories
3. Create files and folders using command line
4. Practice basic file operations

### Exercise 2: Multiple Terminal Workflow
1. Create 3 different terminals
2. Name them appropriately
3. Run different commands in each
4. Practice switching between terminals

### Exercise 3: Development Workflow
1. Initialize a new Node.js project
2. Install dependencies using npm
3. Create a simple server file
4. Run the server in terminal

### Exercise 4: Git Workflow
1. Initialize a Git repository
2. Create and switch branches
3. Make commits with meaningful messages
4. Practice push/pull operations

## Integration with Editor

### Terminal-Editor Integration

#### Opening Files from Terminal
```bash
# Open file in VS Code
code filename.js
code . # Open current directory

# Open specific line
code filename.js:42

# Compare files
code --diff file1.js file2.js
```

#### Running Scripts
- Click "Run" button in package.json
- Use debug configurations
- Terminal tasks integration

### Tasks Integration
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "npm: start",
      "type": "shell",
      "command": "npm start",
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      }
    }
  ]
}
```

## Security Considerations

### Safe Terminal Practices
1. **Be cautious with scripts** from unknown sources
2. **Verify commands** before running them
3. **Use environment variables** for sensitive data
4. **Don't commit credentials** to version control
5. **Keep tools updated** to latest versions

### Environment Isolation
- Use virtual environments for Python
- Use containers for complex setups
- Separate development and production environments
- Use `.env` files for configuration

## Next Steps

In Episode 8, we'll explore:
- Git integration in VS Code
- Source control panel features
- Branching and merging workflows
- Conflict resolution and collaboration

---

**Previous Episode:** Multi-cursor and Selection  
**Next Episode:** Git Integration  
**Duration:** Approximately 30-35 minutes  
**Prerequisites:** Episodes 1-6 completed