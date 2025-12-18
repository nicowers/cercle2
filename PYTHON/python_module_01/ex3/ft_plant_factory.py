class Plant:

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return(f"Created: {self.name} ({self.height}cm, {self.age} days)")

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    i = 0
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
	]
    for plant in plants:
        print(plant.get_info())
        i += 1
    print(f"\nTotal plants created: {i}")