# Episode 4: Code Editing Features

## Overview
VS Code offers powerful editing features that can dramatically improve your coding productivity. In this episode, we'll explore IntelliSense, code formatting, folding, and other advanced editing capabilities.

## IntelliSense - Intelligent Code Completion

### What is IntelliSense?
IntelliSense provides:
- **Auto-completion** - Suggests code as you type
- **Parameter hints** - Shows function parameters
- **Quick info** - Displays documentation on hover
- **Error checking** - Real-time syntax validation

### How IntelliSense Works
1. **Trigger:** Start typing or press `Ctrl+Space`
2. **Navigate:** Use arrow keys to browse suggestions
3. **Accept:** Press `Tab` or `Enter` to accept
4. **Dismiss:** Press `Escape` to close

### IntelliSense Features by Language

#### JavaScript/TypeScript
```javascript
// Auto-completion for objects
const user = {
  name: "John",
  age: 30
};
user. // Shows 'name' and 'age' suggestions

// Function parameter hints
function greet(name, greeting = "Hello") {
  return `${greeting}, ${name}!`;
}
greet( // Shows parameter hints
```

#### Python
```python
# Import suggestions
import os. # Shows available modules
import numpy as np
np. # Shows numpy functions and classes

# Method completion
my_list = [1, 2, 3]
my_list. # Shows list methods like append, remove, etc.
```

#### HTML
```html
<!-- Tag completion -->
<div class="container">
  <h <!-- Suggests h1, h2, h3, etc. -->
  
<!-- Attribute completion -->
<img src="" alt="" <!-- Suggests common attributes -->
```

#### CSS
```css
/* Property completion */
.container {
  background- /* Suggests background properties */
  display: /* Suggests display values */
}
```

### Customizing IntelliSense

#### Settings Configuration
```json
{
  "editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": false
  },
  "editor.suggestOnTriggerCharacters": true,
  "editor.acceptSuggestionOnCommitCharacter": true,
  "editor.acceptSuggestionOnEnter": "on",
  "editor.tabCompletion": "on"
}
```

#### Trigger Characters
- `.` (dot) - Object properties/methods
- `@` - Decorators (Python, TypeScript)
- `#` - CSS selectors, preprocessor directives
- `<` - HTML tags

## Code Formatting

### Automatic Formatting

#### Format Document
- **Command:** `Shift+Alt+F`
- **Or:** Right-click > Format Document
- **Or:** Command Palette > Format Document

#### Format Selection
- Select code block
- **Command:** `Ctrl+K Ctrl+F`
- **Or:** Right-click > Format Selection

#### Format on Save
```json
{
  "editor.formatOnSave": true,
  "editor.formatOnType": true,
  "editor.formatOnPaste": true
}
```

### Language-Specific Formatting

#### JavaScript/TypeScript (with Prettier)
```javascript
// Before formatting
const obj={name:"John",age:30,city:"New York"};

// After formatting
const obj = {
  name: "John",
  age: 30,
  city: "New York"
};
```

#### Python (with autopep8 or black)
```python
# Before formatting
def calculate_total(items,tax_rate=0.1):
    subtotal=sum(item['price'] for item in items)
    return subtotal*(1+tax_rate)

# After formatting
def calculate_total(items, tax_rate=0.1):
    subtotal = sum(item['price'] for item in items)
    return subtotal * (1 + tax_rate)
```

#### HTML
```html
<!-- Before formatting -->
<div><h1>Title</h1><p>Content</p></div>

<!-- After formatting -->
<div>
  <h1>Title</h1>
  <p>Content</p>
</div>
```

### Formatting Configuration

