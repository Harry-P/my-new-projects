# Episode 10: Workspace Management

## Overview
Effective workspace management is crucial for organizing projects and maintaining productivity. This episode covers workspace concepts, multi-folder projects, workspace settings, and best practices for project organization.

## Understanding Workspaces

### What is a Workspace?
A workspace in VS Code represents:
- **Single folder** - Basic project setup
- **Multi-root workspace** - Multiple related folders
- **Workspace settings** - Project-specific configurations
- **Extension settings** - Workspace-level extension configuration

### Types of Workspaces

#### Single Folder Workspace
- **Default setup** for most projects
- **Project root** is the opened folder
- **Settings apply** to entire folder tree

#### Multi-Root Workspace
- **Multiple folders** in one workspace
- **Independent projects** or related modules
- **Saved as** `.code-workspace` file

## Single Folder Workspaces

### Opening Folders
- **File > Open Folder** (`Ctrl+K Ctrl+O`)
- **Drag and drop** folder into VS Code
- **Command line:** `code /path/to/project`

### Workspace Structure
```
my-project/                 # Workspace root
├── .vscode/               # VS Code settings
│   ├── settings.json      # Workspace settings
│   ├── launch.json        # Debug configurations
│   ├── tasks.json         # Task definitions
│   └── extensions.json    # Recommended extensions
├── src/                   # Source code
├── docs/                  # Documentation
├── tests/                 # Test files
├── package.json           # Project configuration
└── README.md             # Project documentation
```

### Workspace Root Benefits
- **Relative paths** work consistently
- **IntelliSense** works across all files
- **Search and replace** scoped to project
- **Git integration** for entire project

## Multi-Root Workspaces

### Creating Multi-Root Workspace

#### Method 1: Add Folder to Workspace
1. **Open first folder** normally
2. **File > Add Folder to Workspace**
3. **Select additional folders**
4. **Save workspace** when prompted

#### Method 2: Create Workspace File
1. **File > New Window**
2. **File > Add Folder to Workspace** (repeat)
3. **File > Save Workspace As...**
4. **Choose location** and name

### Workspace Configuration File
```json
{
  "folders": [
    {
      "name": "Frontend",
      "path": "./frontend"
    },
    {
      "name": "Backend API",
      "path": "./backend"
    },
    {
      "name": "Shared Libraries",
      "path": "./shared"
    }
  ],
  "settings": {
    "typescript.preferences.includePackageJsonAutoImports": "on"
  },
  "extensions": {
    "recommendations": [
      "esbenp.prettier-vscode",
      "ms-vscode.vscode-typescript-next"
    ]
  }
}
```

### Multi-Root Use Cases

#### Microservices Architecture
```
my-workspace.code-workspace
├── user-service/
│   ├── src/
│   └── package.json
├── auth-service/
│   ├── src/
│   └── package.json
├── frontend/
│   ├── components/
│   └── package.json
└── shared-types/
    ├── interfaces/
    └── package.json
```

#### Full-Stack Development
```
fullstack-app.code-workspace
├── client/                # React/Vue frontend
├── server/                # Node.js backend
├── mobile/                # React Native app
└── documentation/         # Project docs
```

#### Library Development
```
library-workspace.code-workspace
├── core/                  # Main library
├── plugins/              # Extensions
├── examples/             # Usage examples
└── tests/                # Integration tests
```

## Workspace Settings

### Settings Hierarchy
1. **Default settings** - VS Code defaults
2. **User settings** - Global preferences
3. **Workspace settings** - Project-specific
4. **Folder settings** - Folder-specific (multi-root)

### Workspace Settings File
Location: `.vscode/settings.json`

```json
{
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "files.associations": {
    "*.env": "properties"
  },
  "python.defaultInterpreterPath": "./venv/bin/python",
  "eslint.workingDirectories": ["frontend", "backend"],
  "search.exclude": {
    "**/node_modules": true,
    "**/dist": true,
    "**/.git": true
  }
}
```

### Language-Specific Settings
```json
{
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.tabSize": 2
  },
  "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.tabSize": 4
  },
  "[markdown]": {
    "editor.wordWrap": "on",
    "editor.quickSuggestions": false
  }
}
```

