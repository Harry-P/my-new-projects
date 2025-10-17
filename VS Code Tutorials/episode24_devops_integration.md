# Episode 24 — DevOps Integration & CI/CD Workflows

## VS Code as a DevOps command center
Modern development requires seamless integration with CI/CD pipelines, infrastructure as code, and deployment workflows. This episode transforms VS Code into your DevOps hub.

## Container development workflows

### Docker integration mastery
Advanced Docker configurations in VS Code:
```dockerfile
# Multi-stage production Dockerfile
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine AS runtime
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001
WORKDIR /app
COPY --from=builder --chown=nextjs:nodejs /app/node_modules ./node_modules
COPY --chown=nextjs:nodejs . .
USER nextjs
EXPOSE 3000
CMD ["npm", "start"]
```

### Dev Containers for consistent environments
`.devcontainer/devcontainer.json`:
```json
{
  "name": "Full Stack Development",
  "dockerComposeFile": "docker-compose.yml",
  "service": "app",
  "workspaceFolder": "/workspace",
  "features": {
    "ghcr.io/devcontainers/features/node:1": {"version": "18"},
    "ghcr.io/devcontainers/features/docker-in-docker:2": {},
    "ghcr.io/devcontainers/features/kubectl-helm-minikube:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-kubernetes-tools.vscode-kubernetes-tools",
        "ms-azuretools.vscode-docker",
        "hashicorp.terraform"
      ],
      "settings": {
        "terminal.integrated.defaultProfile.linux": "bash"
      }
    }
  },
  "postCreateCommand": "npm install",
  "remoteUser": "node"
}
```

### Kubernetes development
Deploy and manage Kubernetes resources:
```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  labels:
    app: my-app
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
        env:
        - name: NODE_ENV
          value: "production"
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "200m"
```

## Infrastructure as Code

### Terraform integration
Configure Terraform in VS Code:
```hcl
# infrastructure/main.tf
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "infrastructure/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_ecs_cluster" "main" {
  name = "${var.project_name}-cluster"
  
  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

resource "aws_ecs_service" "app" {
  name            = "${var.project_name}-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = var.app_count

  deployment_configuration {
    maximum_percent         = 200
    minimum_healthy_percent = 100
  }
}
```

### ARM Templates for Azure
```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "webAppName": {
      "type": "string",
      "metadata": {
        "description": "Web app name."
      }
    }
  },
  "resources": [
    {
      "type": "Microsoft.Web/serverfarms",
      "apiVersion": "2022-03-01",
      "name": "[parameters('webAppName')]",
      "location": "[resourceGroup().location]",
      "sku": {
        "name": "B1",
        "tier": "Basic"
      }
    }
  ]
}
```

## CI/CD Pipeline Configuration

### GitHub Actions workflows
`.github/workflows/deploy.yml`:
```yaml
name: Build and Deploy
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests
        run: npm test
      
      - name: Run linting
        run: npm run lint
      
      - name: Security audit
        run: npm audit --audit-level high

  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    outputs:
      image-digest: ${{ steps.build.outputs.digest }}
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Log in to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=sha,prefix={{branch}}-
      
      - name: Build and push
        id: build
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      
      - name: Deploy to ECS
        run: |
          aws ecs update-service \
            --cluster my-cluster \
            --service my-service \
            --force-new-deployment
```

### GitLab CI/CD
`.gitlab-ci.yml`:
```yaml
stages:
  - test
  - build
  - deploy

variables:
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  KUBERNETES_NAMESPACE: production

test:
  stage: test
  image: node:18
  before_script:
    - npm ci
  script:
    - npm run test:coverage
    - npm run lint
    - npm audit --audit-level moderate
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  before_script:
    - echo $CI_REGISTRY_PASSWORD | docker login -u $CI_REGISTRY_USER --password-stdin $CI_REGISTRY
  script:
    - docker build -t $DOCKER_IMAGE .
    - docker push $DOCKER_IMAGE
  only:
    - main

deploy:
  stage: deploy
  image: bitnami/kubectl:latest
  before_script:
    - kubectl config use-context $KUBE_CONTEXT
  script:
    - kubectl set image deployment/my-app app=$DOCKER_IMAGE -n $KUBERNETES_NAMESPACE
    - kubectl rollout status deployment/my-app -n $KUBERNETES_NAMESPACE
  environment:
    name: production
    url: https://myapp.example.com
  only:
    - main
```

## Monitoring and observability

### Application monitoring setup
Configure monitoring with VS Code tasks:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Deploy Monitoring Stack",
      "type": "shell",
      "command": "helm",
      "args": [
        "upgrade", "--install", "monitoring",
        "prometheus-community/kube-prometheus-stack",
        "--namespace", "monitoring",
        "--create-namespace",
        "--values", "monitoring/values.yaml"
      ],
      "group": "deploy"
    },
    {
      "label": "Port Forward Grafana",
      "type": "shell",
      "command": "kubectl",
      "args": [
        "port-forward",
        "svc/monitoring-grafana",
        "3000:80",
        "-n", "monitoring"
      ],
      "isBackground": true,
      "group": "monitoring"
    }
  ]
}
```

### Log aggregation
Configure structured logging:
```javascript
// utils/logger.js
const winston = require('winston');

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: {
    service: process.env.SERVICE_NAME || 'my-app',
    version: process.env.APP_VERSION || '1.0.0',
    environment: process.env.NODE_ENV || 'development'
  },
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({
      filename: 'logs/error.log',
      level: 'error'
    }),
    new winston.transports.File({
      filename: 'logs/combined.log'
    })
  ]
});

