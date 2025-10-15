# Episode 14: Remote Development

## Overview
Remote development allows you to use VS Code's full feature set while your code, runtime, and tools are hosted elsewhere. This episode covers SSH remote development, container development, WSL integration, and cloud development environments.

## Introduction to Remote Development

### What is Remote Development?
Remote development enables you to:
- **Code on remote servers** while using local VS Code
- **Develop inside containers** for consistent environments
- **Use WSL** for Linux development on Windows
- **Access cloud workspaces** from anywhere
- **Collaborate** on shared development environments

### Benefits of Remote Development
- **Consistent environments** across team members
- **Powerful remote machines** for heavy workloads
- **Isolation** of development environments
- **Access to Linux tools** on Windows
- **No local setup** required for complex projects

### Remote Development Extensions

#### Essential Extensions
- **Remote - SSH** - Connect to remote servers
- **Remote - Containers** - Develop inside Docker containers
- **Remote - WSL** - Work with Windows Subsystem for Linux
- **Remote Development Extension Pack** - All three extensions

## SSH Remote Development

### Setting Up SSH Remote Development

#### Prerequisites
- **SSH server** running on remote machine
- **SSH client** on local machine
- **Network connectivity** between machines
- **SSH key pair** (recommended for security)

#### Installing Remote-SSH Extension
1. **Open Extensions view** (`Ctrl+Shift+X`)
2. **Search** "Remote - SSH"
3. **Install** by Microsoft
4. **Reload** VS Code if prompted

### SSH Configuration

#### SSH Config File
Location: `~/.ssh/config` (Linux/macOS) or `%USERPROFILE%\.ssh\config` (Windows)

```ssh
# Development server
Host devserver
    HostName 192.168.1.100
    User developer
    Port 22
    IdentityFile ~/.ssh/id_rsa

# Production server
Host prodserver
    HostName prod.example.com
    User deploy
    Port 2222
    IdentityFile ~/.ssh/prod_key

# AWS EC2 instance
Host aws-dev
    HostName ec2-xx-xx-xx-xx.compute-1.amazonaws.com
    User ec2-user
    IdentityFile ~/.ssh/aws-key.pem
```

#### SSH Key Authentication
```bash
# Generate SSH key pair
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# Copy public key to remote server
ssh-copy-id user@remote-server

# Or manually copy the key
cat ~/.ssh/id_rsa.pub | ssh user@remote-server "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Connecting to Remote Server

#### Method 1: Command Palette
1. **Open Command Palette** (`Ctrl+Shift+P`)
2. **Type** "Remote-SSH: Connect to Host"
3. **Select** configured host or enter new address
4. **Choose platform** (Linux/Windows/macOS)

#### Method 2: Remote Explorer
1. **Click Remote Explorer** in Activity Bar
2. **View SSH targets**
3. **Click connect icon** next to host

#### Method 3: Status Bar
1. **Click remote indicator** in status bar (bottom-left)
2. **Select** "Connect to Host"
3. **Choose** from available connections

### Remote Development Workflow

#### File Operations
```bash
# VS Code operates on remote files directly
# No need to sync or transfer files manually
# IntelliSense works with remote dependencies
# Extensions run on remote server
```

#### Terminal Integration
- **Integrated terminal** runs on remote server
- **Full access** to remote command line
- **Run commands** as if locally connected
- **Port forwarding** for web servers

#### Extensions on Remote
```json
{
  "remote.SSH.defaultExtensions": [
    "ms-python.python",
    "ms-vscode.vscode-typescript-next",
    "esbenp.prettier-vscode"
  ]
}
```

### Advanced SSH Features

#### Port Forwarding
```bash
# Forward remote port 3000 to local port 3000
# Automatically detected when server starts
# Manual forwarding through Command Palette
```

#### X11 Forwarding (Linux/macOS)
```ssh
# SSH config for X11 forwarding
Host remote-gui
    HostName server.example.com
    User developer
    ForwardX11 yes
    ForwardX11Trusted yes
```

#### SSH Tunneling
```bash
# Tunnel through jump host
ssh -J jumphost user@target-server

# SSH config with ProxyJump
Host target
    HostName target-server
    User developer
    ProxyJump jumphost
