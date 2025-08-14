#!/usr/bin/env python3
import json
import sys

def deep_sort(obj):
    if isinstance(obj, dict):
        return {k: deep_sort(obj[k]) for k in sorted(obj)}
    if isinstance(obj, list):
        # Sort list elements by their JSON representation
        return sorted((deep_sort(x) for x in obj), key=lambda x: json.dumps(x, sort_keys=True))
    return obj

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        obj = json.load(f)
    norm = deep_sort(obj)
    print(json.dumps(norm, indent=2, sort_keys=True))
