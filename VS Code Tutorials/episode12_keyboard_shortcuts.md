# Episode 12: Keyboard Shortcuts

## Overview
Mastering keyboard shortcuts is one of the most effective ways to boost your productivity in VS Code. This episode covers essential shortcuts, creating custom keybindings, and developing efficient keyboard-driven workflows.

## Essential Keyboard Shortcuts

### Basic Navigation

#### File Operations
| Action | Windows/Linux | macOS | Description |
|--------|---------------|-------|-------------|
| New File | `Ctrl+N` | `Cmd+N` | Create new file |
| Open File | `Ctrl+O` | `Cmd+O` | Open existing file |
| Save File | `Ctrl+S` | `Cmd+S` | Save current file |
| Save As | `Ctrl+Shift+S` | `Cmd+Shift+S` | Save with new name |
| Save All | `Ctrl+K S` | `Cmd+Option+S` | Save all open files |
| Close File | `Ctrl+W` | `Cmd+W` | Close current tab |
| Reopen Closed Tab | `Ctrl+Shift+T` | `Cmd+Shift+T` | Reopen last closed tab |

#### Quick Navigation
| Action | Windows/Linux | macOS | Description |
|--------|---------------|-------|-------------|
| Quick Open | `Ctrl+P` | `Cmd+P` | Open file by name |
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` | Access all commands |
| Go to Line | `Ctrl+G` | `Cmd+G` | Jump to specific line |
| Go to Symbol | `Ctrl+Shift+O` | `Cmd+Shift+O` | Navigate to symbols |
| Go to Symbol (Workspace) | `Ctrl+T` | `Cmd+T` | Find symbols across files |

### Editor Navigation

#### Cursor Movement
| Action | Windows/Linux | macOS | Description |
|--------|---------------|-------|-------------|
| Move by Word | `Ctrl+Left/Right` | `Option+Left/Right` | Jump between words |
| Line Start/End | `Home/End` | `Cmd+Left/Right` | Beginning/end of line |
| File Start/End | `Ctrl+Home/End` | `Cmd+Up/Down` | Top/bottom of file |
| Go to Matching Bracket | `Ctrl+Shift+\\` | `Cmd+Shift+\\` | Jump to matching bracket |
| Scroll Line Up/Down | `Ctrl+Up/Down` | `Cmd+Up/Down` | Scroll without moving cursor |

#### Text Selection
| Action | Windows/Linux | macOS | Description |
|--------|---------------|-------|-------------|
| Select All | `Ctrl+A` | `Cmd+A` | Select entire document |
| Select Line | `Ctrl+L` | `Cmd+L` | Select current line |
| Select Word | `Ctrl+D` | `Cmd+D` | Select word/next occurrence |
| Select All Occurrences | `Ctrl+Shift+L` | `Cmd+Shift+L` | Select all occurrences |
| Expand Selection | `Shift+Alt+Right` | `Shift+Option+Right` | Smart selection expansion |
| Shrink Selection | `Shift+Alt+Left` | `Shift+Option+Left` | Smart selection shrinking |

### Editing Shortcuts

#### Basic Editing
| Action | Windows/Linux | macOS | Description |
|--------|---------------|-------|-------------|
| Copy Line | `Ctrl+C` | `Cmd+C` | Copy current line |
| Cut Line | `Ctrl+X` | `Cmd+X` | Cut current line |
| Duplicate Line | `Shift+Alt+Down` | `Shift+Option+Down` | Duplicate current line |
| Move Line Up/Down | `Alt+Up/Down` | `Option+Up/Down` | Move line up or down |
| Delete Line | `Ctrl+Shift+K` | `Cmd+Shift+K` | Delete entire line |
| Insert Line Below | `Ctrl+Enter` | `Cmd+Enter` | New line below cursor |
| Insert Line Above | `Ctrl+Shift+Enter` | `Cmd+Shift+Enter` | New line above cursor |

#### Advanced Editing
| Action | Windows/Linux | macOS | Description |
|--------|---------------|-------|-------------|
| Toggle Comment | `Ctrl+/` | `Cmd+/` | Comment/uncomment line |
| Block Comment | `Shift+Alt+A` | `Shift+Option+A` | Toggle block comment |
| Format Document | `Shift+Alt+F` | `Shift+Option+F` | Format entire document |
| Format Selection | `Ctrl+K Ctrl+F` | `Cmd+K Cmd+F` | Format selected code |
| Indent/Outdent | `Ctrl+]/[` | `Cmd+]/[` | Adjust indentation |

### Multi-cursor Shortcuts

#### Adding Cursors
| Action | Windows/Linux | macOS | Description |
|--------|---------------|-------|-------------|
| Add Cursor | `Alt+Click` | `Option+Click` | Add cursor at click position |
| Add Cursor Above/Below | `Ctrl+Alt+Up/Down` | `Cmd+Option+Up/Down` | Column cursor addition |
| Select Next Occurrence | `Ctrl+D` | `Cmd+D` | Add cursor to next match |
| Select All Occurrences | `Ctrl+F2` | `Cmd+F2` | Add cursors to all matches |
| Undo Last Cursor | `Ctrl+U` | `Cmd+U` | Remove last cursor |

## Search and Replace Shortcuts

### Search Operations
| Action | Windows/Linux | macOS | Description |
|--------|---------------|-------|-------------|
| Find | `Ctrl+F` | `Cmd+F` | Find in current file |
| Find Next/Previous | `F3/Shift+F3` | `Cmd+G/Cmd+Shift+G` | Navigate search results |
| Find in Files | `Ctrl+Shift+F` | `Cmd+Shift+F` | Search across workspace |
| Replace | `Ctrl+H` | `Cmd+Option+F` | Find and replace |
| Replace in Files | `Ctrl+Shift+H` | `Cmd+Shift+H` | Global find and replace |

### Advanced Search
| Action | Windows/Linux | macOS | Description |
|--------|---------------|-------|-------------|
| Find with Selection | `Ctrl+F3` | `Cmd+E` | Find selected text |
| Toggle Case Sensitive | `Alt+C` | `Cmd+Option+C` | Case-sensitive search |
| Toggle Regex | `Alt+R` | `Cmd+Option+R` | Regular expression mode |
| Toggle Whole Word | `Alt+W` | `Cmd+Option+W` | Whole word matching |

## Panel and View Shortcuts

### Panel Management
| Action | Windows/Linux | macOS | Description |
|--------|---------------|-------|-------------|
| Toggle Sidebar | `Ctrl+B` | `Cmd+B` | Show/hide sidebar |
| Toggle Panel | `Ctrl+J` | `Cmd+J` | Show/hide bottom panel |
| Toggle Terminal | `Ctrl+`` | `Cmd+`` | Show/hide terminal |
| Explorer Focus | `Ctrl+Shift+E` | `Cmd+Shift+E` | Focus file explorer |
| Search Focus | `Ctrl+Shift+F` | `Cmd+Shift+F` | Focus search panel |
| Source Control | `Ctrl+Shift+G` | `Cmd+Shift+G` | Focus source control |
| Debug Panel | `Ctrl+Shift+D` | `Cmd+Shift+D` | Focus debug panel |
| Extensions | `Ctrl+Shift+X` | `Cmd+Shift+X` | Focus extensions panel |

### Editor Management
| Action | Windows/Linux | macOS | Description |
|--------|---------------|-------|-------------|
| Split Editor | `Ctrl+\\` | `Cmd+\\` | Split editor vertically |
| Close Editor Group | `Ctrl+K W` | `Cmd+K W` | Close editor group |
| Focus Editor Groups | `Ctrl+1/2/3` | `Cmd+1/2/3` | Switch between groups |
| Move Tab to Group | `Ctrl+Alt+Right/Left` | `Cmd+Option+Right/Left` | Move tab between groups |

## Custom Keybindings

### Accessing Keybinding Settings
1. **Open Command Palette** (`Ctrl+Shift+P`)
2. **Type** "Preferences: Open Keyboard Shortcuts"
3. **Or use** `Ctrl+K Ctrl+S`

### Keybinding Configuration

#### Basic Custom Keybinding
```json
{
  "key": "ctrl+shift+r",
  "command": "workbench.action.reloadWindow"
}
```

#### Conditional Keybinding
```json
{
  "key": "ctrl+enter",
  "command": "editor.action.insertLineAfter",
  "when": "editorTextFocus && !editorReadonly"
}
```

#### Multiple Commands
```json
{
  "key": "ctrl+k ctrl+d",
  "command": "runCommands",
  "args": {
    "commands": [
      "editor.action.copyLinesDownAction",
      "editor.action.commentLine"
    ]
  }
}
```

### Common Custom Keybindings

#### Quick File Operations
```json
[
  {
    "key": "ctrl+n",
    "command": "explorer.newFile",
    "when": "explorerViewletFocus"
  },
  {
    "key": "ctrl+shift+n",
    "command": "explorer.newFolder",
    "when": "explorerViewletFocus"
  },
  {
    "key": "delete",
    "command": "deleteFile",
    "when": "explorerViewletFocus && !inputFocus"
  }
]
```

#### Development Shortcuts
```json
[
  {
    "key": "f5",
    "command": "workbench.action.debug.start",
    "when": "!inDebugMode"
  },
  {
    "key": "ctrl+f5",
    "command": "workbench.action.debug.run",
    "when": "!inDebugMode"
  },
  {
    "key": "ctrl+shift+`",
    "command": "workbench.action.terminal.new"
  }
]
```

#### Text Transformation
```json
[
  {
    "key": "ctrl+u",
    "command": "editor.action.transformToUppercase"
  },
  {
    "key": "ctrl+shift+u",
    "command": "editor.action.transformToLowercase"
  },
  {
    "key": "ctrl+alt+t",
    "command": "editor.action.transformToTitlecase"
  }
]
```

## Context-Specific Shortcuts

### When Conditions
Common `when` clause contexts:

#### Editor Context
```json
"when": "editorTextFocus"                    // Editor has focus
"when": "editorHasSelection"                 // Text is selected
"when": "editorReadonly"                     // Editor is read-only
"when": "editorLangId == javascript"         // Specific language
"when": "editorTextFocus && !editorReadonly" // Editable editor focused
```

#### Explorer Context
```json
"when": "explorerViewletFocus"               // Explorer panel focused
"when": "explorerViewletVisible"             // Explorer panel visible
"when": "filesExplorerFocus"                 // File explorer focused
```

#### Debug Context
```json
"when": "inDebugMode"                        // Debug session active
"when": "debugState == 'stopped'"           // Debugger stopped at breakpoint
"when": "debugType == 'node'"               // Node.js debugging
```

### Language-Specific Shortcuts

#### JavaScript/TypeScript
```json
[
  {
    "key": "ctrl+shift+i",
    "command": "typescript.organizeImports",
    "when": "editorLangId == typescript || editorLangId == javascript"
  },
  {
    "key": "f12",
    "command": "editor.action.revealDefinition",
    "when": "editorLangId == typescript || editorLangId == javascript"
  }
]
```

#### Python
```json
[
  {
    "key": "ctrl+shift+p",
    "command": "python.execInTerminal",
    "when": "editorLangId == python"
  },
  {
    "key": "f5",
    "command": "python.debugInTerminal",
    "when": "editorLangId == python"
  }
]
```

## Advanced Shortcut Techniques

### Chord Keybindings

#### Multi-step Shortcuts
```json
{
  "key": "ctrl+k ctrl+s",
  "command": "workbench.action.openGlobalKeybindings"
}
```

#### Custom Chord Sequences
```json
[
  {
    "key": "ctrl+k ctrl+t",
    "command": "workbench.action.selectTheme"
  },
  {
    "key": "ctrl+k ctrl+f",
    "command": "workbench.action.openFolder"
  }
]
```

### Macro-like Combinations

#### Complex Text Operations
```json
{
  "key": "ctrl+shift+d",
  "command": "runCommands",
  "args": {
    "commands": [
      "editor.action.copyLinesDownAction",
      "cursorDown",
      "editor.action.commentLine"
    ]
  }
}
```

#### Workflow Shortcuts
```json
{
  "key": "ctrl+alt+g",
  "command": "runCommands",
  "args": {
    "commands": [
      "git.add",
      "git.commit",
      "workbench.view.scm"
    ]
  }
}
```

## Workflow-Specific Shortcuts

### Git Workflow
```json
[
  {
    "key": "ctrl+shift+g g",
    "command": "git.stage"
  },
  {
    "key": "ctrl+shift+g c",
    "command": "git.commit"
  },
  {
    "key": "ctrl+shift+g p",
    "command": "git.push"
  },
  {
    "key": "ctrl+shift+g l",
    "command": "git.pull"
  }
]
```

### Testing Workflow
```json
[
  {
    "key": "ctrl+shift+t",
    "command": "workbench.action.tasks.test"
  },
  {
    "key": "ctrl+shift+r",
    "command": "workbench.action.reloadWindow"
  }
]
```

### Debugging Workflow
```json
[
  {
    "key": "f5",
    "command": "workbench.action.debug.start"
  },
  {
    "key": "shift+f5",
    "command": "workbench.action.debug.stop"
  },
  {
    "key": "f9",
    "command": "editor.debug.action.toggleBreakpoint"
  },
  {
    "key": "f10",
    "command": "workbench.action.debug.stepOver"
  },
  {
    "key": "f11",
    "command": "workbench.action.debug.stepInto"
  }
]
```

## Practical Exercises

### Exercise 1: Basic Shortcuts Mastery
1. Practice essential navigation shortcuts for 10 minutes
2. Use only keyboard for file operations
3. Practice multi-cursor editing techniques
4. Time yourself performing common tasks

### Exercise 2: Custom Keybinding Creation
1. Identify 3 frequently used commands
2. Create custom shortcuts for these commands
3. Practice using the new shortcuts
4. Refine based on muscle memory

### Exercise 3: Workflow Optimization
1. Analyze your typical coding workflow
2. Identify repetitive action sequences
3. Create macro-like keybindings for workflows
4. Test and adjust for efficiency

### Exercise 4: Language-Specific Setup
1. Research shortcuts for your primary language
2. Set up language-specific keybindings
3. Create shortcuts for common language tasks
4. Practice language-specific workflows

## Memorization Strategies

### Learning Approach
1. **Start with most frequent** actions
2. **Practice daily** for muscle memory
3. **Use shortcuts consistently** instead of mouse
4. **Group related shortcuts** for learning
5. **Print reference cards** for desk reference

### Shortcuts by Frequency

#### Daily Use (Memorize First)
- `Ctrl+S` (Save)
- `Ctrl+P` (Quick Open)
- `Ctrl+Shift+P` (Command Palette)
- `Ctrl+F` (Find)
- `Ctrl+D` (Select Next)

#### Weekly Use (Secondary Priority)
- `Ctrl+Shift+F` (Find in Files)
- `Alt+Up/Down` (Move Lines)
- `Shift+Alt+F` (Format Document)
- `Ctrl+G` (Go to Line)

#### Occasional Use (Learn Gradually)
- `Ctrl+K Ctrl+F` (Format Selection)
- `Ctrl+Shift+O` (Go to Symbol)
- `Shift+Alt+A` (Block Comment)

## Troubleshooting Shortcuts

### Common Issues

#### Shortcut Not Working
1. **Check for conflicts** with other applications
2. **Verify when conditions** are met
3. **Test in different contexts**
4. **Check extension conflicts**

#### Keybinding Conflicts
```json
// Remove conflicting keybinding
{
  "key": "ctrl+shift+r",
  "command": "-workbench.action.quickOpenNavigateNextInRecentFilesPicker"
}
```

#### System Shortcuts Override
- **Windows:** Check system keyboard shortcuts
- **macOS:** Check system preferences
- **Linux:** Check desktop environment shortcuts

### Reset and Backup

#### Reset Keybindings
1. **Command Palette** > "Preferences: Open Keyboard Shortcuts (JSON)"
2. **Delete custom** keybindings
3. **Restart VS Code**

#### Backup Keybindings
```json
// Export your keybindings.json
[
  {
    "key": "ctrl+shift+r",
    "command": "workbench.action.reloadWindow"
  }
  // ... your custom keybindings
]
```

## Performance and Efficiency

### Measuring Improvement
- **Time common tasks** before and after
- **Count mouse clicks** reduced
- **Track workflow** efficiency
- **Monitor typing** speed improvements

### Advanced Efficiency Tips
1. **Combine shortcuts** with snippets
2. **Use command palette** for rare commands
3. **Create shortcuts** for extension commands
4. **Organize shortcuts** by workflow context
5. **Regular practice** sessions

## Best Practices

### Keybinding Design
1. **Use familiar patterns** (Ctrl+S for save)
2. **Group related shortcuts** (Ctrl+K prefix)
3. **Avoid system conflicts**
4. **Keep it simple** and memorable
5. **Document custom shortcuts**

### Maintenance
1. **Regular review** of custom shortcuts
2. **Remove unused** keybindings
3. **Update for new** VS Code features
4. **Share with team** if collaborative
5. **Backup configurations**

## Next Steps

In Episode 13, we'll explore:
- Creating and using code snippets
- Custom snippet development
- Snippet variables and transformations
- Productivity-boosting snippet libraries

---

**Previous Episode:** Themes and Customization  
**Next Episode:** Code Snippets  
**Duration:** Approximately 30-35 minutes  
**Prerequisites:** Episodes 1-11 completed