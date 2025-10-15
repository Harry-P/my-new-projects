# Episode 6: Multi-cursor and Selection

## Overview
Multi-cursor editing is one of VS Code's most powerful features, allowing you to edit multiple locations simultaneously. This episode covers various selection techniques and multi-cursor workflows that can dramatically improve your productivity.

## Understanding Multi-cursor Editing

### What is Multi-cursor Editing?
Multi-cursor editing allows you to:
- Edit multiple lines simultaneously
- Make identical changes in multiple locations
- Reduce repetitive typing tasks
- Perform bulk edits efficiently

### Visual Indicators
- **Primary cursor:** Regular blinking cursor
- **Secondary cursors:** Smaller vertical lines
- **Selections:** Highlighted text areas
- **Status bar:** Shows number of active cursors

## Basic Multi-cursor Operations

### Adding Cursors

#### Method 1: Alt + Click
- Hold `Alt` and click to add cursors
- Works anywhere in the document
- Most intuitive method for beginners

```javascript
// Click while holding Alt at the end of each line
const firstName = "John";     |
const lastName = "Doe";       |
const email = "john@doe.com"; |
// Now type semicolon to add to all lines
```

#### Method 2: Ctrl + Alt + Up/Down Arrow
- `Ctrl+Alt+Up Arrow` - Add cursor above
- `Ctrl+Alt+Down Arrow` - Add cursor below
- Creates column of cursors

```javascript
// Place cursor here and use Ctrl+Alt+Down Arrow
const name = "John";      |
const age = 30;           |
const city = "New York";  |
```

#### Method 3: Shift + Alt + Drag
- Click and drag while holding `Shift+Alt`
- Creates column selection
- Perfect for rectangular selections

### Adding Cursors to Matching Text

#### Method 1: Ctrl + D
1. Select a word or text
2. Press `Ctrl+D` to select next occurrence
3. Keep pressing `Ctrl+D` for more matches
4. Edit all selected instances simultaneously

```javascript
// Select "user" and press Ctrl+D multiple times
const user = getUser();
user.name = "John";
user.age = 30;
updateUser(user);
```

#### Method 2: Ctrl + Shift + L
- Select text
- Press `Ctrl+Shift+L` to select ALL occurrences
- Instantly selects every matching instance

#### Method 3: Ctrl + F2
- Place cursor on a word
- Press `Ctrl+F2` to select all occurrences of that word
- No need to select first

### Removing Cursors

#### Selective Removal
- **Undo last cursor:** `Ctrl+U`
- **Skip current and go to next:** `Ctrl+K Ctrl+D`
- **Remove all cursors:** `Escape`

#### Smart Cursor Management
```javascript
// If you have too many cursors, use Ctrl+U to remove the last added ones
const data = fetchData();    |
const result = processData(); |
const output = formatData();  |
const final = saveData();     | ← Remove this one with Ctrl+U
```

## Advanced Selection Techniques

### Line Selection

#### Selecting Entire Lines
- **Select current line:** `Ctrl+L`
- **Select multiple lines:** `Ctrl+L` then `Shift+Down Arrow`
- **Extend selection:** `Shift+Up/Down Arrow`

```javascript
// Select these lines with Ctrl+L and Shift+Down Arrow
function calculateTotal(items) {    ← Start here
  const subtotal = items.reduce();
  const tax = subtotal * 0.1;
  return subtotal + tax;
}                                   ← End here
```

#### Copy/Cut Entire Lines
- **Copy line:** `Ctrl+C` (without selection)
- **Cut line:** `Ctrl+X` (without selection)
- **Duplicate line:** `Shift+Alt+Down Arrow`

### Word and Token Selection

#### Double-click Selection
- **Double-click:** Selects entire word
- **Triple-click:** Selects entire line
- **Ctrl+Double-click:** Selects word and similar words

#### Smart Word Selection
- **Expand selection:** `Shift+Alt+Right Arrow`
- **Shrink selection:** `Shift+Alt+Left Arrow`
- Intelligently selects based on syntax

