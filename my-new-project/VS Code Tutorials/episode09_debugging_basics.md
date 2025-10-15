# Episode 9: Debugging Basics

## Overview
Debugging is an essential skill for developers. VS Code provides powerful debugging capabilities for multiple programming languages, making it easier to find and fix issues in your code. This episode covers debugging setup, breakpoints, debug console, and debugging different types of applications.

## Understanding Debugging in VS Code

### What is Debugging?
Debugging allows you to:
- **Pause execution** at specific points (breakpoints)
- **Inspect variables** and their values
- **Step through code** line by line
- **Evaluate expressions** in real-time
- **Identify and fix bugs** efficiently

### Debug Components
- **Debug Console** - Execute commands and evaluate expressions
- **Variables Panel** - View and modify variable values
- **Call Stack** - See function call hierarchy
- **Breakpoints Panel** - Manage all breakpoints
- **Watch Panel** - Monitor specific expressions

## Setting Up Debugging

### Debug Configuration

#### Launch.json File
The `launch.json` file defines debug configurations:
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Launch Program",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/app.js",
      "skipFiles": ["<node_internals>/**"]
    }
  ]
}
```

#### Creating Debug Configuration
1. **Open Run and Debug panel** (`Ctrl+Shift+D`)
2. **Click "create a launch.json file"**
3. **Select environment** (Node.js, Python, etc.)
4. **Customize configuration** as needed

### Auto-generated Configurations

#### Node.js Configuration
```json
{
  "name": "Launch Node.js",
  "type": "node",
  "request": "launch",
  "program": "${file}",
  "console": "integratedTerminal",
  "skipFiles": ["<node_internals>/**"]
}
```

#### Python Configuration
```json
{
  "name": "Python: Current File",
  "type": "python",
  "request": "launch",
  "program": "${file}",
  "console": "integratedTerminal"
}
```

#### Browser/HTML Configuration
```json
{
  "name": "Launch Chrome",
  "type": "chrome",
  "request": "launch",
  "url": "http://localhost:3000",
  "webRoot": "${workspaceFolder}"
}
```

## Working with Breakpoints

### Types of Breakpoints

#### Regular Breakpoints
- **Set breakpoint:** Click in gutter next to line number
- **Red circle** indicates active breakpoint
- **Hollow circle** indicates disabled breakpoint
- **Remove:** Click breakpoint again

#### Conditional Breakpoints
- **Right-click** in gutter > "Add Conditional Breakpoint"
- **Expression:** `count > 10`
- **Hit Count:** `5` (break on 5th hit)

```javascript
// Example: Break only when user is admin
function processUser(user) {
  // Conditional breakpoint: user.role === 'admin'
  if (user.isActive) {
    // Process user logic
    console.log(`Processing ${user.name}`);
  }
}
```

#### Logpoints
- **Right-click** in gutter > "Add Logpoint"
- **Logs message** without stopping execution
- **Syntax:** `Count: {count}, User: {user.name}`

### Breakpoint Management

#### Breakpoints Panel
- **View all breakpoints** in one place
- **Enable/disable** individual breakpoints
- **Remove all breakpoints**
- **Export/import** breakpoint configurations

#### Breakpoint Actions
```
Ctrl+F9        - Toggle breakpoint
Ctrl+Shift+F9  - Toggle inline breakpoint
F9             - Toggle breakpoint (alternative)
```

## Debug Execution Control

### Stepping Through Code

#### Step Controls
- **Continue (F5)** - Run until next breakpoint
- **Step Over (F10)** - Execute current line, don't enter functions
- **Step Into (F11)** - Enter function calls
- **Step Out (Shift+F11)** - Exit current function
- **Restart (Ctrl+Shift+F5)** - Restart debugging session
- **Stop (Shift+F5)** - Stop debugging

#### Stepping Example
```javascript
function calculateTotal(items) {
  let total = 0;                    // 1. Set breakpoint here
  
  for (let item of items) {         // 2. Step Over (F10)
    total += calculatePrice(item);  // 3. Step Into (F11) to enter function
  }                                 // 4. Step Out to return
  
  return total;                     // 5. Continue (F5)
}

function calculatePrice(item) {
  return item.price * item.quantity;
}
```

### Run to Cursor
- **Right-click** on line > "Run to Cursor"
- **Ctrl+F10** keyboard shortcut
- Executes until specified line

## Debug Panels and Information

### Variables Panel

#### Viewing Variables
- **Local variables** - Current scope
- **Global variables** - Application-wide
- **Closure variables** - From outer scopes

#### Modifying Variables
1. **Right-click variable** > "Set Value"
2. **Enter new value**
3. **Continue execution** with modified state

```javascript
function processOrder(order) {
  let discount = 0.1;        // Can modify this value during debugging
  let total = order.amount;  // Watch this variable change
  
  if (order.isVip) {
    discount = 0.2;          // Breakpoint here to inspect values
  }
  
  return total * (1 - discount);
}
```

### Watch Panel

#### Adding Watch Expressions
- **Click "+" in Watch panel**
- **Enter expression:** `user.orders.length`
- **Monitor value** throughout execution

#### Common Watch Expressions
```javascript
// Basic variable watching
user.name
order.total

