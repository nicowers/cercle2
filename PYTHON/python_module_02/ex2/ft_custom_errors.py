class GardenError(Exception):
    """Base exception class for all garden-related errors."""
    pass

class PlantError(GardenError):
    """Exception raised for plant-related problems."""
    def __init__(self, message="The tomato plant is wilting!"):
        super().__init__(message)

class WaterError(GardenError):
    """Exception raised for watering-related problems."""
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)

def raise_error() -> None:
    """Demonstrate raising and catching custom garden exceptions."""
    try:
        print("Testing PlantError...")
        raise PlantError
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    try:
        print("Testing WaterError...")
        raise WaterError
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    try:
        print("Testing catching all garden errors...")
        raise PlantError
    except GardenError as e:
        print(f"Caught PlantError: {e}")
    try:
        raise WaterError
    except GardenError as e:
        print(f"Caught WaterError: {e}")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    raise_error()
    print("\nAll custom error types work correctly!")