```javascript
// Place cursor in "firstName" and use Shift+Alt+Right Arrow
const user = {
  firstName: "John",  // Expands: firstName → "John" → firstName: "John"
  lastName: "Doe"
};
```

#### Bracket Matching
- **Select to matching bracket:** `Ctrl+Shift+\`
- **Jump to matching bracket:** `Ctrl+Shift+\`
- Works with (), [], {}, and HTML tags

### Column Selection and Editing

#### Creating Column Selections
1. **Method 1:** `Shift+Alt+Drag` vertically
2. **Method 2:** `Ctrl+Alt+Up/Down Arrow` for cursor column
3. **Method 3:** Middle mouse button drag (if enabled)

#### Column Editing Examples

**Example 1: Adding Comments**
```javascript
// Before column editing
const firstName = "John";
const lastName = "Doe";
const email = "john@doe.com";

// After adding cursors at line ends and typing
const firstName = "John";      // User data
const lastName = "Doe";        // User data
const email = "john@doe.com";  // User data
```

**Example 2: Formatting Data**
```javascript
// Before: Inconsistent formatting
name:"John"
age:30
city:"New York"

// After: Column selection to add spaces
name: "John"
age: 30
city: "New York"
```

**Example 3: HTML Attributes**
```html
<!-- Before -->
<img src="image1.jpg">
<img src="image2.jpg">
<img src="image3.jpg">

<!-- After adding alt attributes with column selection -->
<img src="image1.jpg" alt="">
<img src="image2.jpg" alt="">
<img src="image3.jpg" alt="">
```

## Practical Multi-cursor Use Cases

### Refactoring Variables

#### Renaming Variables
```javascript
// Original code
function processUser(userData) {
  userData.name = userData.name.toLowerCase();
  userData.email = userData.email.toLowerCase();
  return userData;
}

// Use Ctrl+F2 on "userData" to rename all instances
function processUser(user) {
  user.name = user.name.toLowerCase();
  user.email = user.email.toLowerCase();
  return user;
}
```

### Adding Import Statements
```javascript
// Select the word after each "import" and add quotes
// Before
import React from react
import useState from react
import useEffect from react

// After using multi-cursor
import React from "react"
import useState from "react"
import useEffect from "react"
```

### Formatting Lists
```javascript
// Converting array format
// Before
const colors = [red, blue, green, yellow];

// After using multi-cursor to add quotes
const colors = ["red", "blue", "green", "yellow"];
```

### HTML/CSS Editing

#### Adding Classes to Multiple Elements
```html
<!-- Before -->
<div>Content 1</div>
<div>Content 2</div>
<div>Content 3</div>

<!-- After using column selection -->
<div class="item">Content 1</div>
<div class="item">Content 2</div>
<div class="item">Content 3</div>
```

#### CSS Property Editing
```css
/* Before */
.header { color: red }
.footer { color: red }
.sidebar { color: red }

/* After selecting "red" instances and changing */
.header { color: blue }
.footer { color: blue }
.sidebar { color: blue }
```

## Advanced Multi-cursor Workflows

### Combining with Search and Replace

#### Find and Edit Workflow
1. Use `Ctrl+F` to find pattern
2. Use `Alt+Enter` to select all matches
3. Edit all selected instances
4. More precise than global replace

#### Regular Expression Multi-cursor
1. Enable regex in search (`Alt+R`)
2. Use capture groups in pattern
3. Select all matches with `Alt+Enter`
4. Edit with context awareness

### Multi-cursor with Snippets

#### Creating Repetitive Structures
```javascript
// Use multi-cursor to create multiple functions
// Type "function " then add cursors
function handleClick() {
  
}
function handleSubmit() {
  
}
function handleCancel() {
  
}
```

### Complex Editing Scenarios

#### Transforming Data Formats
```javascript
// Converting object format
// Before (use column selection and editing)
name=John
age=30
city=New York

// After
name: "John",
age: 30,
city: "New York",
```

#### Creating Test Cases
```javascript
// Generate multiple test cases
// Before
testUser1
testUser2
testUser3

