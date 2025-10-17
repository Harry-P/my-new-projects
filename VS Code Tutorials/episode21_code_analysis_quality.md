# Episode 21 — Code Analysis & Quality Tools

## Beyond syntax highlighting
Modern development requires sophisticated code analysis to maintain quality, catch bugs early, and enforce standards. This episode covers integrating powerful analysis tools with VS Code.

## Static analysis fundamentals

### ESLint for JavaScript/TypeScript
Install and configure ESLint:
```bash
npm install -g eslint
eslint --init
```

Configure in `.eslintrc.json`:
```json
{
  "extends": [
    "eslint:recommended",
    "@typescript-eslint/recommended",
    "prettier"
  ],
  "parser": "@typescript-eslint/parser",
  "plugins": ["@typescript-eslint", "import", "security"],
  "rules": {
    "no-console": "warn",
    "no-unused-vars": "error",
    "prefer-const": "error",
    "no-var": "error",
    "security/detect-object-injection": "warn",
    "import/order": ["error", {
      "groups": ["builtin", "external", "internal", "parent", "sibling", "index"]
    }]
  },
  "env": {
    "node": true,
    "browser": true,
    "es2022": true
  }
}
```

### Pylint/Flake8 for Python
Configure in `pyproject.toml`:
```toml
[tool.pylint.messages_control]
disable = ["C0111", "C0103"]

[tool.pylint.format]
max-line-length = 88

[tool.flake8]
max-line-length = 88
extend-ignore = ["E203", "W503"]
exclude = [".git", "__pycache__", "venv"]
```

### SonarLint integration
Install SonarLint extension for advanced code analysis:
```json
{
  "sonarlint.rules": {
    "javascript:S1481": "off",
    "typescript:S1186": "info"
  },
  "sonarlint.connectedMode.project": {
    "connectionId": "my-sonarqube",
    "projectKey": "my-project"
  }
}
```

## Code quality metrics

### Complexity analysis
Configure complexity rules:
```json
{
  "eslint.rules": {
    "complexity": ["error", { "max": 10 }],
    "max-depth": ["error", 4],
    "max-nested-callbacks": ["error", 3],
    "max-params": ["error", 4]
  }
}
```

### Code coverage integration
Configure Jest with coverage:
```json
{
  "jest": {
    "collectCoverage": true,
    "coverageDirectory": "coverage",
    "coverageReporters": ["text", "lcov", "html"],
    "coverageThreshold": {
      "global": {
        "branches": 80,
        "functions": 80,
        "lines": 80,
        "statements": 80
      }
    }
  }
}
```

### Technical debt tracking
Use CodeClimate or similar:
```yaml
# .codeclimate.yml
version: "2"
checks:
  argument-count:
    config:
      threshold: 4
  complex-logic:
    config:
      threshold: 4
  file-lines:
    config:
      threshold: 250
  method-complexity:
    config:
      threshold: 5
```

## Security analysis

### Security linting
Configure security-focused linting:
```json
{
  "eslint": {
    "plugins": ["security"],
    "rules": {
      "security/detect-unsafe-regex": "error",
      "security/detect-buffer-noassert": "error",
      "security/detect-child-process": "warn",
      "security/detect-disable-mustache-escape": "error",
      "security/detect-eval-with-expression": "error",
      "security/detect-no-csrf-before-method-override": "error",
      "security/detect-non-literal-fs-filename": "warn",
      "security/detect-non-literal-regexp": "warn",
      "security/detect-non-literal-require": "warn",
      "security/detect-possible-timing-attacks": "warn",
      "security/detect-pseudoRandomBytes": "error"
    }
  }
}
```

### Dependency vulnerability scanning
Configure npm audit integration:
```json
{
  "scripts": {
    "audit": "npm audit --audit-level moderate",
    "audit:fix": "npm audit fix",
    "security:check": "npm run audit && snyk test"
  }
}
```

### Secrets detection
Use GitLeaks or similar tools:
```toml
# .gitleaks.toml
[rules]
  [[rules.rules]]
    description = "AWS Access Key"
    regex = '''(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}'''
    tags = ["key", "AWS"]

  [[rules.rules]]
    description = "Private Key"
    regex = '''-----BEGIN PRIVATE KEY-----'''
    tags = ["key", "private"]
```

## Performance analysis

### Bundle analysis for web projects
Configure webpack-bundle-analyzer:
```json
{
  "scripts": {
    "analyze": "npm run build && npx webpack-bundle-analyzer build/static/js/*.js"
  }
}
```

### Memory profiling integration
```javascript
// Add to package.json scripts
{
  "profile:memory": "node --inspect --max-old-space-size=4096 app.js",
  "profile:cpu": "node --prof app.js && node --prof-process isolate-*.log > profile.txt"
}
```

### Lighthouse CI integration
```json
{
  "ci": {
    "collect": {
      "url": ["http://localhost:3000"],
      "startServerCommand": "npm start"
    },
    "assert": {
      "assertions": {
        "categories:performance": ["warn", {"minScore": 0.9}],
        "categories:accessibility": ["error", {"minScore": 0.9}]
      }
    }
  }
}
```

## Custom analysis rules