module.exports = logger;
```

## Security and compliance

### Secret management
Configure secret scanning and management:
```yaml
# .github/workflows/security.yml
name: Security Scan
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  secret-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'
      
      - name: Upload Trivy scan results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'

  dependency-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
      
      - name: Install Snyk CLI
        run: npm install -g snyk
      
      - name: Run Snyk security scan
        run: snyk test --severity-threshold=high
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

### Compliance automation
```python
# scripts/compliance_check.py
import json
import subprocess
import sys

def check_docker_compliance():
    """Check Docker image compliance with security standards"""
    result = subprocess.run([
        'docker', 'run', '--rm', '-v', '/var/run/docker.sock:/var/run/docker.sock',
        'aquasec/trivy', 'image', '--format', 'json', 'my-app:latest'
    ], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Docker scan failed: {result.stderr}")
        return False
    
    findings = json.loads(result.stdout)
    critical_vulns = sum(1 for vuln in findings.get('Vulnerabilities', []) 
                        if vuln.get('Severity') == 'CRITICAL')
    
    if critical_vulns > 0:
        print(f"Found {critical_vulns} critical vulnerabilities")
        return False
    
    return True

if __name__ == "__main__":
    if not check_docker_compliance():
        sys.exit(1)
    print("Compliance checks passed")
```

## Environment management

### Multi-environment configuration
```yaml
# environments/staging.yml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: staging
data:
  NODE_ENV: "staging"
  API_URL: "https://api-staging.example.com"
  LOG_LEVEL: "debug"
  REDIS_URL: "redis://redis-staging:6379"

---
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
  namespace: staging
type: Opaque
data:
  DATABASE_URL: <base64-encoded-staging-db-url>
  JWT_SECRET: <base64-encoded-jwt-secret>
```

### Environment promotion pipeline
```bash
#!/bin/bash
# scripts/promote-environment.sh

set -e

SOURCE_ENV=$1
TARGET_ENV=$2

if [[ -z "$SOURCE_ENV" || -z "$TARGET_ENV" ]]; then
    echo "Usage: $0 <source-env> <target-env>"
    exit 1
fi

echo "Promoting from $SOURCE_ENV to $TARGET_ENV"

# Get current image from source environment
CURRENT_IMAGE=$(kubectl get deployment my-app -n $SOURCE_ENV -o jsonpath='{.spec.template.spec.containers[0].image}')

echo "Current image in $SOURCE_ENV: $CURRENT_IMAGE"

# Run integration tests against source environment
npm run test:integration -- --env=$SOURCE_ENV

# Deploy to target environment
kubectl set image deployment/my-app app=$CURRENT_IMAGE -n $TARGET_ENV

# Wait for rollout
kubectl rollout status deployment/my-app -n $TARGET_ENV --timeout=600s

# Run smoke tests against target environment
npm run test:smoke -- --env=$TARGET_ENV

echo "Successfully promoted $CURRENT_IMAGE from $SOURCE_ENV to $TARGET_ENV"
```

## Performance optimization

### Build optimization
```javascript
// webpack.config.js
const path = require('path');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');

module.exports = {
  mode: 'production',
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].[contenthash].js',
    chunkFilename: '[name].[contenthash].chunk.js',
    clean: true
  },
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all'
        }
      }
    }
  },
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: process.env.ANALYZE ? 'server' : 'disabled'
    })
  ]
};
```

### Cache optimization
```dockerfile
# Optimized Dockerfile with layer caching
FROM node:18-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force

FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:18-alpine AS runner
WORKDIR /app
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

COPY --from=deps --chown=nextjs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nextjs:nodejs /app/dist ./dist
COPY --from=builder --chown=nextjs:nodejs /app/package.json ./package.json

USER nextjs
EXPOSE 3000
CMD ["npm", "start"]
```

## Team DevOps workflows

### GitOps with ArgoCD
```yaml
# argocd/application.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/my-app-config
    targetRevision: HEAD
    path: k8s/overlays/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
```

### Disaster recovery automation
```python
# scripts/backup_automation.py
import boto3
import json
from datetime import datetime, timedelta

def create_database_backup():
    """Create automated database backup"""
    rds = boto3.client('rds')
    
    snapshot_id = f"automated-backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    
    response = rds.create_db_snapshot(
        DBSnapshotIdentifier=snapshot_id,
        DBInstanceIdentifier='my-production-db'
    )
    
    return response['DBSnapshot']['DBSnapshotIdentifier']

def cleanup_old_backups(retention_days=7):
    """Remove backups older than retention period"""
    rds = boto3.client('rds')
    cutoff_date = datetime.now() - timedelta(days=retention_days)
    
    snapshots = rds.describe_db_snapshots(
        SnapshotType='manual',
        DBInstanceIdentifier='my-production-db'
    )
    
    for snapshot in snapshots['DBSnapshots']:
        if snapshot['SnapshotCreateTime'].replace(tzinfo=None) < cutoff_date:
            rds.delete_db_snapshot(
                DBSnapshotIdentifier=snapshot['DBSnapshotIdentifier']
            )
            print(f"Deleted snapshot: {snapshot['DBSnapshotIdentifier']}")

if __name__ == "__main__":
    backup_id = create_database_backup()
    print(f"Created backup: {backup_id}")
    cleanup_old_backups()
```

DevOps integration transforms VS Code from a code editor into a complete development and deployment platform—master these workflows to streamline your entire software delivery pipeline!