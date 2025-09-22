#!/usr/bin/env python3
"""
tools/manifest_validator.py

Local manifest validator for Nomimi assets.
Usage:
    python tools/manifest_validator.py Nomimi/assets/manifest.json

Exit codes:
  0 - manifest looks valid
  2 - manifest invalid or referenced files missing
"""
import json
import os
import sys

def validate(manifest_path):
    if not os.path.exists(manifest_path):
        print(f"Manifest not found: {manifest_path}", file=sys.stderr)
        return 2
    with open(manifest_path, 'r', encoding='utf-8') as f:
        m = json.load(f)
    ok = True
    for a in m.get("assets", []):
        p = a.get("path")
        if not p:
            print("Asset missing 'path' field:", a)
            ok = False
        elif not os.path.exists(p):
            print("Referenced asset file missing:", p)
            ok = False
    if ok:
        print("Manifest looks valid.")
        return 0
    return 2

def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/manifest_validator.py <manifest.json>", file=sys.stderr)
        sys.exit(2)
    sys.exit(validate(sys.argv[1]))

if __name__ == "__main__":
    main()
