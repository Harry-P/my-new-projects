# Episode 17 — Extensions Development Basics

## Why create VS Code extensions?
VS Code extensions let you customize and extend the editor to fit your exact workflow. You can:
- Add new languages or frameworks support
- Create custom commands and shortcuts
- Build specialized tools for your team
- Automate repetitive tasks
- Integrate with external services

## Setting up extension development
First, install the required tools:

```bash
npm install -g yo generator-code
```

This gives you Yeoman (yo) and the VS Code extension generator.

## Creating your first extension

### 1. Generate the boilerplate
```bash
yo code
```

Choose "New Extension (TypeScript)" and fill in:
- Extension name: `my-first-extension`
- Identifier: Leave default
- Description: "My first VS Code extension"
- Initialize git repo: Yes
- Bundle source code: No (for now)

### 2. Understanding the structure
Your extension folder contains:
- `package.json` - Extension manifest (metadata, commands, contributions)
- `src/extension.ts` - Main extension code
- `src/test/` - Test files
- `.vscode/` - VS Code configuration for developing the extension

### 3. The package.json manifest
Key sections:
```json
{
  "activationEvents": ["onCommand:my-first-extension.helloWorld"],
  "main": "./out/extension.js",
  "contributes": {
    "commands": [{
      "command": "my-first-extension.helloWorld",
      "title": "Hello World"
    }]
  }
}
```

## Extension lifecycle

### Activation
Extensions activate when their `activationEvents` are triggered:
- `onCommand:commandId` - when a command runs
- `onLanguage:languageId` - when a file type opens
- `*` - on VS Code startup (use sparingly!)

### The activate function
```typescript
export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('my-first-extension.helloWorld', () => {
        vscode.window.showInformationMessage('Hello World from my extension!');
    });
    
    context.subscriptions.push(disposable);
}
```

## Common extension patterns

### 1. Commands
Register commands that users can run:
```typescript
const disposable = vscode.commands.registerCommand('extension.doSomething', () => {
    vscode.window.showInformationMessage('Command executed!');
});
```

### 2. Status bar items
Show information in the status bar:
```typescript
const statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
statusBarItem.text = "$(sync~spin) Processing...";
statusBarItem.show();
```

### 3. Tree views
Create custom explorer panels:
```typescript
const treeDataProvider = new MyTreeDataProvider();
vscode.window.registerTreeDataProvider('myView', treeDataProvider);
```

## Testing your extension

### 1. Run in Extension Development Host
- Press `F5` to launch a new VS Code window with your extension loaded
- Test your commands and features
- Check the Debug Console for logs

### 2. Writing unit tests
Use the included test framework:
```typescript
import * as assert from 'assert';
import * as vscode from 'vscode';

suite('Extension Test Suite', () => {
    test('Sample test', () => {
        assert.strictEqual(-1, [1, 2, 3].indexOf(5));
    });
});
```

## Publishing your extension

### 1. Install vsce (Visual Studio Code Extension manager)
```bash
npm install -g vsce
```

### 2. Package your extension
```bash
vsce package
```
Creates a `.vsix` file you can install manually or share.

### 3. Publish to marketplace
```bash
vsce publish
```
Requires a Visual Studio Marketplace publisher account.

## Best practices
- Follow the [Extension Guidelines](https://code.visualstudio.com/api/references/extension-guidelines)
- Use descriptive command and setting names
- Provide clear documentation
- Handle errors gracefully
- Respect user preferences and themes
- Keep activation time minimal

## Example: Simple text transformer
Let's build an extension that transforms selected text:

```typescript
export function activate(context: vscode.ExtensionContext) {
    let uppercase = vscode.commands.registerCommand('extension.toUpperCase', () => {
        const editor = vscode.window.activeTextEditor;
        if (editor) {
            const selection = editor.selection;
            const text = editor.document.getText(selection);
            editor.edit(editBuilder => {
                editBuilder.replace(selection, text.toUpperCase());
            });
        }
    });
    
    context.subscriptions.push(uppercase);
}
```

Add to package.json:
```json
"contributes": {
    "commands": [{
        "command": "extension.toUpperCase",
        "title": "Transform to Uppercase"
    }]
}
```

## Next steps
- Explore the [VS Code API](https://code.visualstudio.com/api) documentation
- Look at popular extensions' source code on GitHub
- Join the VS Code extension development community
- Build something that solves a real problem in your workflow

## Exercise
Create an extension that:
1. Adds a command to count words in the current file
2. Shows the count in a status bar item
3. Updates the count when the file content changes

This covers the basics of extension development—you're ready to build useful tools for yourself and others!