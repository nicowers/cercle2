class GardenError(Exception):
    """Base exception class for garden-related errors."""
    pass

class PlantError(GardenError):
    """Exception raised for plant-related errors."""
    def __init__(self, message="The tomato plant is wilting!") -> None:
        super().__init__(message)

class WaterError(GardenError):
    """Exception raised for water-related errors."""
    def __init__(self, message="Not enough water in the tank!") -> None:
        super().__init__(message)

class Plant:
    """Represents a plant with water and sunlight requirements."""
    def __init__(self, name: str, water, sun):
        self.name = name
        self.water = water
        self.sun = sun

class GardenManager:
    """Manage plants, watering operations, and health checks."""
    def __init__(self):
        self.plants = []

    def add_plant(self, plant : Plant) -> None:
        """Add a new plant to the garden with validation."""
        if plant.name == "":
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant)
        print(f"Added {plant.name} successfully")
    
    def water_plants(self) -> None:
        """Water all plants in the garden safely."""
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        except TypeError:
            print("Error: Cannot water None - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str, water_level: int, sunlight_hours: int) -> None:
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

def test_garden_management() -> None:
    """Test recovery from a garden-related exception."""
    print("=== Garden Management System ===\n")
    manager = GardenManager()
    print("Adding plants to garden...")
    try:
        manager.add_plant(Plant("tomato", 5, 8))
        manager.add_plant(Plant("lettuce", 15, 6))
        manager.add_plant(Plant("", 3, 5))
    except PlantError as e:
        print(f"Error adding plant: {e}")
    print("\nWatering plants...")
    manager.water_plants()
    print("\nChecking plant health...")
    for plant in manager.plants:
        try:
            manager.check_plant_health(plant.name, plant.water, plant.sun)
        except ValueError as e:
            print(f"Error checking {plant.name}: {e}")
    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    finally:
        print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()

