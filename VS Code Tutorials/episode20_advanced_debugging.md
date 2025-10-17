# Episode 20 — Advanced Debugging Techniques

## Beyond basic debugging
While Episode 9 covered debugging basics, this episode explores advanced debugging scenarios, complex configurations, and debugging across different environments and languages.

## Advanced breakpoint techniques

### Conditional breakpoints
Set breakpoints that only trigger when specific conditions are met:

```javascript
// Right-click on breakpoint and add condition
user.age > 18 && user.isActive === true

// Or use expressions
users.length > 100

// String conditions
user.name.includes('admin')
```

### Logpoints (non-breaking breakpoints)
Log messages without stopping execution:
```javascript
// Add logpoint with expression
console.log('User processed: {user.name}, Age: {user.age}')

// Conditional logpoints
user.role === 'admin' ? 'Admin user: {user.name}' : ''
```

### Hit count breakpoints
Break only after a certain number of hits:
- Hit count: `> 10` (break after 10th hit)
- Hit count: `= 5` (break only on 5th hit)
- Hit count: `% 3 === 0` (break every 3rd hit)

### Function breakpoints
Break when entering specific functions:
```javascript
// Set breakpoint on function name in Call Stack
// Or use Debug Console:
debug.setBreakpoint('myFunction')
```

## Multi-language debugging

### Node.js + Frontend debugging
Configure compound debugging in `launch.json`:
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Launch Backend",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/server/index.js",
      "env": {
        "NODE_ENV": "development"
      },
      "port": 9229
    },
    {
      "name": "Launch Frontend",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:3000",
      "webRoot": "${workspaceFolder}/client/src"
    }
  ],
  "compounds": [
    {
      "name": "Launch Full Stack",
      "configurations": ["Launch Backend", "Launch Frontend"]
    }
  ]
}
```

### Python debugging with different interpreters
```json
{
  "name": "Python: Django",
  "type": "python",
  "request": "launch",
  "program": "${workspaceFolder}/manage.py",
  "args": ["runserver", "8000"],
  "django": true,
  "justMyCode": false,
  "python": "${workspaceFolder}/venv/bin/python"
}
```

### Docker container debugging
```json
{
  "name": "Docker: Attach to Node",
  "type": "node",
  "request": "attach",
  "port": 9229,
  "address": "localhost",
  "localRoot": "${workspaceFolder}",
  "remoteRoot": "/app",
  "protocol": "inspector"
}
```

## Remote debugging

### SSH remote debugging
```json
{
  "name": "Attach to Remote Node",
  "type": "node",
  "request": "attach",
  "address": "192.168.1.100",
  "port": 9229,
  "localRoot": "${workspaceFolder}",
  "remoteRoot": "/home/user/app"
}
```

### WSL debugging
```json
{
  "name": "Python: WSL",
  "type": "python",
  "request": "launch",
  "program": "${workspaceFolder}/app.py",
  "console": "integratedTerminal",
  "pathMappings": [
    {
      "localRoot": "${workspaceFolder}",
      "remoteRoot": "/mnt/c/Users/username/project"
    }
  ]
}
```

## Advanced debugging configurations

### Environment-specific debugging
```json
{
  "name": "Debug Production Issue",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/dist/index.js",
  "env": {
    "NODE_ENV": "production",
    "DEBUG": "app:*",
    "LOG_LEVEL": "debug"
  },
  "sourceMaps": true,
  "outFiles": ["${workspaceFolder}/dist/**/*.js"]
}
```

### Testing framework debugging
```json
{
  "name": "Debug Jest Tests",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/node_modules/.bin/jest",
  "args": ["--runInBand", "--no-cache", "${fileBasenameNoExtension}"],
  "cwd": "${workspaceFolder}",
  "console": "integratedTerminal"
}
```

### Microservices debugging
```json
{
  "name": "Debug Microservice",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/services/user-service/index.js",
  "env": {
    "SERVICE_PORT": "3001",
    "DATABASE_URL": "postgresql://localhost:5432/users_dev"
  },
  "envFile": "${workspaceFolder}/.env.local"
}
```

## Performance debugging

### CPU profiling
```json
{
  "name": "Profile CPU",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/app.js",
  "profilerMode": "cpu",
  "outputCapture": "console"
}
```

### Memory leak debugging
```javascript
// Use Debug Console commands:
// Check memory usage
process.memoryUsage()

// Force garbage collection
global.gc()

// Heap snapshot (with --inspect flag)
// Use Chrome DevTools Memory tab
```

### Slow query debugging
```json
{
  "name": "Debug Slow Queries",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/app.js",
  "env": {
    "DEBUG": "sequelize:sql",
    "NODE_ENV": "development"
  }
}
```

## Advanced debugging tools

### Debug Console advanced usage
```javascript
// Evaluate complex expressions
JSON.stringify(complexObject, null, 2)

