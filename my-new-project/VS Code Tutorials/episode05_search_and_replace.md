# Episode 5: Search and Replace

## Overview
Powerful search and replace capabilities are essential for efficient code editing. VS Code provides advanced search features including regular expressions, multi-file operations, and smart filtering options.

## Basic Search

### Quick Search in Current File
- **Open Search:** `Ctrl+F`
- **Next Match:** `F3` or `Enter`
- **Previous Match:** `Shift+F3`
- **Close Search:** `Escape`

### Search Box Features
- **Case Sensitive:** `Alt+C` or click "Aa" icon
- **Whole Word:** `Alt+W` or click "Ab" icon
- **Regular Expression:** `Alt+R` or click ".*" icon

### Navigation Shortcuts
```
Ctrl+F          - Find in current file
Ctrl+H          - Find and replace in current file
Ctrl+Shift+F    - Find in files (global search)
Ctrl+Shift+H    - Find and replace in files
F3              - Find next
Shift+F3        - Find previous
Ctrl+F3         - Find next selection
Ctrl+Shift+F3   - Find previous selection
```

## Advanced Search Options

### Search Modes

#### Case Sensitivity
- **Sensitive:** Matches exact case
- **Insensitive:** Ignores case differences
- Toggle with `Alt+C`

```
Search: "function"
Case Sensitive: Matches only "function"
Case Insensitive: Matches "function", "Function", "FUNCTION"
```

#### Whole Word Matching
- Matches complete words only
- Ignores partial matches within other words
- Toggle with `Alt+W`

```
Search: "log" (Whole Word enabled)
Matches: "log", "console.log()"
Ignores: "login", "dialog", "logger"
```

#### Regular Expressions
- Enable with `Alt+R`
- Powerful pattern matching
- Uses JavaScript regex syntax

## Find and Replace in Current File

### Basic Replace Operations
1. Open replace panel with `Ctrl+H`
2. Enter search term in first box
3. Enter replacement in second box
4. **Replace:** Click replace icon or `Ctrl+Shift+1`
5. **Replace All:** Click replace all icon or `Ctrl+Alt+Enter`

### Replace Controls
- **Replace Next:** `Ctrl+Shift+1`
- **Replace All:** `Ctrl+Alt+Enter`
- **Skip to Next:** `F3`

### Preserve Case
- Maintains original capitalization pattern
- Useful for variable renaming
- Enable in replace options

```
Original: "userName", "USERNAME", "UserName"
Search: "user"
Replace: "customer" (with preserve case)
Result: "customerName", "CUSTOMERNAME", "CustomerName"
```

## Multi-File Search and Replace

### Global Search
- **Open:** `Ctrl+Shift+F`
- Search across entire workspace
- Powerful filtering options
- Replace across multiple files

### Search Panel Features

#### Include/Exclude Patterns
```
Include files: *.js, *.ts
Exclude files: node_modules/**, *.test.js
Include folders: src/, components/
Exclude folders: build/, dist/
```

#### Search Scope Options
- **Open Editors Only:** Search only in currently open files
- **Include/Exclude:** Use glob patterns to filter files
- **File Type Filter:** Focus on specific file extensions

### Multi-File Replace
1. Use `Ctrl+Shift+H` for global find and replace
2. Enter search and replace terms
3. Review all matches before replacing
4. **Replace All:** Replaces in all files
5. **Replace in File:** Replace only in specific file

### Replace Preview
- Shows all matches before replacement
- Click individual results to navigate
- Uncheck files/matches to exclude from replacement
- Undo available after replacement

## Regular Expressions

### Basic Regex Patterns

#### Character Classes
```
.       - Any character except newline
\d      - Any digit (0-9)
\w      - Any word character (a-z, A-Z, 0-9, _)
\s      - Any whitespace character
[abc]   - Any character in brackets
[a-z]   - Any lowercase letter
[^abc]  - Any character NOT in brackets
```

#### Quantifiers
```
*       - Zero or more
+       - One or more
?       - Zero or one
{n}     - Exactly n times
{n,}    - n or more times
{n,m}   - Between n and m times
```

#### Anchors
```
^       - Start of line
$       - End of line
\b      - Word boundary
\B      - Non-word boundary
```

### Practical Regex Examples

#### Find Email Addresses
```
Pattern: \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b
Matches: user@example.com, test.email+tag@domain.co.uk
```

#### Find Phone Numbers
```
Pattern: \b\d{3}-\d{3}-\d{4}\b
Matches: 123-456-7890
```

#### Find URLs
```
Pattern: https?://[^\s]+
Matches: http://example.com, https://www.site.com/path
```

#### Find Function Definitions (JavaScript)
```
Pattern: function\s+(\w+)\s*\(
Matches: function myFunction(, function calculateTotal(
```

#### Find CSS Classes
```
Pattern: \.[\w-]+
Matches: .container, .nav-item, .btn-primary
```

### Capture Groups and Replacement

#### Using Capture Groups
```
Search: function (\w+)\((.*?)\)
Replace: const $1 = ($2) =>
```

**Example:**
```javascript
// Before
function calculateTotal(price, tax) {
  return price + tax;
}

// After
const calculateTotal = (price, tax) => {
  return price + tax;
}
```

#### Named Capture Groups
```
Search: (?<name>\w+)\s*=\s*(?<value>\d+)
Replace: const ${name} = ${value};
```

### Advanced Regex Patterns

#### Lookahead and Lookbehind
```
(?=pattern)     - Positive lookahead
(?!pattern)     - Negative lookahead
(?<=pattern)    - Positive lookbehind
(?<!pattern)    - Negative lookbehind
```

