class SecurePlant:
    """
    Receive the name, the encapsulation size, and encapsulation age of plants .
    It also including some methods that act on plants.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        The constructor takes parameters that allow objects to be instantiated
        """
        self.name = name
        self.__height = height
        self.__age = age

    @property
    def height(self) -> str:
        """
        Reading without modification.
        """
        return (self.__height)

    @height.setter
    def height(self, height: int) -> str:
        """
        Modify the values of our variable.
        """
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm", end="")
            print(" [REJECTED]\nSecurity: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    @property
    def age(self) -> int:
        """
        Reading without modification.
        """
        return (self.__age)

    @age.setter
    def age(self, age: int) -> str:
        """
        Modify the values of our variables.
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
    plant1.height = 25
    plant1.age = 30
    print()
    plant2.height = -5
    print(f"\nCurrent plant: {plant1.name} ({plant1.height}cm,", end="")
    print(f" {plant1.age} days)")
