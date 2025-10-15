# Episode 13: Code Snippets

## Overview
Code snippets are reusable code templates that can dramatically speed up your development workflow. This episode covers using built-in snippets, creating custom snippets, advanced snippet features, and building a productive snippet library.

## Understanding Code Snippets

### What are Code Snippets?
Code snippets are:
- **Reusable code templates** with placeholder variables
- **Time-saving shortcuts** for common code patterns
- **Customizable templates** that adapt to your coding style
- **Language-specific** or global templates

### How Snippets Work
1. **Type snippet prefix** (trigger text)
2. **Press Tab** to expand
3. **Navigate placeholders** with Tab
4. **Fill in variables** as needed
5. **Press Escape** to exit snippet mode

### Snippet Benefits
- **Faster coding** with reduced typing
- **Consistent code** structure and style
- **Reduced errors** in boilerplate code
- **Better productivity** for repetitive tasks

## Using Built-in Snippets

### Accessing Snippets

#### IntelliSense Integration
- Snippets appear in **auto-completion** suggestions
- **Tab completion** expands snippets
- **Snippet icons** (small square) identify them

#### Insert Snippet Command
1. **Command Palette** (`Ctrl+Shift+P`)
2. **Type** "Insert Snippet"
3. **Choose from list** of available snippets

#### Quick Suggestions
```json
{
  "editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": false
  },
  "editor.suggest.snippetsPreventQuickSuggestions": false
}
```

### Language-Specific Built-in Snippets

#### JavaScript Snippets
```javascript
// Type "log" and press Tab
console.log();

// Type "for" and press Tab
for (let index = 0; index < array.length; index++) {
  const element = array[index];
}

// Type "func" and press Tab
function name(params) {
  
}

// Type "if" and press Tab
if (condition) {
  
}

// Type "try" and press Tab
try {
  
} catch (error) {
  
}
```

#### HTML Snippets
```html
<!-- Type "!" and press Tab -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>

<!-- Type "div" and press Tab -->
<div></div>

<!-- Type "link:css" and press Tab -->
<link rel="stylesheet" href="style.css">

<!-- Type "script:src" and press Tab -->
<script src=""></script>
```

#### CSS Snippets
```css
/* Type "m" and press Tab */
margin: ;

/* Type "p" and press Tab */
padding: ;

/* Type "bg" and press Tab */
background: ;

/* Type "fz" and press Tab */
font-size: ;

/* Type "df" and press Tab */
display: flex;
```

#### Python Snippets
```python
# Type "def" and press Tab
def function_name():
    pass

# Type "class" and press Tab
class ClassName:
    def __init__(self):
        pass

# Type "if" and press Tab
if condition:
    pass

# Type "for" and press Tab
for item in iterable:
    pass

# Type "try" and press Tab
try:
    pass
except Exception as e:
    pass
```

## Creating Custom Snippets

### Snippet File Locations

#### Global Snippets
- **Location:** User snippets folder
- **Access:** File > Preferences > Configure User Snippets
- **Scope:** Available in all projects

#### Workspace Snippets
- **Location:** `.vscode` folder in workspace
- **Scope:** Available only in current workspace
- **Team sharing:** Committed with project

### Snippet File Structure

#### Basic Snippet Format
```json
{
  "Snippet Name": {
    "prefix": "trigger",
    "body": [
      "Line 1 of snippet",
      "Line 2 of snippet",
      "$0"
    ],
    "description": "Description of what this snippet does"
  }
}
```

#### Example: Simple Function Snippet
```json
{
  "Arrow Function": {
    "prefix": "arrf",
    "body": [
      "const $1 = ($2) => {",
      "\t$3",
      "\treturn $4;",
      "};"
    ],
    "description": "Create arrow function"
  }
}
```

### Snippet Variables and Placeholders

#### Tabstops and Placeholders
```json
{
  "React Component": {
    "prefix": "rfc",
    "body": [
      "import React from 'react';",
      "",
      "const $1 = () => {",
      "\treturn (",
      "\t\t<div>",
      "\t\t\t$2",
      "\t\t</div>",
      "\t);",
      "};",
      "",
      "export default $1;"
    ],
    "description": "React functional component"
  }
}
```

#### Default Values
```json
{
  "Function with Default": {
    "prefix": "funcd",
    "body": [
      "function ${1:functionName}(${2:param}) {",
      "\t${3:// function body}",
      "\treturn ${4:value};",
      "}"
    ],
    "description": "Function with default placeholder values"
  }
}
```

#### Choice Placeholders
```json
{
  "Console Method": {
    "prefix": "con",
    "body": [
      "console.${1|log,warn,error,info|}('${2:message}');"
    ],
    "description": "Console with method choice"
  }
}
```

### Advanced Snippet Features