```

## Container Development

### Docker and Dev Containers

#### What are Dev Containers?
Dev containers provide:
- **Consistent development environments**
- **Isolated dependencies** and tools
- **Reproducible setups** across team
- **Version-controlled** environment configuration

#### Prerequisites
- **Docker Desktop** installed and running
- **Remote - Containers** extension
- **Basic Docker knowledge**

### Creating Dev Containers

#### Method 1: From Template
1. **Command Palette** > "Remote-Containers: Add Development Container Configuration Files"
2. **Choose** from available templates
3. **Customize** configuration as needed

#### Method 2: Manual Configuration
Create `.devcontainer/devcontainer.json`:

```json
{
  "name": "Node.js Development",
  "image": "node:16",
  "features": {
    "ghcr.io/devcontainers/features/git:1": {},
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-vscode.vscode-typescript-next",
        "esbenp.prettier-vscode",
        "dbaeumer.vscode-eslint"
      ],
      "settings": {
        "terminal.integrated.defaultProfile.linux": "bash"
      }
    }
  },
  "forwardPorts": [3000, 5000],
  "postCreateCommand": "npm install",
  "remoteUser": "node"
}
```

### Common Dev Container Configurations

#### Node.js Development Container
```json
{
  "name": "Node.js & TypeScript",
  "image": "mcr.microsoft.com/devcontainers/typescript-node:18",
  "features": {
    "ghcr.io/devcontainers/features/node:1": {
      "version": "18"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-vscode.vscode-typescript-next",
        "esbenp.prettier-vscode",
        "dbaeumer.vscode-eslint",
        "bradlc.vscode-tailwindcss"
      ]
    }
  },
  "forwardPorts": [3000, 5173],
  "postCreateCommand": "npm install",
  "mounts": [
    "source=${localWorkspaceFolder}/node_modules,target=/workspaces/project/node_modules,type=volume"
  ]
}
```

#### Python Development Container
```json
{
  "name": "Python Development",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.pylint",
        "ms-python.black-formatter",
        "ms-toolsai.jupyter"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python"
      }
    }
  },
  "postCreateCommand": "pip install -r requirements.txt",
  "remoteUser": "vscode"
}
```

#### Full-Stack Development Container
```dockerfile
# .devcontainer/Dockerfile
FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash - \
    && sudo apt-get install -y nodejs

# Install Python
RUN sudo apt-get update && sudo apt-get install -y python3 python3-pip

# Install additional tools
RUN sudo apt-get install -y git curl wget vim

# Create development user
RUN useradd -m -s /bin/bash developer
USER developer
```

```json
{
  "name": "Full-Stack Development",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-vscode.vscode-typescript-next",
        "ms-python.python",
        "ms-vscode.vscode-json",
        "esbenp.prettier-vscode"
      ]
    }
  },
  "forwardPorts": [3000, 5000, 8000],
  "postCreateCommand": "npm install && pip install -r requirements.txt"
}
```

### Container Development Workflow

#### Opening in Container
1. **Open project** with `.devcontainer` folder
2. **Command Palette** > "Remote-Containers: Reopen in Container"
3. **Or click notification** to reopen in container

#### Development Process
```bash
# Container is built and started
# VS Code connects to container
# Extensions install in container
# Terminal runs inside container
# Port forwarding configured automatically
```

## WSL (Windows Subsystem for Linux)

### Setting Up WSL Development

#### Prerequisites
- **Windows 10/11** with WSL2 enabled
- **Linux distribution** installed from Microsoft Store
- **Remote - WSL** extension

#### Installing WSL2
```powershell
# Enable WSL and Virtual Machine Platform
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Install WSL2
wsl --install

# Set WSL2 as default
wsl --set-default-version 2

# Install Ubuntu (or preferred distribution)
wsl --install -d Ubuntu
```

### WSL Development Workflow

#### Connecting to WSL
1. **Click remote indicator** in status bar
2. **Select** "New WSL Window"
3. **Choose** Linux distribution
4. **Or use** `code .` from WSL terminal

#### File System Access
```bash
# Access Windows files from WSL
cd /mnt/c/Users/username/projects

# Access WSL files from Windows
\\wsl$\Ubuntu\home\username\projects
```

#### Performance Considerations
- **Store code in WSL filesystem** for better performance
- **Avoid cross-filesystem operations** when possible
- **Use WSL2** for better file system performance

### WSL Configuration

#### .wslconfig File
Location: `%USERPROFILE%\.wslconfig`

```ini
[wsl2]
memory=8GB
processors=4
swap=2GB
localhostForwarding=true

[experimental]
autoMemoryReclaim=gradual
```

#### Distribution-Specific Settings
```bash
# Set default user
echo "defaultUser=developer" >> /etc/wsl.conf

