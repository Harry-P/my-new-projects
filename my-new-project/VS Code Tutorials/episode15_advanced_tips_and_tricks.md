# Episode 15: Advanced Tips and Tricks

## Overview
This final episode covers advanced VS Code features, productivity tips, hidden gems, and power-user techniques that can take your development workflow to the next level. We'll explore lesser-known features and advanced customizations.

## Advanced Editor Features

### Sticky Scroll
Keep context visible while scrolling through long files:

```json
{
  "editor.stickyScroll.enabled": true,
  "editor.stickyScroll.maxLineCount": 5
}
```

### Advanced IntelliSense

#### Trigger Suggest with Specific Characters
```json
{
  "editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": true
  },
  "editor.suggestOnTriggerCharacters": true,
  "editor.acceptSuggestionOnEnter": "smart"
}
```

#### Parameter Hints Enhancement
```json
{
  "editor.parameterHints.enabled": true,
  "editor.parameterHints.cycle": true
}
```

### Advanced Text Selection

#### Column Selection with Keyboard
- **Shift+Alt+Ctrl+Arrow Keys** - Create column selection
- **Shift+Alt+Ctrl+PageUp/PageDown** - Extend column selection

#### Smart Selection
```json
{
  "editor.smartSelect.selectLeadingAndTrailingWhitespace": false
}
```

### Advanced Code Folding

#### Custom Folding Regions
```javascript
// #region Helper Functions
function utility1() {
  // implementation
}

function utility2() {
  // implementation
}
// #endregion

// #region Main Logic
function mainFunction() {
  // implementation
}
// #endregion
```

#### Folding Configuration
```json
{
  "editor.foldingStrategy": "indentation",
  "editor.foldingHighlight": true,
  "editor.showFoldingControls": "mouseover",
  "editor.foldingImportsByDefault": true
}
```

## Advanced Search and Replace

### Regular Expression Power Features

#### Lookahead and Lookbehind
```regex
# Positive lookahead - find "function" followed by "test"
function(?=.*test)

# Negative lookahead - find "function" NOT followed by "test"
function(?!.*test)

# Positive lookbehind - find "test" preceded by "function"
(?<=function.*)test

# Negative lookbehind - find "test" NOT preceded by "function"
(?<!function.*)test
```

#### Advanced Capture Groups
```regex
# Named capture groups
(?<method>get|post|put|delete)\s+['"](?<path>[^'"]+)['"]

# Replace with named groups
app.${method}('${path}', handler);
```

### Search Scope Optimization

#### Advanced File Patterns
```json
{
  "search.include": {
    "src/**/*.{js,ts,jsx,tsx}": true,
    "tests/**/*.test.*": true
  },
  "search.exclude": {
    "**/node_modules": true,
    "**/dist": true,
    "**/*.min.js": true,
    "**/coverage": true
  }
}
```

## Advanced Debugging Techniques

### Conditional Breakpoints with Complex Logic

#### JavaScript Debugging
```javascript
// Conditional breakpoint: users.length > 5 && user.role === 'admin'
function processUsers(users) {
  users.forEach(user => {
    // Breakpoint hits only when condition is true
    processUser(user);
  });
}
```

#### Data Breakpoints
- Set breakpoints on **variable changes**
- Monitor **object property** modifications
- Track **array mutations**

### Advanced Debug Configuration

#### Compound Configurations
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Launch Frontend",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:3000"
    },
    {
      "name": "Launch Backend",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/server.js"
    }
  ],
  "compounds": [
    {
      "name": "Launch Full Stack",
      "configurations": ["Launch Frontend", "Launch Backend"],
      "stopAll": true
    }
  ]
}
```

#### Debug with External Tools
```json
{
  "name": "Debug with Docker",
  "type": "node",
  "request": "attach",
  "port": 9229,
  "address": "localhost",
  "localRoot": "${workspaceFolder}",
  "remoteRoot": "/app",
  "protocol": "inspector"
}
```

## Advanced Workspace Management

### Multi-Root Workspace Advanced Features

#### Folder-Specific Settings
```json
{
  "folders": [
    {
      "name": "Frontend",
      "path": "./client"
    },
    {
      "name": "Backend",
      "path": "./server"
    }
  ],
  "settings": {
    "search.exclude": {
      "**/node_modules": true
    }
  },
  "extensions": {
    "recommendations": [
      "esbenp.prettier-vscode"
    ]
  }
}
```

#### Task Dependencies
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Build Backend",
      "type": "shell",
      "command": "npm run build",
      "options": {
        "cwd": "${workspaceFolder}/server"
      }
    },
    {
      "label": "Build Frontend", 
      "type": "shell",
      "command": "npm run build",
      "options": {
        "cwd": "${workspaceFolder}/client"
      },
      "dependsOn": "Build Backend"
    }
  ]
}
```

