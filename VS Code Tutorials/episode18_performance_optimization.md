# Episode 18 — Performance Optimization & Large Codebases

## Why performance matters
When working with large codebases, VS Code can become slow without proper optimization. This episode covers strategies to keep VS Code responsive and efficient.

## Understanding VS Code performance

### Performance indicators
- **Startup time** - How quickly VS Code launches
- **File operations** - Opening, saving, searching files
- **IntelliSense responsiveness** - Code completion speed
- **Extension overhead** - Impact of installed extensions

### Built-in performance monitoring
Open the Command Palette (`Ctrl+Shift+P`) and run:
- `Developer: Startup Performance` - See startup metrics
- `Developer: Show Running Extensions` - Check extension performance
- `Developer: Reload Window With Extensions Disabled` - Test without extensions

## Optimizing workspace settings

### Exclude unnecessary files
Configure `.vscode/settings.json`:

```json
{
  "files.exclude": {
    "**/node_modules": true,
    "**/bower_components": true,
    "**/.git": true,
    "**/.DS_Store": true,
    "**/tmp": true,
    "**/dist": true,
    "**/build": true,
    "**/*.log": true
  },
  "search.exclude": {
    "**/node_modules": true,
    "**/dist": true,
    "**/build": true,
    "**/*.min.js": true
  },
  "files.watcherExclude": {
    "**/node_modules/**": true,
    "**/dist/**": true,
    "**/build/**": true
  }
}
```

### Limit file watching
```json
{
  "files.watcherExclude": {
    "**/node_modules/**": true,
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true
  }
}
```

## Extension management

### Audit installed extensions
1. Open Extensions view (`Ctrl+Shift+X`)
2. Review enabled extensions
3. Disable unused extensions
4. Use workspace-specific extension recommendations

### Profile extension performance
```bash
# Start VS Code with extension profiling
code --enable-extension-profiler
```

### Use workspace-specific extensions
Create `.vscode/extensions.json`:
```json
{
  "recommendations": [
    "ms-python.python"
  ],
  "unwantedRecommendations": [
    "ms-vscode.vscode-typescript-next"
  ]
}
```

## Language server optimization

### TypeScript/JavaScript performance
```json
{
  "typescript.preferences.includePackageJsonAutoImports": "off",
  "typescript.suggest.autoImports": false,
  "typescript.disableAutomaticTypeAcquisition": true,
  "typescript.preferences.includePackageJsonAutoImports": "off"
}
```

### Python performance
```json
{
  "python.analysis.autoImportCompletions": false,
  "python.analysis.indexing": false,
  "python.analysis.packageIndexDepths": [
    { "name": "", "depth": 2 }
  ]
}
```

## Memory and CPU optimization

### Adjust memory limits
```json
{
  "typescript.tsserver.maxTsServerMemory": 4096,
  "eslint.options": {
    "maxWarnings": 100
  }
}
```

### Control automatic features
```json
{
  "editor.formatOnSave": false,
  "editor.formatOnType": false,
  "editor.codeActionsOnSave": {},
  "editor.suggestOnTriggerCharacters": false
}
```

## Large file handling

### Configure large file thresholds
```json
{
  "workbench.editorAssociations": {
    "*.{csv,log}": "default"
  },
  "files.maxMemoryForLargeFilesMB": 4096
}
```

### Use external tools for large files
- Log files: Use external log viewers
- Data files: Use specialized tools
- Binary files: Configure appropriate viewers

## Search and indexing optimization

### Optimize search settings
```json
{
  "search.smartCase": true,
  "search.useGlobalIgnoreFiles": true,
  "search.useParentIgnoreFiles": true,
  "search.followSymlinks": false
}
```

### Configure ripgrep (VS Code's search engine)
```json
{
  "search.ripgrep.args": [
    "--max-filesize=1M",
    "--type-not",
    "log"
  ]
}
```

## Workspace organization strategies

### Use multi-root workspaces wisely
- Split large monorepos into focused workspaces
- Group related projects logically
- Use workspace-specific settings

### Folder structure best practices
```
project/
├── .vscode/
│   ├── settings.json       # Workspace settings
│   ├── extensions.json     # Recommended extensions
│   └── tasks.json         # Build tasks
├── src/                   # Source code
├── tests/                 # Test files
├── docs/                  # Documentation
└── .gitignore            # Git exclusions
```

## Git performance optimization

### Large repository settings
```json
{
  "git.enabled": true,
  "git.decorations.enabled": false,
  "git.autorefresh": false,
  "git.autofetch": false
}
```

### Use .gitignore effectively
```gitignore
# Dependencies
node_modules/
bower_components/

# Build outputs
dist/
build/
*.min.js
*.min.css

# Logs
*.log
logs/

# OS files
.DS_Store
Thumbs.db
```

## Monitoring and troubleshooting

### Built-in tools
- **Developer Tools**: `Help > Toggle Developer Tools`
- **Process Explorer**: `Help > Open Process Explorer`
- **Performance Profiler**: Available in developer tools

### Command line options
```bash
# Start with specific performance settings
code --max-memory=8192 --disable-gpu

# Profile startup
code --prof-startup

# Verbose logging
code --verbose --log debug
```

## Performance testing checklist

### Regular performance checks
1. ✅ Startup time under 3 seconds
2. ✅ File operations respond quickly
3. ✅ IntelliSense appears within 1 second
4. ✅ Search completes promptly
5. ✅ Extensions don't slow down typing

### When performance degrades
1. Check extension performance
2. Review workspace settings
3. Clear VS Code cache
4. Update VS Code and extensions
5. Consider workspace splitting

## Advanced optimization techniques

### Use VS Code Insiders for latest performance improvements
```bash
# Install VS Code Insiders
winget install Microsoft.VisualStudioCode.Insiders
```

### Custom build configurations
```json
{
  "tasks": [
    {
      "label": "build-fast",
      "type": "shell",
      "command": "npm run build:dev",
      "group": "build",
      "options": {
        "env": {
          "NODE_ENV": "development"
        }
      }
    }
  ]
}
```

## Team optimization strategies

### Shared workspace configuration
Commit `.vscode/` folder with:
- `settings.json` - Performance-optimized settings
- `extensions.json` - Essential extensions only
- `tasks.json` - Optimized build tasks

### Documentation
Create `WORKSPACE.md`:
```markdown
# Workspace Setup

## Required Extensions
- Language support: Python, TypeScript
- Essential tools: GitLens, Prettier

## Performance Settings
- File exclusions configured
- Search optimized for large codebase
- Auto-save disabled for performance
```

## Troubleshooting common issues

### High CPU usage
1. Check running extensions
2. Disable unnecessary language servers
3. Reduce file watching scope

### High memory usage
1. Increase TypeScript memory limit
2. Close unused editor tabs
3. Split large workspaces

### Slow IntelliSense
1. Check language server status
2. Reduce auto-import scope
3. Clear language server cache

Performance optimization is ongoing—regularly review and adjust settings as your codebase grows!