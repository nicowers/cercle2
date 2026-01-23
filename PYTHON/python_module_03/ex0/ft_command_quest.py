#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print("No arguments provided!")
        print("Program name:", sys.argv[0])
        print("Total arguments: 1")
        sys.exit(1)
    print("Program name:", sys.argv[0])
    print("Arguments received:", len(sys.argv) - 1)
    for i in range(1, len(sys.argv)):
        print(f"Argument {i}:", sys.argv[i])
    print("Total arguments:", len(sys.argv))