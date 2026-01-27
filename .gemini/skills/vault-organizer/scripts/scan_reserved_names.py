import os
import sys

RESERVED_NAMES = {
    'CON', 'PRN', 'AUX', 'NUL',
    'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9',
    'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'
}

def scan_reserved(root_dir):
    found = False
    for root, dirs, files in os.walk(root_dir):
        for name in files + dirs:
            if name.upper().split('.')[0] in RESERVED_NAMES:
                path = os.path.join(root, name)
                print(f"CRITICAL WARNING: Reserved name found: {path}")
                found = True
    return found

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    if scan_reserved(root):
        sys.exit(1)
    else:
        print("No reserved names found.")
        sys.exit(0)