### Advanced File Watching

#### Custom File Watchers
```json
{
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/node_modules/**": true,
    "**/tmp/**": true,
    "**/.hg/store/**": true
  },
  "files.watcherInclude": [
    "**/*.config.js",
    "**/*.env*"
  ]
}
```

## Advanced Terminal Usage

### Terminal Profiles and Automation

#### Custom Terminal Profiles
```json
{
  "terminal.integrated.profiles.windows": {
    "PowerShell Dev": {
      "source": "PowerShell",
      "args": ["-NoProfile", "-ExecutionPolicy", "Bypass"],
      "env": {
        "NODE_ENV": "development"
      }
    },
    "Git Bash": {
      "path": "C:\\Program Files\\Git\\bin\\bash.exe",
      "args": ["--login"]
    }
  }
}
```

#### Terminal Automation
```json
{
  "terminal.integrated.automationShell.windows": "pwsh.exe",
  "terminal.integrated.automationShell.linux": "/bin/bash"
}
```

### Advanced Shell Integration

#### Command Decorations
```json
{
  "terminal.integrated.shellIntegration.decorationsEnabled": true,
  "terminal.integrated.shellIntegration.history": 100
}
```

#### Terminal Link Providers
- **File links** with line numbers
- **URL detection** and opening
- **Custom link patterns**

## Advanced Git Integration

### Git Lens Advanced Features

#### Custom Git Blame Format
```json
{
  "gitlens.blame.format": "${author|10} ${agoOrDate|14-}",
  "gitlens.blame.avatars": true,
  "gitlens.blame.compact": false,
  "gitlens.blame.dateFormat": "MMMM Do, YYYY h:mma"
}
```

#### File Annotations
```json
{
  "gitlens.codeLens.authors.enabled": true,
  "gitlens.codeLens.recentChange.enabled": true,
  "gitlens.currentLine.enabled": true,
  "gitlens.currentLine.pullRequests.enabled": true
}
```

### Advanced Git Workflows

#### Interactive Rebase in VS Code
1. **Open Git Graph** (GitLens extension)
2. **Right-click commits** for rebase options
3. **Squash, edit, drop** commits visually
4. **Resolve conflicts** inline

#### Cherry-Pick Workflows
```bash
# Command palette approach
# Git: Cherry Pick...
# Select commit hash
# Resolve conflicts if any
```

## Advanced Extension Development

### Creating Simple Extensions

#### Basic Extension Structure
```javascript
// extension.js
const vscode = require('vscode');

function activate(context) {
  let disposable = vscode.commands.registerCommand('extension.helloWorld', function () {
    vscode.window.showInformationMessage('Hello World from VS Code!');
  });
  
  context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
  activate,
  deactivate
};
```

#### Package.json Configuration
```json
{
  "name": "my-extension",
  "displayName": "My Extension",
  "description": "A simple VS Code extension",
  "version": "0.0.1",
  "engines": {
    "vscode": "^1.74.0"
  },
  "categories": ["Other"],
  "activationEvents": [],
  "main": "./extension.js",
  "contributes": {
    "commands": [
      {
        "command": "extension.helloWorld",
        "title": "Hello World"
      }
    ]
  }
}
```

### Advanced Extension Features

#### Custom Views and Panels
```javascript
class CustomViewProvider {
  constructor(context) {
    this._view = undefined;
    this._context = context;
  }
  
  resolveWebviewView(webviewView) {
    this._view = webviewView;
    
    webviewView.webview.options = {
      enableScripts: true,
      localResourceRoots: [this._context.extensionUri]
    };
    
    webviewView.webview.html = this._getHtmlContent();
  }
  
  _getHtmlContent() {
    return `<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Custom View</title>
    </head>
    <body>
        <h1>Custom Extension View</h1>
        <button onclick="sendMessage()">Click me!</button>
    </body>
    </html>`;
  }
}
```

## Performance Optimization

### VS Code Performance Tuning

#### Memory and CPU Optimization
```json
{
  "extensions.autoUpdate": false,
  "extensions.autoCheckUpdates": false,
  "workbench.enableExperiments": false,
  "telemetry.telemetryLevel": "off",
  "search.maintainFileSearchCache": true,
  "search.maxResults": 20000
}
```

