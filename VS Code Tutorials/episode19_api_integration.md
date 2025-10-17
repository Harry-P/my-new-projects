# Episode 19 — API Integration & External Tools

## Why integrate with external tools?
Modern development often requires connecting VS Code with external APIs, databases, cloud services, and development tools. This episode covers strategies for seamless integration.

## REST API integration

### Using VS Code extensions for API testing

#### REST Client extension
Install the REST Client extension and create `.http` files:

```http
### Get all users
GET https://jsonplaceholder.typicode.com/users
Content-Type: application/json

### Create a new user
POST https://jsonplaceholder.typicode.com/users
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "username": "johndoe"
}

### Get user by ID
GET https://jsonplaceholder.typicode.com/users/1

### Update user
PUT https://jsonplaceholder.typicode.com/users/1
Content-Type: application/json

{
  "name": "Jane Doe Updated",
  "email": "jane.updated@example.com"
}
```

#### Thunder Client extension
Alternative GUI-based REST client:
1. Install Thunder Client
2. Create collections for your APIs
3. Set up environments (dev, staging, prod)
4. Export/import collections for team sharing

### Environment variables in API testing
Create `.vscode/settings.json`:
```json
{
  "rest-client.environmentVariables": {
    "local": {
      "baseUrl": "http://localhost:3000",
      "token": "dev-token-123"
    },
    "production": {
      "baseUrl": "https://api.myapp.com",
      "token": "{{$processEnv TOKEN}}"
    }
  }
}
```

## Database integration

### Database extensions

#### MySQL/PostgreSQL
```sql
-- Create a .sql file and use MySQL extension
SELECT * FROM users 
WHERE created_at >= '2023-01-01'
ORDER BY name;

-- With parameters
SELECT * FROM products 
WHERE category = @category 
AND price BETWEEN @min_price AND @max_price;
```

#### MongoDB
```javascript
// Use MongoDB for VS Code extension
// Create .mongodb files
use('myDatabase');

db.users.find({
  status: 'active',
  lastLogin: { $gte: new Date('2023-01-01') }
});

db.products.aggregate([
  { $match: { category: 'electronics' } },
  { $group: { _id: '$brand', totalSales: { $sum: '$sales' } } },
  { $sort: { totalSales: -1 } }
]);
```

### Database connection configuration
```json
{
  "mssql.connections": [
    {
      "connectionString": "Server=localhost;Database=TestDB;Trusted_Connection=true;",
      "profileName": "LocalDB",
      "password": ""
    }
  ]
}
```

## Cloud service integration

### AWS integration
Install AWS Toolkit extension:

```yaml
# Configure AWS credentials in tasks.json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Deploy to AWS",
      "type": "shell",
      "command": "aws",
      "args": [
        "s3",
        "sync",
        "./dist",
        "s3://my-bucket",
        "--delete"
      ],
      "group": "build"
    }
  ]
}
```

### Azure integration
```json
{
  "azureFunctions.projectRuntime": "~4",
  "azureFunctions.projectLanguage": "JavaScript",
  "azureFunctions.deploySubpath": "dist"
}
```

### Google Cloud integration
```bash
# Configure gcloud CLI
gcloud auth login
gcloud config set project my-project-id

# Deploy from VS Code terminal
gcloud app deploy
```

## CI/CD integration

### GitHub Actions
Create `.github/workflows/ci.yml`:
```yaml
name: CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm test
      - run: npm run build
```

### GitLab CI
Create `.gitlab-ci.yml`:
```yaml
stages:
  - test
  - build
  - deploy

test:
  stage: test
  script:
    - npm ci
    - npm test

build:
  stage: build
  script:
    - npm run build
  artifacts:
    paths:
      - dist/
```

## Container integration

### Docker integration
Install Docker extension and create `Dockerfile`:
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

Create `.vscode/tasks.json` for Docker commands:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Docker Build",
      "type": "shell",
      "command": "docker",
      "args": ["build", "-t", "my-app", "."],
      "group": "build"
    },
    {
      "label": "Docker Run",
      "type": "shell",
      "command": "docker",
      "args": ["run", "-p", "3000:3000", "my-app"],
      "group": "test"
    }
  ]
}
```

### Kubernetes integration
```yaml
# k8s-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app:latest
        ports:
        - containerPort: 3000