// Complex expressions
items.filter(item => item.price > 100).length
JSON.stringify(response)

// Function calls (be careful with side effects)
getCurrentTime()
```

### Call Stack Panel

#### Understanding Call Stack
- **Shows function call hierarchy**
- **Click stack frame** to navigate
- **Examine variables** in different scopes

```javascript
function main() {
  processUser(userData);     // 3. Third in call stack
}

function processUser(user) {
  validateUser(user);        // 2. Second in call stack
}

function validateUser(user) {
  // 1. Current execution point
  if (!user.email) {
    throw new Error("Email required");
  }
}
```

### Debug Console

#### Interactive Debugging
- **Execute JavaScript** in current context
- **Evaluate expressions** and variables
- **Call functions** with current scope

#### Console Commands
```javascript
// Evaluate variables
> user.name
"John Doe"

// Test expressions
> user.age > 18
true

// Call functions
> calculateTotal(items)
150.50

// Modify variables
> discount = 0.15
0.15
```

## Language-Specific Debugging

### JavaScript/Node.js Debugging

#### Basic Node.js Setup
```json
{
  "name": "Launch Node.js",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/server.js",
  "env": {
    "NODE_ENV": "development"
  },
  "console": "integratedTerminal",
  "skipFiles": ["<node_internals>/**"]
}
```

#### Attach to Running Process
```json
{
  "name": "Attach to Node.js",
  "type": "node",
  "request": "attach",
  "port": 9229,
  "restart": true,
  "localRoot": "${workspaceFolder}",
  "remoteRoot": "."
}
```

#### Starting Node.js with Debugging
```bash
# Start with debugging enabled
node --inspect server.js

# Start with debugging and break on first line
node --inspect-brk server.js

# Specific port
node --inspect=9229 server.js
```

### Browser Debugging

#### Chrome DevTools Integration
```json
{
  "name": "Launch Chrome",
  "type": "chrome",
  "request": "launch",
  "url": "http://localhost:3000",
  "webRoot": "${workspaceFolder}/src",
  "sourceMapPathOverrides": {
    "webpack:///src/*": "${webRoot}/*"
  }
}
```

#### Debugging React Applications
```json
{
  "name": "Debug React App",
  "type": "chrome",
  "request": "launch",
  "url": "http://localhost:3000",
  "webRoot": "${workspaceFolder}/src",
  "sourceMapPathOverrides": {
    "webpack:///src/*": "${webRoot}/*",
    "webpack:///./src/*": "${webRoot}/*"
  }
}
```

### Python Debugging

#### Basic Python Configuration
```json
{
  "name": "Python: Current File",
  "type": "python",
  "request": "launch",
  "program": "${file}",
  "console": "integratedTerminal",
  "args": ["--verbose"]
}
```

#### Django Debugging
```json
{
  "name": "Django",
  "type": "python",
  "request": "launch",
  "program": "${workspaceFolder}/manage.py",
  "args": ["runserver", "127.0.0.1:8000"],
  "django": true
}
```

#### Flask Debugging
```json
{
  "name": "Flask",
  "type": "python",
  "request": "launch",
  "program": "${workspaceFolder}/app.py",
  "env": {
    "FLASK_APP": "app.py",
    "FLASK_ENV": "development"
  }
}
```

### C/C++ Debugging

#### GDB Configuration
```json
{
  "name": "C++ Debug",
  "type": "cppdbg",
  "request": "launch",
  "program": "${workspaceFolder}/build/main",
  "args": [],
  "stopAtEntry": false,
  "cwd": "${workspaceFolder}",
  "environment": [],
  "MIMode": "gdb",
  "setupCommands": [
    {
      "description": "Enable pretty-printing for gdb",
      "text": "-enable-pretty-printing",
      "ignoreFailures": true
    }
  ]
}
```

## Advanced Debugging Techniques

### Remote Debugging

#### Remote Node.js Debugging
```json
{
  "name": "Remote Node.js",
  "type": "node",
  "request": "attach",
  "address": "192.168.1.100",
  "port": 9229,
  "localRoot": "${workspaceFolder}",
  "remoteRoot": "/app"
}
```

#### SSH Remote Debugging
- Use Remote-SSH extension
- Debug applications on remote servers
- Seamless local debugging experience

### Debugging Tests

#### Jest Testing Framework
```json
{
  "name": "Debug Jest Tests",
  "type": "node",
  "request": "launch",
  "runtimeArgs": [
    "--inspect-brk",
    "${workspaceFolder}/node_modules/.bin/jest",
    "--runInBand"
  ],
  "console": "integratedTerminal",
  "internalConsoleOptions": "neverOpen"
}
```

#### Python Unit Tests
```json
{
  "name": "Debug Python Tests",
  "type": "python",
  "request": "launch",
  "module": "pytest",
  "args": ["tests/", "-v"],
  "console": "integratedTerminal"
}
```

### Exception Handling

#### Uncaught Exceptions
```json
{
  "name": "Node.js with Exception Handling",
  "type": "node",
  "request": "launch",
  "program": "${file}",
  "stopOnEntry": false,
  "console": "integratedTerminal",
  "uncaughtException": true
}
```

#### Python Exception Handling
```json
{
  "name": "Python with Exceptions",
  "type": "python",
  "request": "launch",
  "program": "${file}",
  "console": "integratedTerminal",
  "justMyCode": false
}
```

## Debugging Best Practices

### Effective Breakpoint Usage

#### Strategic Breakpoint Placement
```javascript
function processOrder(order) {
  // 1. Set breakpoint at function entry
  if (!order) {
    return null;
  }
  
  // 2. Breakpoint before complex logic
  const items = order.items || [];
  let total = 0;
  
  // 3. Conditional breakpoint in loops
  for (const item of items) {
    // Condition: item.price > 100
    total += item.price * item.quantity;
  }
  
  // 4. Breakpoint before return
  return {
    orderId: order.id,
    total: total,
    timestamp: new Date()
  };
}
```

### Debug Information

#### Adding Debug Information
```javascript
// Use console.log strategically
function calculateDiscount(user, amount) {
  console.log('Calculating discount for:', user.email, 'amount:', amount);
  
  let discount = 0;
  
  if (user.isPremium) {
    discount = amount * 0.1;
    console.log('Premium discount applied:', discount);
  }
  
  console.log('Final discount:', discount);
  return discount;
}
```

#### Using Logpoints
- Replace temporary console.log statements
- No need to modify source code
- Can include expressions and variables

### Performance Debugging

#### Profiling Integration
- Use browser developer tools for performance
- Node.js profiling with --prof flag
- Memory usage debugging

#### Common Performance Issues
```javascript
// Inefficient code that might need debugging
function findUserById(users, id) {
  // O(n) operation - might be slow for large arrays
  return users.find(user => user.id === id);
}

