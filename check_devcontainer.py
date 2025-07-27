#!/usr/bin/env python3
import os, sys

def is_devcontainer():
    # Common VS Code devcontainer env vars
    if os.environ.get('DEVCONTAINER') == 'true':
        return True
    if os.environ.get('VSCODE_DEVCONTAINER') == 'true':
        return True
    # Check for .devcontainer marker file
    if os.path.exists('/workspaces') or os.path.exists('/.devcontainer.json'):
        return True
    # Check for VS Code server env
    if 'VSCODE_IPC_HOOK_CLI' in os.environ:
        return True
    return False

if __name__ == '__main__':
    if is_devcontainer():
        print('PASS: Running inside devcontainer.')
        sys.exit(0)
    else:
        print('FAIL: Not running inside devcontainer. Please use the provided devcontainer for all development and testing.')
        sys.exit(1)