#### Large File Handling
```json
{
  "editor.largeFileOptimizations": true,
  "diffEditor.maxFileSize": 50,
  "files.maxMemoryForLargeFilesMB": 4096
}
```

### Extension Performance

#### Monitoring Extension Performance
1. **Help > Developer Tools**
2. **Console tab**
3. **Type:** `code --status`
4. **Review extension** startup times

#### Performance-Focused Settings
```json
{
  "extensions.experimental.affinity": {
    "vscodevim.vim": 1,
    "ms-python.python": 2
  }
}
```

## Advanced Customization

### CSS Customization with Extensions

#### Custom CSS and JS Loader
1. **Install** "Custom CSS and JS Loader" extension
2. **Create custom** CSS file
3. **Apply styles** to VS Code interface

```css
/* custom-vscode.css */
.monaco-workbench .part.editor > .content .editor-group-container > .title .tabs-container > .tab {
  background: linear-gradient(45deg, #ff6b6b, #4ecdc4) !important;
}

.monaco-editor .current-line {
  background-color: rgba(255, 255, 255, 0.1) !important;
}
```

### Advanced Theming

#### Creating Custom Color Themes
```json
{
  "name": "My Custom Theme",
  "type": "dark",
  "colors": {
    "editor.background": "#1a1a1a",
    "editor.foreground": "#d4d4d4",
    "activityBar.background": "#2d2d30",
    "sideBar.background": "#252526",
    "statusBar.background": "#007acc",
    "titleBar.activeBackground": "#3c3c3c"
  },
  "tokenColors": [
    {
      "scope": ["comment", "punctuation.definition.comment"],
      "settings": {
        "fontStyle": "italic",
        "foreground": "#6A9955"
      }
    },
    {
      "scope": ["keyword", "storage.type", "storage.modifier"],
      "settings": {
        "foreground": "#569cd6"
      }
    }
  ]
}
```

## Hidden Features and Easter Eggs

### Command Palette Power Features

#### Advanced Command Usage
```
# Search with prefixes
> - Show and run commands
@ - Go to symbol in file
# - Go to symbol by category
: - Go to line number
? - Get help on command palette
```

#### Workspace Symbol Search
```
# Search all symbols in workspace
Ctrl+T then type:
MyClass - Find all classes named MyClass
@method - Find all methods
#interface - Find all interfaces
```

### Secret Commands

#### Accessible through Command Palette
- **Developer: Inspect Editor Tokens and Scopes**
- **Developer: Set Log Level**
- **Workbench: Export Data**
- **Developer: Startup Performance**

### Advanced File Operations

#### Quick Open Power Features
```
# Ctrl+P then:
filename.js - Open file
filename.js:42 - Open file at line 42
filename.js:42:5 - Open file at line 42, column 5
filename.js@symbol - Open file and go to symbol
```

## Productivity Workflows

### Automation with Tasks