#### Built-in Variables
```json
{
  "File Header": {
    "prefix": "header",
    "body": [
      "/**",
      " * File: $TM_FILENAME",
      " * Author: $USER",
      " * Date: $CURRENT_DATE",
      " * Time: $CURRENT_HOUR:$CURRENT_MINUTE",
      " * Description: $1",
      " */"
    ],
    "description": "File header with auto-filled information"
  }
}
```

#### Common Variables
```
$TM_FILENAME          # Current filename
$TM_FILENAME_BASE     # Filename without extension
$TM_DIRECTORY         # Directory of current file
$TM_FILEPATH          # Full file path
$WORKSPACE_NAME       # Name of workspace
$WORKSPACE_FOLDER     # Path to workspace folder
$CURRENT_YEAR         # Current year
$CURRENT_MONTH        # Current month (01-12)
$CURRENT_DATE         # Current date (dd)
$CURRENT_HOUR         # Current hour (24-hour format)
$CURRENT_MINUTE       # Current minute
$CURRENT_SECOND       # Current second
$USER                 # Username
$LINE_COMMENT         # Line comment character
$BLOCK_COMMENT_START  # Block comment start
$BLOCK_COMMENT_END    # Block comment end
```

#### Variable Transformations
```json
{
  "Class from Filename": {
    "prefix": "class",
    "body": [
      "class ${TM_FILENAME_BASE/(.*)/${1:/pascalcase}/} {",
      "\tconstructor(${1:params}) {",
      "\t\t$2",
      "\t}",
      "",
      "\t$3",
      "}"
    ],
    "description": "Class with name from filename"
  }
}
```

## Practical Snippet Examples

### Web Development Snippets

#### HTML Structure Snippets
```json
{
  "HTML5 Boilerplate": {
    "prefix": "html5",
    "body": [
      "<!DOCTYPE html>",
      "<html lang=\"${1:en}\">",
      "<head>",
      "\t<meta charset=\"UTF-8\">",
      "\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
      "\t<title>${2:Document}</title>",
      "\t<link rel=\"stylesheet\" href=\"${3:style.css}\">",
      "</head>",
      "<body>",
      "\t$4",
      "\t<script src=\"${5:script.js}\"></script>",
      "</body>",
      "</html>"
    ],
    "description": "Complete HTML5 boilerplate"
  },
  
  "Navigation Menu": {
    "prefix": "nav",
    "body": [
      "<nav class=\"${1:navbar}\">",
      "\t<ul>",
      "\t\t<li><a href=\"${2:#}\">${3:Home}</a></li>",
      "\t\t<li><a href=\"${4:#}\">${5:About}</a></li>",
      "\t\t<li><a href=\"${6:#}\">${7:Contact}</a></li>",
      "\t</ul>",
      "</nav>"
    ],
    "description": "Basic navigation menu"
  }
}
```

#### CSS Snippets
```json
{
  "Flexbox Container": {
    "prefix": "flexbox",
    "body": [
      "display: flex;",
      "justify-content: ${1|flex-start,flex-end,center,space-between,space-around,space-evenly|};",
      "align-items: ${2|stretch,flex-start,flex-end,center,baseline|};",
      "flex-direction: ${3|row,row-reverse,column,column-reverse|};"
    ],
    "description": "Flexbox container properties"
  },
  
  "CSS Grid": {
    "prefix": "grid",
    "body": [
      "display: grid;",
      "grid-template-columns: ${1:repeat(auto-fit, minmax(250px, 1fr))};",
      "grid-gap: ${2:1rem};",
      "grid-template-rows: ${3:auto};"
    ],
    "description": "CSS Grid container"
  },
  
  "Media Query": {
    "prefix": "media",
    "body": [
      "@media (${1|max-width,min-width|}: ${2:768px}) {",
      "\t$3",
      "}"
    ],
    "description": "CSS media query"
  }
}
```

#### JavaScript/React Snippets
```json
{
  "React Hooks Component": {
    "prefix": "rfc",
    "body": [
      "import React, { useState, useEffect } from 'react';",
      "",
      "const $1 = () => {",
      "\tconst [${2:state}, set${2/(.*)/${1:/capitalize}/}] = useState(${3:initialValue});",
      "",
      "\tuseEffect(() => {",
      "\t\t$4",
      "\t}, []);",
      "",
      "\treturn (",
      "\t\t<div>",
      "\t\t\t$5",
      "\t\t</div>",
      "\t);",
      "};",
      "",
      "export default $1;"
    ],
    "description": "React functional component with hooks"
  },
  
  "Async Function": {
    "prefix": "asyncfunc",
    "body": [
      "const ${1:functionName} = async (${2:params}) => {",
      "\ttry {",
      "\t\tconst response = await ${3:apiCall};",
      "\t\t$4",
      "\t} catch (error) {",
      "\t\tconsole.error('Error:', error);",
      "\t\t$5",
      "\t}",
      "};"
    ],
    "description": "Async function with error handling"
  },
  
  "API Fetch": {
    "prefix": "fetch",
    "body": [
      "fetch('${1:url}')",
      "\t.then(response => {",
      "\t\tif (!response.ok) {",
      "\t\t\tthrow new Error('Network response was not ok');",
      "\t\t}",
      "\t\treturn response.json();",
      "\t})",
      "\t.then(data => {",
      "\t\t$2",
      "\t})",
      "\t.catch(error => {",
      "\t\tconsole.error('Error:', error);",
      "\t\t$3",
      "\t});"
    ],
    "description": "Fetch API call with error handling"
  }
}
```

