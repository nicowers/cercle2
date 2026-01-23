def check_plant_health(plant_name, water_level, sunlight_hours):
    """Validate plant health based on name, water level, and sunlight hours."""
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10 :
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2 :
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")
    print(f"Plant '{plant_name}' is healthy!")

def test_plant_checks():
    """Test plant health validation with valid and invalid inputs."""
    print("=== Garden Plant Health Checker ===\n")
    try:
        print("Testing good values...")
        check_plant_health("tomato", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("\nTesting empty plant name...")
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("\nTesting bad water level...")
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("\nTesting bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("\nAll error raising tests completed!")

if __name__=="__main__":
    test_plant_checks()







