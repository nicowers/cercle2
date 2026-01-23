class Plant:
    """
    Receive the name, size, and age of plants.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        The constructor takes parameters that allow objects to be instantiated
        """
        self.name = name
        self.height = height
        self.age = age

    def description(self) -> str:
        """
        Print variables in a string.
        """
        return (f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    for plant in plants:
        print(plant.description())