```

## Version control integration

### Advanced Git workflows
```json
{
  "git.postCommitCommand": "sync",
  "git.enableCommitSigning": true,
  "git.rebaseWhenSync": true,
  "gitflow.hotfixPrefix": "hotfix/",
  "gitflow.featurePrefix": "feature/"
}
```

### Pre-commit hooks
Create `.husky/pre-commit`:
```bash
#!/bin/sh
npm run lint
npm test
```

## Package manager integration

### npm/yarn integration
```json
{
  "npm.packageManager": "yarn",
  "npm.enableRunFromFolder": true,
  "npm.exclude": "**/node_modules/**"
}
```

### Tasks for package management
```json
{
  "tasks": [
    {
      "label": "Install Dependencies",
      "type": "shell",
      "command": "npm",
      "args": ["install"],
      "group": "build"
    },
    {
      "label": "Update Dependencies",
      "type": "shell",
      "command": "npm",
      "args": ["update"],
      "group": "build"
    }
  ]
}
```

## External editor integration

### Vim/Neovim integration
Install Vim extension:
```json
{
  "vim.easymotion": true,
  "vim.sneak": true,
  "vim.incsearch": true,
  "vim.useSystemClipboard": true,
  "vim.useCtrlKeys": true
}
```

### Emacs keybindings
```json
{
  "editor.multiCursorModifier": "ctrlCmd",
  "workbench.list.multiSelectModifier": "ctrlCmd"
}
```

## Productivity tool integration

### Note-taking integration
```json
{
  "markdown.preview.fontSize": 14,
  "markdown.preview.lineHeight": 1.6,
  "markdown.extensions": [
    "mermaid",
    "katex"
  ]
}
```

### Time tracking integration
Configure with extensions like:
- WakaTime for automatic time tracking
- Code Time for productivity metrics
- GitLens for Git activity insights

## Custom tool integration

### Creating custom tasks
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Custom Tool",
      "type": "shell",
      "command": "python",
      "args": ["scripts/custom_tool.py", "${file}"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      }
    }
  ]
}
```

### External command integration
```python
# scripts/format_json.py
import json
import sys

def format_json_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)

if __name__ == "__main__":
    format_json_file(sys.argv[1])
```

## Security considerations

### API key management
Never commit API keys! Use:
- Environment variables
- VS Code settings (user-level)
- External secret managers

```json
{
  "terminal.integrated.env.windows": {
    "API_KEY": "${env:MY_API_KEY}"
  }
}
```

### Secure connection practices
```json
{
  "http.proxy": "http://proxy.company.com:8080",
  "http.proxyStrictSSL": true,
  "http.proxyAuthorization": null
}
```

## Team collaboration

### Shared integration configs
Create `.vscode/settings.json` for team:
```json
{
  "api.baseUrl": "https://api.staging.myapp.com",
  "database.connectionString": "postgresql://localhost:5432/myapp_dev",
  "docker.buildArgs": {
    "NODE_ENV": "development"
  }
}
```

### Documentation template
```markdown
# API Integration Guide

## Required Setup
1. Install REST Client extension
2. Copy `.env.example` to `.env`
3. Set API_KEY in environment variables

## Available Endpoints
- User management: `api/users.http`
- Product catalog: `api/products.http`
- Orders: `api/orders.http`

## Database Access
Use the PostgreSQL extension with connection string:
`postgresql://localhost:5432/myapp_dev`
```

## Troubleshooting integration issues

### Common problems
1. **Authentication failures**: Check API keys and tokens
2. **Network timeouts**: Verify proxy settings
3. **Extension conflicts**: Disable conflicting extensions
4. **Environment issues**: Verify environment variables

### Debugging tools
- Use VS Code's built-in terminal for CLI tools
- Check extension output panels for errors
- Monitor network requests in developer tools
- Use logging in custom scripts

Effective tool integration makes VS Code the central hub for your entire development workflow!