def garden_operations() -> str:
    """Demonstrate and handle different built-in Python error types."""
    res = 0
    try :
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        res = 16 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    try:
        print("\nTesting FileNotFoundError...")
        open('missing.txt', 'r')
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file or directory: 'missing.txt'")
    try:
        print("\nTesting KeyError...")
        data = {}
        _ = data["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    try :
        print("\nTesting multiple errors together...")
        int("abc")
        res = 16 / 0
        open('missing.txt', 'r')
        data = {}
        _ = data["bonjour"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


def test_error_types() -> str:
    """Run all garden error demonstrations and confirm program stability."""
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
