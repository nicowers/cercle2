class Plant:
    """
    Receive the name, the encapsulation size, and encapsulation age of plants .
    It also including some methods that act on plants.
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Inherited the parent parameters; it also contains its own method.
    """
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """
        Print variables in a string.
        """
        return (f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    Inherited the parent parameters; it also contains its own method.
    """
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Print variables in a string.
        """
        return (f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    """
    Inherited the parent parameters; it also contains its own method.
    """
    def __init__(self, name: str, height: int, age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def nutritional_value(self):
        """
        Print variables in a string.
        """
        return (f"{self.name} is rich in Vitamin C")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    coquelicot = Flower("Coquelicot", 20, 40, "red")
    oak = Tree("Oak", 500, 1825, 50)
    mapple = Tree("mapple", 300, 505, 25)
    tomato = Vegetable("Tomato", 80, 90, "summer")
    cucumber = Vegetable("cucumber", 60, 70, "automn")
    print(f"Rose (Flower): {rose.height}cm, {rose.age} days,", end="")
    print(f" {rose.color} color")
    print(rose.bloom())
    print(f"\nOak (Tree): {oak.height}cm, {oak.age} days,", end="")
    print(f" {oak.trunk_diameter}cm diameter")
    print(oak.produce_shade())
    print(f"\nTomato (Vegetable): {tomato.height}cm,", end="")
    print(f" {tomato.age} days, {tomato.harvest_season} harvest")
    print(tomato.nutritional_value())
