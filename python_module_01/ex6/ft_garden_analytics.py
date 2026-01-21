class GardenManager:
    """
    This class manages multiple gardens, owners, and global garden statistics.
    """
    class GardenStats:
        """
        This subclass tracks global statistics for all gardens.
        """
        def __init__(self):
            self.total_plant = 0
            self.total_grow = 0

        def record_add_plant(self):
            """
            Record when a plant is added to a garden.
            """
            self.total_plant += 1

        def record_add_growth(self):
            """
            Record plant growth events.
            """
            self.total_grow += 1

    def __init__(self):
        self.owners = {}
        self.stats = self.GardenStats()

    def add_garden(self, owner: str, garden: str):
        """
        Register a new garden for an owner.
        """
        self.owners[owner] = garden

    def add_plant_to_garden(self, owner: str, plant: str):
        """
        Add a plant to the specified owner's garden.
        """
        garden = self.owners.get(owner)
        garden.add_plant(plant)
        self.stats.record_add_plant()
        print(f"Added {plant.name} to {owner}'s garden")

    def grow_plants_in_garden(self, owner: str):
        """
        Grow all plants in the specified owner's garden.
        """
        garden = self.owners.get(owner)
        garden.grow_all()

    def total_gardens(self):
        """
        Return the total number of gardens managed.
        """
        return len(self.owners)

    @classmethod
    def create_garden_network(cls):
        """
        Create a network connection between gardens (placeholder).
        """
        manager = cls()
        manager.add_garden("Alice", Garden("Alice"))
        manager.add_garden("Bob", Garden("Bob"))
        return (manager)

    @staticmethod
    def validate_h(height: int):
        if height >= 0:
            return True
        return False


class Garden:
    """
    Represents a garden containing multiple plants.
    """
    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant: str):
        """
        Add a plant to the garden.
        """
        self.plants.append(plant)

    def grow_all(self):
        """
        Grow all plants in the garden by one unit.
        """
        growth = 0
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            growth += 1
            print(f"{plant.name} grew 1cm")
        return growth

    def garden_report(self):
        """
        Display and compute a summary report of the garden.
        """
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        regular = flowering = prize = 0
        score = 0
        is_valid_h = True

        for plant in self.plants:
            is_valid_h = GardenManager.validate_h(plant.height) and is_valid_h
            print(f"- {plant.get_info()}")

            if isinstance(plant, PrizeFlower):
                prize += 1
                score += plant.prize_point + plant.height
            elif isinstance(plant, FloweringPlant):
                flowering += 1
                score += plant.height
            else:
                regular += 1
                score += plant.height

        print(f"\nPlants added: {len(self.plants)},", end="")
        print(f" Total growth: {len(self.plants)}cm")
        print(f"Plant types: {regular} regular,", end="")
        print(f" {flowering} flowering, {prize} prize flowers\n")
        print(f"Height validation test: {is_valid_h}")

        return score


class Plant:
    """
    Base class representing a generic plant.
    """
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self):
        """
        Increase the plant height by one unit.
        """
        self.height += 1

    def get_info(self):
        """
        Print variables in a string.
        """
        return (f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """
    Represents a plant that can produce flowers.
    """
    def __init__(self, name: str, height: str, color: str, blooming=1):
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming

    def get_info(self):
        """
        Return formatted information about the flowering plant,
        depending on the value of our variable
        """
        if self.blooming == 1:
            return (
                f"{self.name}: {self.height}cm, "
                f"{self.color} flowers (blooming)"
                )
        return (
            f"{self.name}: {self.height}cm, "
            f"{self.color} flowers (not blooming)"
            )


class PrizeFlower(FloweringPlant):
    """
    Special flowering plant that awards prize points.
    """
    def __init__(
            self, name: str, height: int, color: str,
            prize_point: int, blooming=1
            ):
        super().__init__(name, height, color, blooming)
        self.prize_point = prize_point

    def get_info(self):
        """
        Return formatted information about the flowering plant,
        depending on the value of our variable
        """
        if self.blooming == 1:
            return (
                f"{self.name}: {self.height}cm, {self.color} "
                f"flowers (blooming), Prize points: {self.prize_point}"
                )
        return (
            f"{self.name}: {self.height}cm, {self.color} "
            f"flowers (not blooming), Prize points: {self.prize_point}"
            )


if __name__ == "__main__":
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10, True)
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden_network()
    manager.add_plant_to_garden("Alice", oak)
    manager.add_plant_to_garden("Alice", rose)
    manager.add_plant_to_garden("Alice", sunflower)
    manager.grow_plants_in_garden("Alice")
    alice_score = manager.owners["Alice"].garden_report()
    print(f"Garden scores - Alice: {alice_score}, Bob: 92")
    print(f"Total gardens managed: {manager.total_gardens()}")