#### Per-Language Settings
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
  "[html]": {
    "editor.defaultFormatter": "vscode.html-language-features",
    "editor.tabSize": 2
  }
}
```

## Code Folding

### What is Code Folding?
Code folding allows you to:
- Collapse and expand code sections
- Focus on specific parts of large files
- Improve code readability
- Navigate complex codebases easier

### Folding Controls

#### Manual Folding
- **Collapse:** Click the down arrow (chevron) next to line numbers
- **Expand:** Click the right arrow
- **Keyboard:** `Ctrl+Shift+[` to fold, `Ctrl+Shift+]` to unfold

#### Folding Commands
- **Fold All:** `Ctrl+K Ctrl+0`
- **Unfold All:** `Ctrl+K Ctrl+J`
- **Fold Level 1:** `Ctrl+K Ctrl+1`
- **Fold Level 2:** `Ctrl+K Ctrl+2`
- **Toggle Fold:** `Ctrl+K Ctrl+L`

### Foldable Regions

#### Automatic Folding
- Functions and methods
- Classes and objects
- Control structures (if, for, while)
- Comment blocks
- Import sections

#### Custom Folding Regions

**JavaScript/TypeScript:**
```javascript
//#region Helper Functions
function add(a, b) {
  return a + b;
}

function multiply(a, b) {
  return a * b;
}
//#endregion

//#region Main Logic
// Your main code here
//#endregion
```

**Python:**
```python
# region Helper Functions
def calculate_tax(amount, rate):
    return amount * rate

def format_currency(amount):
    return f"${amount:.2f}"
# endregion

# region Main Application
# Your main code here
# endregion
```

**CSS:**
```css
/* #region Layout Styles */
.container {
  max-width: 1200px;
  margin: 0 auto;
}

.grid {
  display: grid;
  gap: 1rem;
}
/* #endregion */

/* #region Typography */
h1, h2, h3 {
  font-family: 'Arial', sans-serif;
}
/* #endregion */
```

## Syntax Highlighting

### Understanding Syntax Highlighting
- **Keywords** - `function`, `class`, `if`, `for` (usually blue)
- **Strings** - Text in quotes (usually green or orange)
- **Comments** - Explanatory text (usually gray)
- **Numbers** - Numeric values (usually light blue)
- **Operators** - `+`, `-`, `=`, `&&` (usually white or gray)

### Language Detection
VS Code automatically detects file types by:
1. **File extension** - `.js`, `.py`, `.html`
2. **Shebang lines** - `#!/usr/bin/python`
3. **File content analysis**

### Manual Language Selection
1. Click language indicator in status bar
2. **Or:** `Ctrl+K M`
3. **Or:** Command Palette > "Change Language Mode"

### Custom File Associations
```json
{
  "files.associations": {
    "*.env": "properties",
    "*.config": "json",
    "Dockerfile.*": "dockerfile"
  }
}
```

## Indentation and Whitespace

### Indentation Settings

#### Global Settings
```json
{
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "editor.detectIndentation": true,
  "editor.trimAutoWhitespace": true
}
```

#### Per-Language Indentation
```json
{
  "[python]": {
    "editor.tabSize": 4,
    "editor.insertSpaces": true
  },
  "[javascript]": {
    "editor.tabSize": 2,
    "editor.insertSpaces": true
  },
  "[go]": {
    "editor.tabSize": 4,
    "editor.insertSpaces": false
  }
}
```

### Whitespace Visualization
- **Show whitespace:** View > Render Whitespace
- **Or:** `Ctrl+Shift+P` > "View: Toggle Render Whitespace"
- Dots for spaces, arrows for tabs

### Auto-Indentation
- **Smart indentation** - VS Code automatically indents based on language rules
- **Bracket matching** - Maintains proper nesting
- **Paste formatting** - Adjusts indentation when pasting code

## Code Navigation

### Go to Definition
- **Shortcut:** `F12` or `Ctrl+Click`
- Jump to where function/variable is defined
- Works across files

### Peek Definition
- **Shortcut:** `Alt+F12`
- Shows definition in inline popup
- Continue editing without losing context

### Go to Symbol
- **In File:** `Ctrl+Shift+O`
- **In Workspace:** `Ctrl+T`
- **Add `:` to group symbols**

### Go to Line
- **Shortcut:** `Ctrl+G`
- Type line number to jump directly

### Breadcrumb Navigation
- **Enable:** View > Show Breadcrumbs
- **Navigate:** `Ctrl+Shift+.`
- Shows current location in file hierarchy

## Error Detection and Quick Fixes

### Error Indicators
- **Red squiggly lines** - Syntax errors
- **Yellow squiggly lines** - Warnings
- **Blue squiggly lines** - Information/suggestions