### Extension Settings
```json
{
  "prettier.singleQuote": true,
  "prettier.trailingComma": "es5",
  "eslint.validate": ["javascript", "typescript", "vue"],
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "git.ignoreMissingGitWarning": true
}
```

## Workspace Configuration Files

### Launch Configuration (Debugging)
Location: `.vscode/launch.json`

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug Frontend",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:3000",
      "webRoot": "${workspaceFolder}/src"
    },
    {
      "name": "Debug Backend",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/server.js",
      "env": {
        "NODE_ENV": "development"
      }
    }
  ]
}
```

### Tasks Configuration
Location: `.vscode/tasks.json`

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
    },
    {
      "label": "Run Tests",
      "type": "shell",
      "command": "npm test",
      "group": "test",
      "problemMatcher": ["$tsc"]
    }
  ]
}
```

### Extensions Recommendations
Location: `.vscode/extensions.json`

```json
{
  "recommendations": [
    "esbenp.prettier-vscode",
    "ms-python.python",
    "ms-vscode.vscode-typescript-next",
    "bradlc.vscode-tailwindcss",
    "eamodio.gitlens"
  ],
  "unwantedRecommendations": [
    "ms-vscode.vscode-json"
  ]
}
```

## Project Organization Strategies

### Standard Project Structure

#### Web Development Project
```
web-project/
├── .vscode/
│   ├── settings.json
│   ├── launch.json
│   └── extensions.json
├── src/
│   ├── components/
│   ├── pages/
│   ├── utils/
│   └── styles/
├── public/
│   ├── index.html
│   └── assets/
├── tests/
│   ├── unit/
│   └── integration/
├── docs/
│   ├── README.md
│   └── API.md
├── .gitignore
├── package.json
└── webpack.config.js
```

#### Python Project Structure
```
python-project/
├── .vscode/
│   ├── settings.json
│   └── launch.json
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── modules/
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── docs/
├── requirements.txt
├── setup.py
└── README.md
```

### Configuration Templates

#### Frontend Development Template
```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "emmet.includeLanguages": {
    "javascript": "javascriptreact",
    "typescript": "typescriptreact"
  }
}
```

#### Backend Development Template
```json
{
  "python.defaultInterpreterPath": "./venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "files.associations": {
    "*.env": "properties"
  }
}
```

## Workspace Navigation

### File Explorer Enhancements

#### Custom File Explorer
```json
{
  "explorer.fileNesting.enabled": true,
  "explorer.fileNesting.patterns": {
    "*.ts": "${capture}.js",
    "*.js": "${capture}.js.map, ${capture}.min.js, ${capture}.d.ts",
    "*.jsx": "${capture}.js",
    "*.tsx": "${capture}.ts",
    "tsconfig.json": "tsconfig.*.json",
    "package.json": "package-lock.json, yarn.lock, pnpm-lock.yaml"
  }
}
```

#### Hide/Show Files
```json
{
  "files.exclude": {
    "**/.git": true,
    "**/.svn": true,
    "**/.hg": true,
    "**/CVS": true,
    "**/.DS_Store": true,
    "**/node_modules": true,
    "**/dist": true,
    "**/*.pyc": true
  }
}
```

### Workspace Symbols

#### Go to Symbol in Workspace
- **Shortcut:** `Ctrl+T`
- **Search across** all files in workspace
- **Filter by type** (functions, classes, variables)

#### Symbol Search Examples
```
MyClass          # Find class definitions
@override        # Find decorators
test_           # Find test functions
interface User   # Find TypeScript interfaces
```

## Remote Workspaces

### Remote Development
- **Remote-SSH** - Develop on remote servers
- **Remote-Containers** - Docker container development
- **Remote-WSL** - Windows Subsystem for Linux

### Remote Workspace Benefits
- **Consistent environment** across team
- **Powerful remote machines** for development
- **Isolated development** environments
- **Easy collaboration** on shared resources

### Setting Up Remote Workspace
```json
{
  "remote.SSH.remotePlatform": {
    "myserver": "linux"
  },
  "remote.SSH.defaultExtensions": [
    "ms-python.python",
    "ms-vscode.vscode-typescript-next"
  ]
}
```

