class SecurePlant:
    def __init__(self,name: str, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, height):
        if (height < 0):
            return (f"Invalid operation attempted: height {height}cm [REJECTED]\nSecurity: Negative height rejected")
        self.__height = height
        return (f"Height updated: {self.__height} cm [OK]")

    def get_height(self):
        return (self.__height)

    def set_age(self, age):
        if (age < 0):
            return (f"Invalid operation attempted: {age} days [REJECTED]\nSecurity: Negative age rejected")
        self.__age = age
        return (f"Age updated: {self.__age} days [OK]")

    def get_age(self):
        return (self.__age)

if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", -5, 30)
    plant2 = SecurePlant("Oak", 200, 365)
    # print(plant1.get_height())
    # print(plant1.get_age())
    print(f"Plant created: {plant1.name}")
    print(plant1.set_height(25))
    print(plant1.set_age(30))
    print()
    print(plant1.set_height(-5))
    print(f"\nCurrent plant: {plant1.name} ({plant1.get_height()}cm, {plant1.get_age()} days)")
