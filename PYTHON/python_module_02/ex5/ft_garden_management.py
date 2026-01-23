class GardenError(Exception):
    """Base exception class for garden-related errors."""
    pass

class PlantError(GardenError):
    """Exception raised for plant-related errors."""
    def __init__(self, message="The tomato plant is wilting!"):
        super().__init__(message)

class WaterError(GardenError):
    """Exception raised for water-related errors."""
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)

def check_plant_health(plant_name, water_level, sunlight_hours):
    """Validate plant health based on name, water level, and sunlight exposure."""
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

def water_plants(plant_list):
    """Water a list of plants with error handling and cleanup."""
    str = ""
    print("Opening watering system")
    try:
        for plant in plant_list:
            str = "Watering " + plant + ""
            print(str)
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
    finally:
         print("Closing watering system (cleanup)")

class Plant:
    """Represents a plant with water and sunlight requirements."""
    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun

class GardenManager:
    """Manage plants, watering operations, and health checks."""
    def __init__(self):
        self.plants = []

    def add_plant(self, name, water, sun):
        """Add a new plant to the garden with validation."""
        if name == "":
            raise PlantError("Plant name cannot be empty!")
        plant = Plant(name, water, sun)
        self.plants.append(plant)
        print(f"Added {name} successfully")
    
    def water_plants(self):
        """Water all plants in the garden safely."""
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self):
        """Check and display the health status of all plants."""
        for plant in self.plants:
            try:
                check_plant_health(plant.name, plant.water, plant.sun)
                print(f"{plant.name}: healthy (water: {plant.water}, sun: {plant.sun})")
            except ValueError as e:
                print(f"Error checking {plant.name}: {e}")

def test_recovery():
    """Test recovery from a garden-related exception."""
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")

    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato", 5, 8)
        manager.add_plant("lettuce", 15, 6)
        manager.add_plant("", 3, 5)
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_health()

    print("\nTesting error recovery...")
    test_recovery()

    print("\nGarden management system test complete!")
