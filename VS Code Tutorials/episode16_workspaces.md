# Episode 16 — Workspaces in VS Code

## What is a workspace?
A workspace in VS Code is the context that groups files, folders, and settings for a project. There are two main kinds of workspaces:

- Single-folder workspace: you open a single folder in VS Code. Settings and extensions apply to that folder only.
- Multi-root workspace (.code-workspace): you can add multiple folders to one workspace and have a single `.code-workspace` file that stores settings, folders, and configuration.

## Why use multi-root workspaces?
- Work on related projects together (frontend + backend)
- Share workspace-specific settings and launch configurations
- Save and reopen a set of folders with one click

## Creating a workspace
1. Open VS Code.
2. Use File → Add Folder to Workspace... to add more folders.
3. File → Save Workspace As... to create a `.code-workspace` file.

## Anatomy of a .code-workspace file
```json
{
  "folders": [
    { "path": "frontend" },
    { "path": "backend" }
  ],
  "settings": {
    "editor.tabSize": 2,
    "files.exclude": {
      "**/.git": true
    }
  }
}
```

Place this file at the workspace root or anywhere you like and open it in VS Code to load the workspace.

## Workspace settings vs User settings
- User settings: global to your VS Code installation (File → Preferences → Settings)
- Workspace settings: stored in `.vscode/settings.json` inside a folder or in the `.code-workspace` file for multi-root workspaces

Workspace settings override User settings for that workspace.

## Recommended workspace settings for teams
- Use workspace-level formatting rules (editor.formatOnSave)
- Configure language-specific settings
- Lock down extensions recommended in `.vscode/extensions.json`

## Extensions and workspace recommendations
Create `.vscode/extensions.json` and add:

```json
{
  "recommendations": [
    "ms-python.python",
    "esbenp.prettier-vscode"
  ]
}
```

VS Code will prompt contributors to install these extensions when they open the workspace.

## Tasks and launch configurations
- Tasks (`.vscode/tasks.json`) let you run build/test commands from the Command Palette
- Launch (`.vscode/launch.json`) configures debuggers for the workspace

Example `tasks.json` snippet:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build",
      "type": "shell",
      "command": "npm run build",
      "group": "build"
    }
  ]
}
```

## Quick tips
- Use the workspace file to share settings across team members.
- Keep workspace-specific secrets out of `.code-workspace` (use environment variables or secrets managers).
- Use relative paths in workspace `folders` entries for portability.

## Example: Create a reusable workspace
1. Create folders `frontend/` and `backend/` in a repo root.
2. Add both to a workspace and save as `project.code-workspace`.
3. Commit `project.code-workspace` to the repo (optional).

## Exercises
- Convert an existing single-folder project to a multi-root workspace by adding another related folder.
- Add `extensions.json` and a `tasks.json` to automate a build process.

---

If you'd like, I can also:
- Add a sample `project.code-workspace` file to the repo
- Update `VS Code Tutorials/README.md` with a link to this episode
- Create a short video script or checklist for teaching this episode

Which extras would you like me to add?