### Backend Development Snippets

#### Python Snippets
```json
{
  "Python Class": {
    "prefix": "class",
    "body": [
      "class ${1:ClassName}:",
      "\t\"\"\"${2:Class description}\"\"\"",
      "\t",
      "\tdef __init__(self, ${3:params}):",
      "\t\t\"\"\"Initialize ${1:ClassName}\"\"\"",
      "\t\t$4",
      "\t",
      "\tdef ${5:method_name}(self, ${6:params}):",
      "\t\t\"\"\"${7:Method description}\"\"\"",
      "\t\t$8"
    ],
    "description": "Python class with docstrings"
  },
  
  "Flask Route": {
    "prefix": "route",
    "body": [
      "@app.route('/${1:path}', methods=['${2|GET,POST,PUT,DELETE|}'])",
      "def ${3:function_name}():",
      "\t\"\"\"${4:Route description}\"\"\"",
      "\t$5",
      "\treturn ${6:response}"
    ],
    "description": "Flask route handler"
  },
  
  "Python Function with Docstring": {
    "prefix": "deff",
    "body": [
      "def ${1:function_name}(${2:params}) -> ${3:return_type}:",
      "\t\"\"\"${4:Function description}",
      "\t",
      "\tArgs:",
      "\t\t${2:params}: ${5:Parameter description}",
      "\t",
      "\tReturns:",
      "\t\t${3:return_type}: ${6:Return description}",
      "\t\"\"\"",
      "\t$7",
      "\treturn $8"
    ],
    "description": "Function with complete docstring"
  }
}
```

#### Node.js/Express Snippets
```json
{
  "Express Route": {
    "prefix": "route",
    "body": [
      "router.${1|get,post,put,delete|}('/${2:path}', async (req, res) => {",
      "\ttry {",
      "\t\t$3",
      "\t\tres.status(200).json({ success: true, data: $4 });",
      "\t} catch (error) {",
      "\t\tconsole.error(error);",
      "\t\tres.status(500).json({ success: false, error: error.message });",
      "\t}",
      "});"
    ],
    "description": "Express route with error handling"
  },
  
  "Mongoose Schema": {
    "prefix": "schema",
    "body": [
      "const ${1:modelName}Schema = new mongoose.Schema({",
      "\t${2:field}: {",
      "\t\ttype: ${3|String,Number,Date,Boolean,Array,Object|},",
      "\t\trequired: ${4|true,false|},",
      "\t\t${5:unique: true,}",
      "\t\t${6:default: ''}",
      "\t}",
      "}, {",
      "\ttimestamps: true",
      "});",
      "",
      "module.exports = mongoose.model('${1:modelName}', ${1:modelName}Schema);"
    ],
    "description": "Mongoose schema definition"
  }
}
```

## Advanced Snippet Techniques

### Conditional Snippets

#### Environment-Specific Snippets
```json
{
  "Console Log Debug": {
    "prefix": "logd",
    "body": [
      "if (process.env.NODE_ENV === 'development') {",
      "\tconsole.log('${1:Debug}:', ${2:variable});",
      "}"
    ],
    "description": "Debug console log"
  }
}
```

#### Multi-line Complex Snippets
```json
{
  "Test Suite": {
    "prefix": "describe",
    "body": [
      "describe('${1:Test Suite}', () => {",
      "\tbeforeEach(() => {",
      "\t\t${2:// Setup code}",
      "\t});",
      "",
      "\tafterEach(() => {",
      "\t\t${3:// Cleanup code}",
      "\t});",
      "",
      "\tit('${4:should do something}', () => {",
      "\t\t${5:// Test code}",
      "\t\texpect(${6:actual}).toBe(${7:expected});",
      "\t});",
      "",
      "\tit('${8:should do something else}', () => {",
      "\t\t${9:// Test code}",
      "\t\texpect(${10:actual}).toBe(${11:expected});",
      "\t});",
      "});"
    ],
    "description": "Complete test suite with setup and teardown"
  }
}
```

