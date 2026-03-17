import sys
import os
import site


def in_virtual_env() -> bool:
    """
    Check if the program is running inside a virtual environment.
    """
    # sys.prefix: path of the currently active Python environment
    # sys.base_prefix: path of the base (global) Python installation
    return sys.prefix != sys.base_prefix


def get_venv_name() -> str | None:
    """
    os.environ allows access to system environment variables.
    'VIRTUAL_ENV' is automatically created when a virtual
    environment is activated.
    """
    # os.path.basename extracts only the final part of the path matrix_env

    env_path = os.environ.get("VIRTUAL_ENV")

    if env_path:
        return os.path.basename(env_path)
    return None


if __name__ == "__main__":

    # sys.executable returns the full path
    # of the Python interpreter currently running
    current_python = sys.executable

    # path to the virtual environment
    env_path = os.environ.get("VIRTUAL_ENV")

    # Name of the virtual environment
    venv_name = get_venv_name()

    if in_virtual_env():

        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {current_python}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {env_path}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")

        print("Package installation path:")

        # site.getsitepackages() returns a list of directories where
        # Python installs third-party packages (site-packages).
        print(site.getsitepackages()[0])

    else:

        print("MATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {current_python}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate    # On Windows\n")

        print("Then run this program again.")
