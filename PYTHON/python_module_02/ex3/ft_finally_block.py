def water_plants(plant_list: list) -> None:
    """
    Water each plant in the list and ensure cleanup even if an error occurs.
    """
    str = ""
    print("Opening watering system")
    try:
        for plant in plant_list:
            str = "Watering " + plant
            print(str)
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Test the watering system with valid and invalid plant lists."""
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    print("Watering completed successfully!\n")
    plant_list = ["tomato", None]
    print("Testing with error...")
    water_plants(plant_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
