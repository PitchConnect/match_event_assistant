#!/usr/bin/env python3
import os, sys

def check_file_contains(path, keywords):
    if not os.path.exists(path):
        print(f"FAIL: {path} does not exist.")
        return False
    with open(path) as f:
        content = f.read()
    for kw in keywords:
        if kw not in content:
            print(f"FAIL: {path} missing required content: {kw}")
            return False
    print(f"PASS: {path} contains required content.")
    return True

def main():
    ok = True
    ok &= check_file_contains('ONBOARDING.md', ['Devcontainer', 'check_devcontainer.py'])
    ok &= check_file_contains('CONTRIBUTING.md', ['Devcontainer', 'check_devcontainer.py'])
    ok &= os.path.exists('check_devcontainer.py')
    if not ok:
        print('FAIL: Onboarding/devcontainer compliance audit failed.')
        sys.exit(1)
    print('PASS: Onboarding/devcontainer compliance audit passed.')
    sys.exit(0)

if __name__ == '__main__':
    main()