### Creating custom ESLint rules
```javascript
// rules/no-console-log.js
module.exports = {
  meta: {
    type: "problem",
    docs: {
      description: "disallow console.log statements",
      category: "Best Practices"
    }
  },
  create(context) {
    return {
      CallExpression(node) {
        if (
          node.callee.type === "MemberExpression" &&
          node.callee.object.name === "console" &&
          node.callee.property.name === "log"
        ) {
          context.report({
            node,
            message: "Unexpected console.log statement."
          });
        }
      }
    };
  }
};
```

### Custom VS Code diagnostics
```typescript
// Create diagnostic provider
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  const diagnosticCollection = vscode.languages.createDiagnosticCollection('custom-analyzer');
  
  context.subscriptions.push(
    vscode.workspace.onDidChangeTextDocument((event) => {
      analyzeDDocument(event.document, diagnosticCollection);
    })
  );
}

function analyzeDocument(document: vscode.TextDocument, collection: vscode.DiagnosticCollection) {
  const diagnostics: vscode.Diagnostic[] = [];
  const text = document.getText();
  
  // Custom analysis logic
  const todoRegex = /TODO|FIXME|HACK/gi;
  let match;
  
  while ((match = todoRegex.exec(text)) !== null) {
    const diagnostic = new vscode.Diagnostic(
      new vscode.Range(
        document.positionAt(match.index),
        document.positionAt(match.index + match[0].length)
      ),
      `Found ${match[0]} comment`,
      vscode.DiagnosticSeverity.Information
    );
    diagnostics.push(diagnostic);
  }
  
  collection.set(document.uri, diagnostics);
}
```

## Automated quality gates

### Pre-commit hooks with Husky
```json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged && npm run test:coverage",
      "pre-push": "npm run lint && npm run test && npm run build"
    }
  },
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "eslint --fix",
      "prettier --write",
      "git add"
    ],
    "*.{css,scss,md}": [
      "prettier --write",
      "git add"
    ]
  }
}
```

### GitHub Actions quality pipeline
```yaml
# .github/workflows/quality.yml
name: Code Quality
on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Run linting
        run: npm run lint
        
      - name: Run tests with coverage
        run: npm run test:coverage
        
      - name: Run security audit
        run: npm audit --audit-level moderate
        
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage/lcov.info
```

## Code review automation

### Automated code review tools
Configure ReviewBoard or similar:
```yaml
# .reviewboardrc
REPOSITORY = 'git@github.com:company/project.git'
BRANCH = 'main'
TRACKING_BRANCH = 'origin/main'
```

### Pull request templates
```markdown
<!-- .github/pull_request_template.md -->
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Quality Checklist
- [ ] Tests added/updated
- [ ] Linting passes
- [ ] Coverage maintained/improved
- [ ] Security implications considered
- [ ] Performance impact assessed

## Screenshots (if applicable)

## Additional Notes
```

## Continuous monitoring

### SonarQube integration
```properties
# sonar-project.properties
sonar.projectKey=my-project
sonar.organization=my-org
sonar.sources=src
sonar.tests=tests
sonar.language=js
sonar.sourceEncoding=UTF-8
sonar.javascript.lcov.reportPaths=coverage/lcov.info
```

### Quality metrics dashboard
```json
{
  "scripts": {
    "quality:report": "npm run lint:report && npm run test:coverage && npm run complexity:report",
    "lint:report": "eslint . --format json --output-file reports/eslint.json",
    "complexity:report": "complexity-report --output reports/complexity.json src/**/*.js"
  }
}
```

## Team quality standards

### Coding standards document
```markdown
# Coding Standards

## Code Quality Requirements
- Minimum 80% test coverage
- No ESLint errors in CI
- Maximum cyclomatic complexity: 10
- All security vulnerabilities addressed

## Review Process
1. Automated checks must pass
2. At least 2 reviewer approvals
3. Security review for sensitive changes
4. Performance impact assessment

## Quality Tools
- ESLint for code standards
- Jest for testing
- SonarLint for code quality
- Snyk for security scanning
```

### Quality metrics tracking
```javascript
// scripts/quality-metrics.js
const fs = require('fs');
const { execSync } = require('child_process');

function collectMetrics() {
  const metrics = {
    timestamp: new Date().toISOString(),
    coverage: getCoverageMetrics(),
    complexity: getComplexityMetrics(),
    linting: getLintingMetrics(),
    security: getSecurityMetrics()
  };
  
  fs.writeFileSync('reports/quality-metrics.json', JSON.stringify(metrics, null, 2));
  return metrics;
}

function getCoverageMetrics() {
  const coverage = JSON.parse(fs.readFileSync('coverage/coverage-summary.json'));
  return {
    lines: coverage.total.lines.pct,
    statements: coverage.total.statements.pct,
    functions: coverage.total.functions.pct,
    branches: coverage.total.branches.pct
  };
}
```

## Troubleshooting quality tools

### Common configuration issues
```javascript
// Fix ESLint parser issues
{
  "parserOptions": {
    "ecmaVersion": 2022,
    "sourceType": "module",
    "project": "./tsconfig.json"
  }
}

// Fix Prettier conflicts
{
  "extends": ["prettier"],
  "plugins": ["prettier"],
  "rules": {
    "prettier/prettier": "error"
  }
}
```

### Performance optimization for large codebases
```json
{
  "eslint.workingDirectories": ["src", "tests"],
  "eslint.lintTask.options": "--cache --cache-location .eslintcache",
  "typescript.preferences.includePackageJsonAutoImports": "off"
}
```

Quality tools transform good code into great code—implement these practices to build robust, maintainable software!