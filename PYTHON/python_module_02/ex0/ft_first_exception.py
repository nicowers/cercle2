def check_temperature(temp_str: str) -> str:
    """Validate and display whether a temperature is suitable for plants."""
    temp = 0
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> str:
    """Prompt the user for multiple temperature inputs and test each one."""
    for i in range(4):
        temp_str = input("Testing temperature: ")
        check_temperature(temp_str)
        print()


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
    print("All tests completed - program didn't crash!")