### Snippet Transformations

#### String Transformations
```json
{
  "Component File": {
    "prefix": "component",
    "body": [
      "import React from 'react';",
      "import './${TM_FILENAME_BASE}.css';",
      "",
      "const ${TM_FILENAME_BASE/(.*)/${1:/pascalcase}/} = ({ ${1:props} }) => {",
      "\treturn (",
      "\t\t<div className=\"${TM_FILENAME_BASE/(.*)/${1:/downcase}/}\">",
      "\t\t\t$2",
      "\t\t</div>",
      "\t);",
      "};",
      "",
      "export default ${TM_FILENAME_BASE/(.*)/${1:/pascalcase}/};"
    ],
    "description": "React component from filename"
  }
}
```

#### Available Transformations
```
/upcase/           # UPPERCASE
/downcase/         # lowercase
/capitalize/       # Capitalize First Letter
/pascalcase/       # PascalCase
/camelcase/        # camelCase
```

## Snippet Management

### Organizing Snippets

#### Language-Specific Files
```
snippets/
├── javascript.json      # JavaScript snippets
├── typescript.json     # TypeScript snippets
├── python.json         # Python snippets
├── html.json          # HTML snippets
├── css.json           # CSS snippets
└── global.json        # Global snippets
```

#### Snippet Categories
```json
{
  "// === REACT COMPONENTS ===": {},
  
  "React Functional Component": {
    "prefix": "rfc",
    "body": ["..."],
    "description": "React functional component"
  },
  
  "React Class Component": {
    "prefix": "rcc",
    "body": ["..."],
    "description": "React class component"
  },
  
  "// === HOOKS ===": {},
  
  "useState Hook": {
    "prefix": "useState",
    "body": ["..."],
    "description": "React useState hook"
  }
}
```

### Sharing Snippets

#### Team Snippets
1. **Create workspace snippets** in `.vscode` folder
2. **Commit to version control**
3. **Document snippet usage** in README
4. **Maintain consistency** across team

#### Snippet Extensions
- **Create extension** for company/team snippets
- **Publish to marketplace** for wider sharing
- **Version control** snippet collections

### Testing and Validation

#### Snippet Testing
1. **Test all placeholders** work correctly
2. **Verify transformations** produce expected results
3. **Check in different** file contexts
4. **Validate generated** code syntax

#### Common Issues
- **Missing commas** in JSON
- **Incorrect escaping** of special characters
- **Wrong placeholder** numbering
- **Invalid regex** in transformations

## Practical Exercises

### Exercise 1: Basic Snippet Creation
1. Create snippets for your most-used code patterns
2. Test placeholder navigation
3. Use different variable types
4. Add meaningful descriptions

### Exercise 2: Advanced Features
1. Create snippets using built-in variables
2. Implement choice placeholders
3. Use string transformations
4. Create multi-line complex snippets

### Exercise 3: Language-Specific Collection
1. Build comprehensive snippet collection for your main language
2. Include error handling patterns
3. Add testing and documentation snippets
4. Organize by categories

### Exercise 4: Team Snippet Library
1. Create workspace snippets for team
2. Document snippet usage
3. Establish naming conventions
4. Set up snippet maintenance process

## Snippet Best Practices

### Design Principles
1. **Keep prefixes short** but memorable
2. **Use consistent naming** conventions
3. **Include sensible defaults**
4. **Provide helpful descriptions**
5. **Test thoroughly** before sharing

### Maintenance
1. **Regular review** and updates
2. **Remove unused** snippets
3. **Update for new** language features
4. **Version control** snippet files
5. **Document changes**

### Performance
1. **Avoid overly complex** transformations
2. **Limit snippet size** when possible
3. **Use efficient** placeholder patterns
4. **Monitor impact** on IntelliSense performance

## Troubleshooting

### Common Problems

#### Snippet Not Appearing
1. **Check JSON syntax** for errors
2. **Verify file location** and naming
3. **Restart VS Code** to refresh
4. **Check language scope** restrictions

#### Placeholder Issues
1. **Verify numbering** sequence ($1, $2, $3...)
2. **Check special character** escaping
3. **Test transformation** regex patterns
4. **Validate choice** syntax

#### Performance Issues
1. **Simplify complex** snippets
2. **Reduce file size** if very large
3. **Optimize transformations**
4. **Check for conflicting** extensions

## Next Steps

In Episode 14, we'll explore:
- Remote development with SSH
- Working with containers
- WSL (Windows Subsystem for Linux) integration
- Cloud development environments

---

**Previous Episode:** Keyboard Shortcuts  
**Next Episode:** Remote Development  
**Duration:** Approximately 30-35 minutes  
**Prerequisites:** Episodes 1-12 completed