#### Find Console.log Statements to Remove
```
Pattern: console\.log\(.*?\);?\n?
Replace: (empty)
```

#### Convert Single Quotes to Double Quotes
```
Pattern: '([^']*)'
Replace: "$1"
```

## Search Filters and Scope

### File Pattern Matching

#### Include Patterns
```
*.js                    - All JavaScript files
src/**/*.ts            - All TypeScript files in src folder
components/**/*.vue    - All Vue files in components
**/*.{js,ts,jsx,tsx}   - All JS/TS files anywhere
```

#### Exclude Patterns
```
node_modules/**        - Exclude all node_modules
**/*.test.js          - Exclude test files
dist/**               - Exclude build output
**/*.min.js           - Exclude minified files
*.log                 - Exclude log files
```

### Search in Specific Locations

#### Search in Open Editors Only
- Checkbox in search panel
- Limits search to currently open files
- Faster for active development

#### Search in Selection
1. Select text in editor
2. Open search with `Ctrl+F`
3. Search automatically scoped to selection
4. Indicated by selection icon in search box

## Search Results Navigation

### Results Panel
- Shows all matches with context
- Click to navigate to specific match
- Grouped by file
- Expandable/collapsible sections

### Keyboard Navigation
```
F4              - Go to next search result
Shift+F4        - Go to previous search result
Enter           - Go to selected result
Arrow Keys      - Navigate through results
```

### Search History
- **Previous Search:** `Alt+Up Arrow`
- **Next Search:** `Alt+Down Arrow`
- Automatically saved across sessions

## Advanced Search Techniques

### Search and Replace Workflows

#### Refactoring Variable Names
1. Select variable name
2. Press `Ctrl+F2` to select all occurrences
3. Type new name to replace all instances
4. Or use `Ctrl+Shift+L` to add cursors to all matches

#### Converting Code Patterns
```
# Convert var to const/let
Search: var (\w+) = (.+);
Replace: const $1 = $2;

# Add semicolons to lines
Search: ^(.+)(?<!;)$
Replace: $1;

# Remove empty lines
Search: ^\s*$\n
Replace: (empty)
```

### Search in Specific File Types

#### JavaScript/TypeScript Specific
```
# Find all function exports
Pattern: export\s+(function|const|let)\s+(\w+)

# Find import statements
Pattern: import.*from\s+['"](.+)['"]

# Find async functions
Pattern: async\s+function\s+(\w+)
```

#### HTML/CSS Specific
```
# Find all class attributes
Pattern: class=['"]([^'"]*)['"']

# Find CSS color values
Pattern: #[0-9a-fA-F]{3,6}

# Find inline styles
Pattern: style=['"]([^'"]*)['"']
```

## Search Performance Optimization

### Improving Search Speed

#### Use Specific Patterns
- Be as specific as possible
- Use file type filters
- Exclude unnecessary directories

#### Exclude Large Directories
```json
{
  "search.exclude": {
    "**/node_modules": true,
    "**/bower_components": true,
    "**/*.code-search": true,
    "**/dist": true,
    "**/build": true
  }
}
```

#### File Watchers
```json
{
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/node_modules/**": true,
    "**/tmp/**": true
  }
}
```

## Practical Exercises

### Exercise 1: Basic Search and Replace
1. Create a file with repeated text
2. Practice case-sensitive vs insensitive search
3. Use whole word matching
4. Replace single instances vs all instances

### Exercise 2: Multi-File Operations
1. Create multiple files with similar content
2. Use global search to find patterns across files
3. Practice include/exclude patterns
4. Perform multi-file replace operation

### Exercise 3: Regular Expression Practice
1. Create file with various data patterns
2. Practice basic regex patterns
3. Use capture groups for complex replacements
4. Try lookahead/lookbehind patterns

### Exercise 4: Code Refactoring
1. Create JavaScript code with old patterns
2. Use regex to convert var to const/let
3. Update function syntax using capture groups
4. Clean up console.log statements

## Common Search Patterns

### Code Cleanup
```
# Remove console.log statements
Search: console\.log\(.*?\);?\s*\n?
Replace: (empty)

# Remove empty lines
Search: ^\s*\n
Replace: (empty)

# Fix spacing around operators
Search: (\w+)\s*=\s*(\w+)
Replace: $1 = $2
```

### Documentation
```
# Find TODO comments
Search: //\s*TODO:?\s*(.*)
Replace: // TODO: $1

# Find functions without JSDoc
Search: ^\s*function\s+(\w+)(?!\s*\/\*\*)
```

### HTML/CSS
```
# Convert class to className (React)
Search: class=
Replace: className=

# Find broken image tags
Search: <img[^>]*src=['"']['"']
```

## Troubleshooting Search Issues

### Common Problems

#### Search Not Finding Expected Results
1. Check case sensitivity settings
2. Verify whole word option
3. Ensure correct file inclusion/exclusion
4. Test regex pattern in regex tester

#### Performance Issues
1. Exclude large directories
2. Use more specific search patterns
3. Limit search scope with file patterns
4. Close unnecessary editor tabs

#### Regex Not Working
1. Verify regex mode is enabled (`Alt+R`)
2. Escape special characters properly
3. Test pattern incrementally
4. Use online regex testing tools

## Next Steps

In Episode 6, we'll explore:
- Multi-cursor editing techniques
- Column selection and editing
- Advanced text selection methods
- Productivity shortcuts for bulk editing

---

**Previous Episode:** Code Editing Features  
**Next Episode:** Multi-cursor and Selection  
**Duration:** Approximately 25-30 minutes  
**Prerequisites:** Episodes 1-4 completed