// Call functions
myFunction('test parameter')

// Access scope variables
$0  // Last selected element in Elements panel
$_  // Result of last expression

// Debug utility functions
console.table(arrayOfObjects)
console.time('operation')
console.timeEnd('operation')
```

### Source map debugging
```json
{
  "name": "Debug TypeScript",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/dist/app.js",
  "sourceMaps": true,
  "outFiles": [
    "${workspaceFolder}/dist/**/*.js"
  ],
  "preLaunchTask": "tsc: build"
}
```

### Exception handling
```json
{
  "name": "Debug with Exception Handling",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/app.js",
  "stopOnEntry": false,
  "exceptionOptions": {
    "uncaught": "stop",
    "caught": "ignore"
  }
}
```

## Debugging different architectures

### Monorepo debugging
```json
{
  "name": "Debug Package A",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/packages/package-a/index.js",
  "cwd": "${workspaceFolder}/packages/package-a"
}
```

### Serverless function debugging
```json
{
  "name": "Debug Lambda",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/node_modules/.bin/serverless",
  "args": ["invoke", "local", "--function", "hello"],
  "env": {
    "IS_OFFLINE": "true"
  }
}
```

### API debugging with middleware
```javascript
// Express middleware debugging
app.use((req, res, next) => {
  console.log(`${req.method} ${req.path}`);
  // Set breakpoint here to debug all requests
  next();
});
```

## Browser debugging integration

### Chrome DevTools integration
```json
{
  "name": "Debug Chrome",
  "type": "chrome",
  "request": "launch",
  "url": "http://localhost:3000",
  "webRoot": "${workspaceFolder}/src",
  "userDataDir": false,
  "runtimeArgs": [
    "--disable-web-security",
    "--disable-features=VizDisplayCompositor"
  ]
}
```

### Edge debugging
```json
{
  "name": "Debug Edge",
  "type": "msedge",
  "request": "launch",
  "url": "http://localhost:3000",
  "webRoot": "${workspaceFolder}"
}
```

## Advanced debugging workflows

### Debug tasks integration
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start Debug Server",
      "type": "shell",
      "command": "npm run dev:debug",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "."
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Starting development server",
          "endsPattern": "Debugger listening on port 9229"
        }
      }
    }
  ]
}
```

### Pre-launch tasks
```json
{
  "name": "Debug with Build",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/dist/app.js",
  "preLaunchTask": "build",
  "postDebugTask": "cleanup"
}
```

## Debugging production issues

### Production debugging setup
```json
{
  "name": "Debug Production Replica",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/app.js",
  "env": {
    "NODE_ENV": "production",
    "DATABASE_URL": "postgresql://localhost:5432/app_production_replica",
    "REDIS_URL": "redis://localhost:6379/1"
  }
}
```

### Log-based debugging
```javascript
// Structured logging for debugging
const debug = require('debug');
const log = debug('app:user');

function processUser(user) {
  log('Processing user: %O', user);
  // Debug conditional logging
  if (debug.enabled('app:user')) {
    console.time('user-processing');
  }
  
  // Your logic here
  
  if (debug.enabled('app:user')) {
    console.timeEnd('user-processing');
  }
}
```

## Debugging best practices

### Debugging checklist
1. ✅ Use descriptive breakpoint conditions
2. ✅ Leverage logpoints for non-intrusive debugging
3. ✅ Set up compound configurations for complex apps
4. ✅ Use source maps for compiled languages
5. ✅ Configure exception handling appropriately
6. ✅ Use performance profiling for optimization

### Team debugging workflows
```markdown
# Debugging Runbook

## Before Debugging
1. Reproduce the issue locally
2. Check recent commits for related changes
3. Review error logs and stack traces
4. Identify the affected components

## Debugging Session
1. Start with the most likely cause
2. Use conditional breakpoints to narrow scope
3. Document findings in issue tracker
4. Share debugging configurations with team

## After Debugging
1. Add regression tests
2. Update documentation
3. Share learnings with team
4. Update debugging configurations
```

### Performance debugging tips
- Use CPU profiler for performance bottlenecks
- Memory snapshots for leak detection
- Network throttling for connection issues
- Timeline analysis for rendering problems

## Troubleshooting debugging issues

### Common problems
- **Breakpoints not hit**: Check source maps, file paths
- **Variables not accessible**: Verify scope and context
- **Slow debugging**: Reduce breakpoint count, optimize conditions
- **Source maps broken**: Rebuild with proper map generation

### Debug configuration validation
```json
{
  "name": "Validate Debug Setup",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/debug-test.js",
  "console": "integratedTerminal",
  "trace": true
}
```

Advanced debugging transforms complex problems into manageable investigations—master these techniques to debug like a pro!