def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:

    def power_accumulator(amount):
        nonlocal initial_power
        initial_power += amount
        return initial_power
    return power_accumulator


def enchantment_factory(enchantment_type: str) -> callable:

    def enchanted_weapon(weapon: str) -> str:
        result = enchantment_type.capitalize() + " " + weapon.capitalize()
        return result
    return enchanted_weapon


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        for keys in memory:
            if key == keys:
                return memory[key]
        return "Memory not found"
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    counter1 = mage_counter()

    print("\nTesting mage_counter...")
    print("Call 1:", counter1())
    print("Call 2:", counter1())
    print("Call 3:", counter1())

    initial_power = 460
    power_count = spell_accumulator(initial_power)

    print(f"\nTesting spell accumulator with intial power of {initial_power}")
    print("Call 1 (adding 5):", power_count(5))
    print("Call 2 (adding 5):", power_count(5))

    result1 = enchantment_factory("frozen")
    result2 = enchantment_factory("Flaming")

    print("\nTesting enchantment factory...")
    print(result1("shield"))
    print(result2("sword"))

    vault = memory_vault()

    vault["store"]("name", "gandalf")
    print("\nTesting memory vault")
    print(vault["recall"]("name"))