# Configure systemd (WSL2)
echo "[boot]" >> /etc/wsl.conf
echo "systemd=true" >> /etc/wsl.conf
```

## Cloud Development Environments

### GitHub Codespaces

#### What are Codespaces?
- **Cloud-hosted** development environments
- **Pre-configured** with tools and dependencies
- **Accessible** from browser or VS Code
- **Scalable** compute resources

#### Creating a Codespace
1. **Navigate** to GitHub repository
2. **Click** "Code" button
3. **Select** "Codespaces" tab
4. **Click** "Create codespace on main"

#### Codespace Configuration
`.devcontainer/devcontainer.json`:
```json
{
  "name": "GitHub Codespace",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:2": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "GitHub.copilot",
        "ms-vscode.vscode-typescript-next"
      ]
    }
  },
  "portsAttributes": {
    "3000": {
      "label": "Application",
      "onAutoForward": "openPreview"
    }
  }
}
```

### Other Cloud Platforms

#### GitPod
```yaml
# .gitpod.yml
image: gitpod/workspace-full

tasks:
  - init: npm install
    command: npm start

ports:
  - port: 3000
    onOpen: open-preview

vscode:
  extensions:
    - esbenp.prettier-vscode
    - ms-vscode.vscode-typescript-next
```

#### Replit
- **Browser-based** development environment
- **Collaborative** coding features
- **Integrated** deployment options
- **Multiple language** support

## Practical Exercises

### Exercise 1: SSH Remote Development
1. Set up SSH server on remote machine or VM
2. Configure SSH keys for authentication
3. Connect VS Code to remote server
4. Develop a simple project remotely

### Exercise 2: Container Development
1. Create a dev container configuration
2. Build and connect to the container
3. Install extensions in container
4. Test port forwarding with web server

### Exercise 3: WSL Development
1. Set up WSL2 on Windows
2. Install Linux distribution
3. Connect VS Code to WSL
4. Create project in WSL filesystem

### Exercise 4: Cloud Development
1. Create GitHub Codespace for existing repository
2. Configure dev container for cloud environment
3. Test development workflow in browser
4. Compare performance with local development

## Best Practices

### Security Considerations
1. **Use SSH keys** instead of passwords
2. **Limit SSH access** with proper firewall rules
3. **Keep remote systems** updated
4. **Use VPN** for additional security
5. **Regular security** audits

### Performance Optimization
1. **Choose appropriate** container base images
2. **Minimize container** layer size
3. **Use volume mounts** for large dependencies
4. **Configure resource** limits appropriately
5. **Monitor network** latency

### Team Collaboration
1. **Standardize** dev container configurations
2. **Version control** environment definitions
3. **Document** setup procedures
4. **Share SSH** configuration templates
5. **Establish** remote development policies

## Troubleshooting

### Common SSH Issues

#### Connection Problems
```bash
# Test SSH connection
ssh -v user@hostname

# Check SSH service
sudo systemctl status ssh

# Verify SSH config
ssh -F ~/.ssh/config -v hostname
```

#### Permission Issues
```bash
# Fix SSH key permissions
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chmod 700 ~/.ssh

# Fix authorized_keys permissions
chmod 600 ~/.ssh/authorized_keys
```

### Container Issues

#### Build Failures
```bash
# Check Docker service
docker --version
docker ps

# View build logs
docker build --no-cache .

# Clean Docker system
docker system prune -a
```

#### Extension Problems
1. **Check extension** compatibility with remote
2. **Verify extension** installation in container
3. **Check container** resource limits
4. **Review extension** logs

### WSL Issues

#### Performance Problems
1. **Store files** in WSL filesystem
2. **Avoid frequent** cross-filesystem access
3. **Configure WSL** resource limits
4. **Use WSL2** instead of WSL1

#### File System Issues
```bash
# Reset WSL distribution
wsl --unregister Ubuntu
wsl --install -d Ubuntu

# Check WSL status
wsl --list --verbose

# Update WSL
wsl --update
```

## Advanced Remote Development

### Multi-Container Development
```yaml
# docker-compose.yml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db
    volumes:
      - .:/workspace
  
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: devdb
      POSTGRES_USER: developer
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
```

### Remote Debugging
```json
{
  "name": "Remote Debug",
  "type": "node",
  "request": "attach",
  "address": "localhost",
  "port": 9229,
  "localRoot": "${workspaceFolder}",
  "remoteRoot": "/workspace"
}
```

### Custom Dev Container Features
```json
{
  "name": "Custom Feature",
  "features": {
    "./local-features/my-tool": {
      "version": "latest"
    }
  }
}
```

## Next Steps

In Episode 15, we'll explore:
- Advanced VS Code features and hidden gems
- Productivity tips and workflow optimization
- Extension development basics
- VS Code customization for power users

---

**Previous Episode:** Code Snippets  
**Next Episode:** Advanced Tips and Tricks  
**Duration:** Approximately 35-40 minutes  
**Prerequisites:** Episodes 1-13 completed, basic knowledge of SSH, Docker, or WSL helpful