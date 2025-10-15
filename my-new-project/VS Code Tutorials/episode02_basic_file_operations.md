# Episode 2: Basic File Operations and Navigation

## Overview
Now that you have VS Code installed and understand the interface, let's explore how to work with files and navigate your projects efficiently.

## Creating Files and Folders

### Creating New Files
1. **Method 1: File Menu**
   - Go to **File > New File** or press `Ctrl+N`
   - Type your content
   - Save with `Ctrl+S` and specify name and location

2. **Method 2: Explorer Panel**
   - Click the "New File" icon in Explorer
   - Type filename directly in the sidebar
   - Press `Enter` to confirm

3. **Method 3: Command Palette**
   - Press `Ctrl+Shift+P`
   - Type "File: New File"
   - Select the command

### Creating New Folders
1. **In Explorer Panel**
   - Right-click in empty space or on a folder
   - Select "New Folder"
   - Type folder name and press `Enter`

2. **Using New Folder Icon**
   - Click the folder icon in Explorer toolbar
   - Type folder name

### File Naming Best Practices
- Use descriptive names
- Avoid spaces (use hyphens or underscores)
- Include appropriate file extensions
- Follow project naming conventions

**Examples:**
- `index.html`
- `main-styles.css`
- `user_authentication.py`
- `api-endpoints.js`

## Opening Files and Folders

### Opening Individual Files
1. **File Menu:** File > Open File (`Ctrl+O`)
2. **Drag and Drop:** Drag files into VS Code window
3. **Quick Open:** Press `Ctrl+P` and type filename
4. **Recent Files:** File > Open Recent

### Opening Folders/Projects
1. **File Menu:** File > Open Folder (`Ctrl+K Ctrl+O`)
2. **Drag and Drop:** Drag folder into VS Code
3. **Command Line:** `code .` to open current directory
4. **From Terminal:** `code /path/to/project`

### Opening Multiple Folders
- File > Add Folder to Workspace
- Create multi-root workspaces
- Useful for related projects

## File Navigation Techniques

### Quick Open (`Ctrl+P`)
- Type filename to quickly jump to files
- Fuzzy search - doesn't need exact spelling
- Recent files appear at the top

**Advanced Quick Open:**
- `filename:line` - Go to specific line
- `@symbol` - Navigate to symbols in file
- `#text` - Search across all files
- `:42` - Go to line 42

### Explorer Panel Navigation
- **Expand/Collapse:** Click arrows or use `Space`
- **Navigate:** Use arrow keys
- **Open:** Press `Enter` or double-click
- **Rename:** Press `F2` or right-click > Rename

### Breadcrumb Navigation
- Shows file path at top of editor
- Click any part to navigate up the hierarchy
- Use `Ctrl+Shift+.` to focus breadcrumbs

## Working with Multiple Files

### Tabs Management
- **New Tab:** `Ctrl+N`
- **Close Tab:** `Ctrl+W`
- **Switch Tabs:** `Ctrl+Tab` or `Ctrl+PageUp/PageDown`
- **Close All:** `Ctrl+K Ctrl+W`
- **Reopen Closed:** `Ctrl+Shift+T`

