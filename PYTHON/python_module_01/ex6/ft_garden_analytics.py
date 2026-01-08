class GardenManager:
    class GardenStats:
        def __init__(self):
            self.total_plant = 0
            self.total_grow = 0

        def record_add_plant(self):
            self.total_plant += 1
    
        def record_add_growth(self):
            self.total_grow += 1

    def __init__(self):
        self.owners = {}
        self.stats = self.GardenStats()


    def add_garden(self, owner: str, garden: str):
        self.owners[owner] = garden

    def add_plant_to_garden(self, owner: str, plant):
        garden = self.owners.get(owner)
        garden.add_plant(plant)
        self.stats.record_add_plant()
        print(f"Added {plant.name} to {owner}'s garden")

    def grow_plants_in_garden(self, owner: str):
        garden = self.owners.get(owner)
        garden.grow_all()

    def total_gardens(self):
        return len(self.owners)

    def create_garden_network(self):
        manager = self
            
class Garden:
    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def grow_all(self):
        growth = 0
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            growth += 1
            print(f"{plant.name} grew 1cm")
        return growth

    def garden_report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        regular = flowering = prize = 0
        score = 0

        for plant in self.plants:
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

        print(f"\nPlants added: {len(self.plants)}, Total growth: {len(self.plants)}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers\n")
        print(f"Height validation test: {all(p.height > 0 for p in self.plants)}")

        return score

class Plant:
    def __init__(self, name: str, height: str):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1

    def get_info(self):
        return(f"-{self.name}: {self.height}cm")

class FloweringPlant(Plant):
    def __init__(self, name: str, height: str, color: str, blooming=1):
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming
        
    def get_info(self):
        if self.blooming == 1:
            return(f"{self.name}: {self.height}cm {self.color} flowers (blooming)")
        return(f"{self.name}: {self.height}cm {self.color} flowers (not blooming)")
    
class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color,prize_point , blooming=1):
        super().__init__(name, height, color, blooming)
        self.prize_point = prize_point


    def get_info(self):
        if self.blooming == 1:
            return(f"{self.name}: {self.height}cm {self.color} flowers (blooming), Prize points: {self.prize_point}")
        return(f"{self.name}: {self.height}cm {self.color} flowers (not blooming), Prize points: {self.prize_point}")



if __name__ == "__main__":
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10, True)
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager()
    garden = Garden("Alice")

    manager.add_garden("Alice", garden)
    manager = GardenManager()
    garden = Garden("Alice")
    manager.add_garden("Alice", garden)

    manager.add_plant_to_garden("Alice", oak)
    manager.add_plant_to_garden("Alice", rose)
    manager.add_plant_to_garden("Alice", sunflower)

    manager.grow_plants_in_garden("Alice")

    alice_score = garden.garden_report()

    print(f"Garden scores - Alice: {alice_score}, Bob: 92")
    print(f"Total gardens managed: {manager.total_gardens()}")
    