// After using multi-cursor
describe("testUser1", () => {});
describe("testUser2", () => {});
describe("testUser3", () => {});
```

## Keyboard Shortcuts Summary

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Add cursor | `Alt+Click` | `Option+Click` |
| Add cursor above/below | `Ctrl+Alt+Up/Down` | `Cmd+Option+Up/Down` |
| Select next occurrence | `Ctrl+D` | `Cmd+D` |
| Select all occurrences | `Ctrl+Shift+L` | `Cmd+Shift+L` |
| Select word occurrences | `Ctrl+F2` | `Cmd+F2` |
| Undo last cursor | `Ctrl+U` | `Cmd+U` |
| Skip current selection | `Ctrl+K Ctrl+D` | `Cmd+K Cmd+D` |
| Column selection | `Shift+Alt+Drag` | `Shift+Option+Drag` |
| Select line | `Ctrl+L` | `Cmd+L` |
| Duplicate line | `Shift+Alt+Down` | `Shift+Option+Down` |

## Tips and Best Practices

### Effective Multi-cursor Usage

#### Start Small
- Begin with simple edits
- Practice basic cursor addition
- Gradually try complex scenarios

#### Use Preview
- Observe selections before editing
- Ensure all cursors are correctly placed
- Use `Escape` to cancel if needed

#### Combine Techniques
- Mix different cursor addition methods
- Use search to find, then multi-cursor to edit
- Combine with copy/paste operations

### Common Mistakes to Avoid

#### Too Many Cursors
- Limit cursors to manageable numbers
- Use `Ctrl+U` to remove excess cursors
- Consider search and replace for large numbers

#### Wrong Selections
- Double-check cursor positions
- Use undo if selection goes wrong
- Practice on test files first

#### Overcomplicating
- Sometimes simple search/replace is better
- Don't force multi-cursor for everything
- Choose the right tool for the task

## Practical Exercises

### Exercise 1: Basic Multi-cursor
1. Create a list of items
2. Use `Alt+Click` to add cursors
3. Add quotes around each item
4. Practice removing cursors with `Escape`

### Exercise 2: Ctrl+D Practice
1. Create repeated variable names
2. Select one occurrence
3. Use `Ctrl+D` to select others incrementally
4. Rename all instances

### Exercise 3: Column Selection
1. Create aligned data (like CSV)
2. Use `Shift+Alt+Drag` for column selection
3. Add/modify column data
4. Practice with different column widths

### Exercise 4: Complex Refactoring
1. Create a JavaScript object with repeated patterns
2. Use combination of selection techniques
3. Transform the structure using multi-cursor
4. Add/remove properties across multiple objects

## Real-world Examples

### Converting API Response Format
```javascript
// Before: Snake case to camel case
{
  user_name: "john",
  user_email: "john@example.com",
  user_age: 30
}

// After: Using multi-cursor to rename properties
{
  userName: "john",
  userEmail: "john@example.com",
  userAge: 30
}
```

### HTML Template Creation
```html
<!-- Before: Creating navigation items -->
Home
About
Contact
Services

<!-- After: Multi-cursor to create nav structure -->
<li><a href="#home">Home</a></li>
<li><a href="#about">About</a></li>
<li><a href="#contact">Contact</a></li>
<li><a href="#services">Services</a></li>
```

### CSS Media Queries
```css
/* Before: Multiple similar rules */
.container { width: 100%; }
.header { width: 100%; }
.footer { width: 100%; }

/* After: Adding responsive rules with multi-cursor */
.container { width: 100%; max-width: 1200px; }
.header { width: 100%; max-width: 1200px; }
.footer { width: 100%; max-width: 1200px; }
```

## Next Steps

In Episode 7, we'll explore:
- Using the integrated terminal
- Running commands and scripts
- Multiple terminal instances
- Terminal customization and shell integration

---

**Previous Episode:** Search and Replace  
**Next Episode:** Integrated Terminal  
**Duration:** Approximately 25-30 minutes  
**Prerequisites:** Episodes 1-5 completed