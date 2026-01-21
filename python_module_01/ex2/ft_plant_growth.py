class Plant:
    """
    Receive the name, size, and age of plants.
    It also including some methods that act on plants.
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, height: int):
        """
        Add the desired size to the plant size.
        """
        self.height += height

    def set_age(self, age: int):
        """
        Add the desired age to the plant age.
        """
        self.age += age

    def get_info(self):
        """
        Print variables in a string.
        """
        return (f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Day 1 ===")
    plants = [
        Plant("Rose", 25, 30),
        # Plant("Sunflower", 80, 45),
        # Plant("Cactus", 15, 120),
    ]
    for plant in plants:
        print(plant.get_info())
    growing_time = 6
    print(f"=== Day {growing_time + 1} ===")
    for plant in plants:
        plant.grow(growing_time)
        plant.set_age(growing_time)
        print(plant.get_info())
    print(f"Growth this week: +{growing_time}cm")