### Problems Panel
- **Open:** View > Problems or `Ctrl+Shift+M`
- Lists all errors and warnings
- Click to navigate to problem location

### Quick Fixes
- **Shortcut:** `Ctrl+.` on error line
- **Light bulb icon** - Click for suggestions
- Common fixes:
  - Import missing modules
  - Fix syntax errors
  - Add missing semicolons
  - Convert to arrow functions

### Example Quick Fixes

#### JavaScript
```javascript
// Error: 'console' is not defined
console.log("Hello World");
// Quick fix: Add /* global console */ comment

// Warning: Unused variable
let unusedVar = 5;
// Quick fix: Remove variable or add underscore prefix
```

#### Python
```python
# Error: Import not found
import numpy as np
# Quick fix: Install numpy package

# Warning: Unused import
import os
import sys  # This is unused
# Quick fix: Remove unused import
```

## Code Snippets (Built-in)

### Using Built-in Snippets
- Type snippet prefix and press `Tab`
- Use `Tab` to navigate between placeholders
- `Shift+Tab` to go backwards

### Common Snippets by Language

#### JavaScript
- `log` → `console.log()`
- `for` → `for (let i = 0; i < array.length; i++) {}`
- `func` → `function name() {}`
- `if` → `if (condition) {}`

#### HTML
- `!` → HTML5 boilerplate
- `div` → `<div></div>`
- `link:css` → CSS link tag
- `script:src` → External script tag

#### CSS
- `m` → `margin: ;`
- `p` → `padding: ;`
- `bg` → `background: ;`
- `fz` → `font-size: ;`

## Practical Exercises

### Exercise 1: IntelliSense Practice
1. Create a JavaScript file
2. Define an object with properties
3. Practice using auto-completion for object properties
4. Try function parameter hints

### Exercise 2: Formatting Setup
1. Install Prettier extension
2. Enable format on save
3. Create messy code and test auto-formatting
4. Try formatting selection vs. entire document

### Exercise 3: Code Folding
1. Create a large file with multiple functions
2. Practice folding and unfolding sections
3. Create custom folding regions
4. Use different folding levels

### Exercise 4: Navigation Practice
1. Create multiple files with interconnected functions
2. Practice Go to Definition and Peek Definition
3. Use Go to Symbol to navigate within files
4. Try breadcrumb navigation

## Keyboard Shortcuts Summary

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| IntelliSense | `Ctrl+Space` | `Cmd+Space` |
| Format Document | `Shift+Alt+F` | `Shift+Option+F` |
| Format Selection | `Ctrl+K Ctrl+F` | `Cmd+K Cmd+F` |
| Fold/Unfold | `Ctrl+Shift+[/]` | `Cmd+Option+[/]` |
| Go to Definition | `F12` | `F12` |
| Peek Definition | `Alt+F12` | `Option+F12` |
| Go to Symbol | `Ctrl+Shift+O` | `Cmd+Shift+O` |
| Go to Line | `Ctrl+G` | `Cmd+G` |
| Quick Fix | `Ctrl+.` | `Cmd+.` |
| Problems Panel | `Ctrl+Shift+M` | `Cmd+Shift+M` |

## Tips for Better Code Editing

### Performance Tips
1. **Disable unused extensions** for better IntelliSense performance
2. **Use workspace-specific settings** for large projects
3. **Exclude large folders** from file watching

### Productivity Tips
1. **Learn common snippets** for your language
2. **Use quick fixes** regularly to improve code quality
3. **Customize indentation** per project needs
4. **Enable format on save** for consistent code style

### Best Practices
1. **Consistent formatting** across team projects
2. **Use meaningful variable names** for better IntelliSense
3. **Add JSDoc/docstrings** for better documentation
4. **Keep files reasonably sized** for better folding

## Next Steps

In Episode 5, we'll explore:
- Advanced search and replace functionality
- Regular expressions in VS Code
- Multi-file search and replace
- Search filters and excludes

---

**Previous Episode:** Essential Extensions  
**Next Episode:** Search and Replace  
**Duration:** Approximately 30-35 minutes  
**Prerequisites:** Episodes 1-3 completed