#### Complex Task Workflows
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Full Development Setup",
      "dependsOrder": "sequence",
      "dependsOn": [
        "Install Dependencies",
        "Setup Database",
        "Start Services"
      ]
    },
    {
      "label": "Install Dependencies",
      "type": "shell",
      "command": "npm install",
      "group": "build"
    },
    {
      "label": "Setup Database",
      "type": "shell",
      "command": "npm run db:setup",
      "group": "build"
    },
    {
      "label": "Start Services",
      "type": "shell",
      "command": "npm run dev",
      "group": "build",
      "isBackground": true
    }
  ]
}
```

### Macro-like Keybindings

#### Complex Command Sequences
```json
{
  "key": "ctrl+alt+d",
  "command": "runCommands",
  "args": {
    "commands": [
      "editor.action.selectAll",
      "editor.action.formatDocument",
      "workbench.action.files.save",
      "workbench.action.closeActiveEditor"
    ]
  }
}
```

## Advanced Collaboration

### Live Share Advanced Features

#### Custom Live Share Settings
```json
{
  "liveshare.account": "user@example.com",
  "liveshare.autoShareServers": true,
  "liveshare.autoShareTerminals": true,
  "liveshare.guestApprovalRequired": false
}
```

### Code Review Workflows

#### GitHub Pull Requests Extension
- **Inline comments** and reviews
- **Diff viewing** and navigation
- **Merge conflict** resolution
- **CI/CD status** integration

## Practical Exercises

### Exercise 1: Advanced Debugging Setup
1. Create a complex debug configuration with multiple targets
2. Set up conditional breakpoints with complex logic
3. Use data breakpoints to monitor variable changes
4. Test remote debugging capabilities

### Exercise 2: Custom Extension Development
1. Create a simple extension with custom commands
2. Add a custom view provider
3. Implement extension settings
4. Test and package the extension

### Exercise 3: Performance Optimization
1. Analyze VS Code performance with large projects
2. Optimize settings for better performance
3. Profile extension impact
4. Implement workspace-specific optimizations

### Exercise 4: Advanced Workflow Automation
1. Create complex task dependencies
2. Set up automated development environment setup
3. Implement custom keybinding macros
4. Test workflow efficiency improvements

## Power User Tips

### Daily Workflow Optimizations

#### Morning Setup Routine
```json
{
  "key": "ctrl+alt+m",
  "command": "runCommands",
  "args": {
    "commands": [
      "workbench.action.openFolder",
      "git.pull",
      "workbench.action.terminal.new",
      "npm start"
    ]
  }
}
```

#### Code Review Shortcuts
```json
{
  "key": "ctrl+alt+r",
  "command": "pr.create",
  "when": "gitOpenRepositoryCount != 0"
}
```

### Advanced Navigation

#### Workspace Navigation
- **Ctrl+R** - Switch between recent workspaces
- **Ctrl+K Ctrl+O** - Open folder in new window
- **Ctrl+Shift+N** - New window

#### Symbol Navigation
- **Ctrl+Shift+O** - Go to symbol in file
- **Ctrl+T** - Go to symbol in workspace
- **F12** - Go to definition
- **Alt+F12** - Peek definition

## Troubleshooting Advanced Issues

### Performance Debugging

#### Identifying Slow Extensions
```bash
# Command line flag to profile startup
code --prof-startup
```

#### Memory Usage Analysis
1. **Help > Developer Tools**
2. **Memory tab**
3. **Take heap snapshot**
4. **Analyze memory usage**

### Configuration Conflicts

#### Settings Precedence
1. **Default settings**
2. **User settings**
3. **Workspace settings**
4. **Folder settings** (multi-root)

#### Extension Conflicts
1. **Disable extensions** one by one
2. **Check extension** output logs
3. **Review settings** conflicts
4. **Test in safe mode**

## Future-Proofing Your Setup

### Staying Updated

#### Beta and Insider Versions
- **VS Code Insiders** - Latest features
- **Extension pre-releases** - Early access
- **Feature flags** and experiments

#### Following VS Code Development
- **VS Code Blog** - Feature announcements
- **GitHub Repository** - Issue tracking
- **Release Notes** - Detailed changes
- **Community Forums** - Tips and tricks

### Backup and Migration

#### Settings Sync
```json
{
  "settingsSync.ignoredExtensions": [
    "ms-vscode.vscode-typescript-next"
  ],
  "settingsSync.ignoredSettings": [
    "workbench.colorTheme"
  ]
}
```

#### Manual Backup
- **Export settings** regularly
- **Document custom** configurations
- **Version control** workspace settings
- **Test restoration** process

## Conclusion

Congratulations! You've completed the comprehensive VS Code tutorial series. You now have the knowledge and skills to:

- **Master the fundamentals** of VS Code
- **Leverage advanced features** for productivity
- **Customize your environment** to fit your workflow
- **Collaborate effectively** with teams
- **Debug complex applications** efficiently
- **Develop and manage** remote environments
- **Create custom extensions** and automations

### Next Steps
1. **Practice regularly** with these advanced techniques
2. **Experiment with** new extensions and features
3. **Join the VS Code** community for continued learning
4. **Share your knowledge** with other developers
5. **Stay updated** with the latest VS Code developments

### Resources for Continued Learning
- **VS Code Documentation** - https://code.visualstudio.com/docs
- **VS Code Tips and Tricks** - https://code.visualstudio.com/docs/getstarted/tips-and-tricks
- **Extension Marketplace** - https://marketplace.visualstudio.com/
- **VS Code GitHub** - https://github.com/microsoft/vscode
- **Community Forums** - https://github.com/microsoft/vscode/discussions

---

**Previous Episode:** Remote Development  
**Series Complete!**  
**Duration:** Approximately 40-45 minutes  
**Prerequisites:** Episodes 1-14 completed

**Total Series Duration:** Approximately 7-8 hours of comprehensive VS Code training!