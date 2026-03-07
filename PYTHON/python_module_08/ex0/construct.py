import sys
import os
import site

if __name__ == "__main__":
    current_python = sys.executable
    path_to_matrix = sys.prefix
    in_venv = sys.prefix != sys.base_prefix
    if in_venv:
        print("MATRIX STATUS: Welcome to the construct\n")
        print("Current Python:", current_python)
        print("Virtual Environment: matrix_env")
        print("Environment Path:", path_to_matrix)
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.\n")
        print("Package installation path:")
        print("/path/to/matrix_env/lib/python3.11/site-packages")
    else:
        print("MATRIX STATUS: You're still plugged in")
        print("Current Python:")
        print("\nVirtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        source matrix_env/bin/activate # On Unix
        matrix_env
        Scripts
        activate # On Windows
        Then run this program again.)
