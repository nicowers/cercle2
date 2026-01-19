class SecurePlant:
    """
    Receive the name, the encapsulation size, and encapsulation age of plants .
    It also including some methods that act on plants.
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age

    @property
    def get_height(self):
        """
        Reading without modification.
        """
        return (self.__height)

    @get_height.setter
    def set_height(self, height: int):
        """
        Modify the values ​​of our variable.
        """
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm", end="")
            print(" [REJECTED]\nSecurity: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    @property
    def get_age(self):
        """
        Reading without modification.
        """
        return (self.__age)

    @get_age.setter
    def set_age(self, age: int):
        """
        Modify the values ​​of our variable.
        """
        if (age < 0):
            print(f"Invalid operation attempted: {age} days", end="")
            print("[REJECTED]\nSecurity: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", 5, 30)
    plant2 = SecurePlant("Oak", 200, 365)
    print(f"Plant created: {plant1.name}")
    plant1.set_height = 25
    plant1.set_age = 30
    print()
    plant2.set_height = -5
    print(f"\nCurrent plant: {plant1.name} ({plant1.get_height}cm,", end="")
    print(f" {plant1.get_age} days")