// Better approach with debugging
function findUserById(users, id) {
  console.time('findUser');
  const result = users.find(user => user.id === id);
  console.timeEnd('findUser');
  return result;
}
```

## Troubleshooting Debug Issues

### Common Debugging Problems

#### Source Maps Not Working
```json
{
  "name": "Debug with Source Maps",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/dist/app.js",
  "outFiles": ["${workspaceFolder}/dist/**/*.js"],
  "sourceMaps": true
}
```

#### Path Resolution Issues
```json
{
  "name": "Fixed Path Debug",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/src/index.js",
  "cwd": "${workspaceFolder}",
  "resolveSourceMapLocations": [
    "${workspaceFolder}/**",
    "!**/node_modules/**"
  ]
}
```

#### Port Conflicts
```bash
# Find processes using port
netstat -an | grep :9229
lsof -i :9229

# Kill process if needed
kill -9 <process-id>
```

### Debug Console Troubleshooting

#### Console Not Responding
1. **Check debug session** is active
2. **Verify breakpoint** is hit
3. **Restart debug session**
4. **Check console scope**

#### Variable Not Found
```javascript
// Ensure variable is in scope
function testFunction() {
  let localVar = "test";
  debugger; // Variables available here: localVar
}

let globalVar = "global";
debugger; // Variables available here: globalVar
```

## Practical Exercises

### Exercise 1: Basic Debugging Setup
1. Create a simple Node.js or Python application
2. Set up debug configuration
3. Add breakpoints and start debugging
4. Practice stepping through code

### Exercise 2: Variable Inspection
1. Create a function with local variables
2. Add breakpoints inside the function
3. Inspect and modify variables during execution
4. Use watch expressions to monitor values

### Exercise 3: Conditional Debugging
1. Create a loop with conditional logic
2. Set conditional breakpoints
3. Use logpoints to trace execution
4. Debug only specific conditions

### Exercise 4: Exception Debugging
1. Create code that throws exceptions
2. Configure debugger to break on exceptions
3. Examine call stack when exception occurs
4. Fix the issues found during debugging

## Debug Configuration Examples

### Complete Node.js Configuration
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Launch App",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/app.js",
      "args": ["--port", "3000"],
      "env": {
        "NODE_ENV": "development",
        "DEBUG": "app:*"
      },
      "console": "integratedTerminal",
      "skipFiles": ["<node_internals>/**"],
      "restart": true
    },
    {
      "name": "Attach to Process",
      "type": "node",
      "request": "attach",
      "port": 9229,
      "restart": true
    }
  ]
}
```

### Multi-Configuration Setup
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug Frontend",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:3000"
    },
    {
      "name": "Debug Backend",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/server.js"
    }
  ],
  "compounds": [
    {
      "name": "Debug Full Stack",
      "configurations": ["Debug Frontend", "Debug Backend"]
    }
  ]
}
```

## Next Steps

In Episode 10, we'll explore:
- Creating and managing workspaces
- Multi-folder projects
- Workspace settings and configuration
- Project templates and organization

---

**Previous Episode:** Git Integration  
**Next Episode:** Workspace Management  
**Duration:** Approximately 35-40 minutes  
**Prerequisites:** Episodes 1-8 completed, basic programming knowledge