### Split Editor Views
1. **Split Right:** `Ctrl+\`
2. **Split Down:** `Ctrl+K Ctrl+\`
3. **Move Between Groups:** `Ctrl+1`, `Ctrl+2`, `Ctrl+3`
4. **Move File to Group:** Drag tab to desired group

### Tab Management Tips
- Pin important tabs (right-click > Pin Tab)
- Use `Ctrl+K Enter` to keep tab open permanently
- Right-click tabs for context menu options

## File Operations

### Saving Files
- **Save:** `Ctrl+S`
- **Save As:** `Ctrl+Shift+S`
- **Save All:** `Ctrl+K S`
- **Auto Save:** Enable in settings for automatic saving

### Auto Save Configuration
1. Go to Settings (`Ctrl+,`)
2. Search for "auto save"
3. Options:
   - `off` - Never auto save
   - `afterDelay` - Save after typing stops
   - `onFocusChange` - Save when switching files
   - `onWindowChange` - Save when switching windows

### Copying, Moving, and Deleting
1. **Copy Files:**
   - Right-click > Copy
   - Paste in destination folder

2. **Move Files:**
   - Drag and drop in Explorer
   - Cut (`Ctrl+X`) and Paste (`Ctrl+V`)

3. **Delete Files:**
   - Press `Delete` key
   - Right-click > Delete
   - Move to Recycle Bin (can be recovered)

4. **Rename Files:**
   - Press `F2`
   - Right-click > Rename
   - Slow double-click on filename

## File Search and Filtering

### Search in Explorer
- Type while Explorer is focused
- Files matching search appear highlighted
- Clear search with `Escape`

### Files to Exclude
- Configure in settings or workspace
- Hide generated files, dependencies
- Example: `node_modules`, `.git`, `*.log`

## Working with Different File Types

### Language-Specific Features
VS Code automatically detects file types by extension:
- `.html` - HTML with tag completion
- `.css` - CSS with property suggestions
- `.js` - JavaScript with IntelliSense
- `.py` - Python with syntax checking
- `.md` - Markdown with preview

### Changing Language Mode
1. Click language in status bar
2. Or press `Ctrl+K M`
3. Select desired language
4. Affects syntax highlighting and features

## Project Structure Best Practices

### Typical Web Project Structure
```
my-project/
├── index.html
├── css/
│   ├── style.css
│   └── normalize.css
├── js/
│   ├── main.js
│   └── utils.js
├── images/
│   └── logo.png
└── README.md
```

### Python Project Structure
```
my-python-project/
├── main.py
├── src/
│   ├── __init__.py
│   ├── models.py
│   └── utils.py
├── tests/
│   └── test_main.py
├── requirements.txt
└── README.md
```

## Practical Exercises

### Exercise 1: Create a Simple Website Structure
1. Create a new folder called "my-website"
2. Inside it, create:
   - `index.html`
   - `css` folder with `style.css`
   - `js` folder with `script.js`
   - `images` folder
3. Practice navigating between files using different methods

### Exercise 2: File Operations Practice
1. Create 5 text files with different names
2. Practice renaming them
3. Create folders and move files between them
4. Use Quick Open to navigate between files
5. Try splitting the editor to view multiple files

### Exercise 3: Configure Auto Save
1. Open Settings
2. Enable auto save with a 1-second delay
3. Create a new file and test auto save functionality

## Keyboard Shortcuts Summary

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| New File | `Ctrl+N` | `Cmd+N` |
| Open File | `Ctrl+O` | `Cmd+O` |
| Open Folder | `Ctrl+K Ctrl+O` | `Cmd+K Cmd+O` |
| Save | `Ctrl+S` | `Cmd+S` |
| Save As | `Ctrl+Shift+S` | `Cmd+Shift+S` |
| Quick Open | `Ctrl+P` | `Cmd+P` |
| Close Tab | `Ctrl+W` | `Cmd+W` |
| Split Editor | `Ctrl+\` | `Cmd+\` |
| Switch Tabs | `Ctrl+Tab` | `Cmd+Tab` |
| Rename File | `F2` | `F2` |

## Tips and Tricks

1. **Workspace Settings:** Each project can have its own settings file
2. **File Associations:** Map file extensions to specific languages
3. **Exclude Patterns:** Hide irrelevant files from Explorer
4. **Sticky Scroll:** Keep function/class headers visible while scrolling
5. **File Nesting:** Group related files together in Explorer

## Common Issues and Solutions

### Issue: File Not Opening
- Check file permissions
- Ensure file isn't corrupted
- Try opening with different application first

### Issue: Can't See File Extensions
- Enable in Windows File Explorer settings
- VS Code shows extensions by default

### Issue: Too Many Open Tabs
- Use tab limits in settings
- Pin only essential tabs
- Use workspace switching for different projects

## Next Steps

In Episode 3, we'll explore:
- Essential VS Code extensions
- Installing and managing extensions
- Recommended extensions for different programming languages
- Creating your first extension setup

---

**Previous Episode:** Introduction to VS Code  
**Next Episode:** Essential Extensions  
**Duration:** Approximately 20-25 minutes  
**Prerequisites:** Episode 1 completed