## Workspace Collaboration

### Team Settings

#### Shared Workspace Configuration
```json
{
  "folders": [
    {
      "path": "."
    }
  ],
  "settings": {
    "editor.formatOnSave": true,
    "editor.rulers": [80, 120],
    "files.trimTrailingWhitespace": true,
    "files.insertFinalNewline": true
  },
  "extensions": {
    "recommendations": [
      "esbenp.prettier-vscode",
      "dbaeumer.vscode-eslint"
    ]
  }
}
```

#### Code Style Enforcement
```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": true,
    "source.organizeImports": true
  },
  "prettier.requireConfig": true,
  "eslint.validate": ["javascript", "typescript"]
}
```

### Version Control Integration

#### Workspace in Git
```gitignore
# VS Code workspace files
*.code-workspace

# But keep shared configurations
!.vscode/settings.json
!.vscode/launch.json
!.vscode/tasks.json
!.vscode/extensions.json
```

## Advanced Workspace Features

### Workspace Trust

#### Trusted Workspaces
- **Security feature** for unknown code
- **Restricted mode** for untrusted workspaces
- **Full functionality** in trusted workspaces

#### Trust Configuration
```json
{
  "security.workspace.trust.enabled": true,
  "security.workspace.trust.startupPrompt": "always",
  "security.workspace.trust.banner": "always"
}
```

### Workspace State

#### Preserving Workspace State
- **Open tabs** and editor layout
- **Panel visibility** and sizes
- **Search history** and filters
- **Debug configurations** and breakpoints

#### State Management
```json
{
  "workbench.editor.restoreViewState": true,
  "workbench.editor.wrapTabs": true,
  "workbench.startupEditor": "welcomePageInEmptyWorkspaces"
}
```

## Practical Exercises

### Exercise 1: Single Folder Workspace
1. Create a new project folder
2. Set up workspace-specific settings
3. Configure debug and task configurations
4. Add recommended extensions

### Exercise 2: Multi-Root Workspace
1. Create multiple related project folders
2. Add them to a multi-root workspace
3. Configure folder-specific settings
4. Save and organize the workspace

### Exercise 3: Project Templates
1. Create configuration templates for different project types
2. Set up standardized folder structures
3. Create reusable settings configurations
4. Test with new projects

### Exercise 4: Team Collaboration Setup
1. Configure shared workspace settings
2. Set up extension recommendations
3. Create standardized debug configurations
4. Test collaboration features

## Workspace Management Best Practices

### Organization Tips
1. **Use consistent** folder structures
2. **Create templates** for common project types
3. **Document workspace** setup in README
4. **Version control** shared configurations
5. **Regular cleanup** of unused workspaces

### Performance Optimization
```json
{
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/node_modules/**": true,
    "**/dist/**": true
  },
  "search.exclude": {
    "**/node_modules": true,
    "**/bower_components": true,
    "**/*.code-search": true
  }
}
```

### Security Considerations
1. **Review workspace trust** settings
2. **Avoid sensitive data** in settings
3. **Use environment variables** for secrets
4. **Careful with** extension recommendations
5. **Regular security** updates

## Troubleshooting Workspace Issues

### Common Problems

#### Settings Not Applied
1. **Check settings hierarchy** (user vs workspace)
2. **Verify JSON syntax** in settings files
3. **Restart VS Code** to apply changes
4. **Check extension** requirements

#### Multi-Root Issues
1. **Verify folder paths** in workspace file
2. **Check relative path** resolution
3. **Update workspace file** manually if needed
4. **Recreate workspace** if corrupted

#### Performance Issues
1. **Exclude large directories** from file watching
2. **Limit search scope** with patterns
3. **Close unused** workspace folders
4. **Monitor extension** performance impact

## Next Steps

In Episode 11, we'll explore:
- Customizing VS Code appearance
- Installing and configuring themes
- Icon themes and customization
- Layout and UI personalization

---

**Previous Episode:** Debugging Basics  
**Next Episode:** Themes and Customization  
**Duration:** Approximately 30-35 minutes  
**Prerequisites:** Episodes 1-9 completed