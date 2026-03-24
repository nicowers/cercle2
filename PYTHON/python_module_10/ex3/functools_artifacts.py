import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation.capitalize() == "Add":
        return (functools.reduce(operator.add, spells))
    if operation.capitalize() == "Multiply":
        return (functools.reduce(operator.mul, spells))
    elif operation.capitalize() == "Max":
        return (functools.reduce(max, spells))
    elif operation.capitalize() == "Min":
        return (functools.reduce(min, spells))
    else:
        return 0


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire_enchant = functools.partial(base_enchantment, 50, "fire")
    ice_enchant = functools.partial(base_enchantment, 50, "ice")
    lightning_enchant = functools.partial(base_enchantment, 50, "lightning")
    return {"fire_enchant": fire_enchant,
            "ice_enchant": ice_enchant,
            "lightning_enchant": lightning_enchant}


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def spell(x):
        return ("Unknown type")

    @spell.register
    def _(x: int):
        return f"Damage spell {x}"

    @spell.register
    def _(x: str):
        return f"Enchantment {x}"

    @spell.register
    def _(x: list):
        return [spell(e) for e in x]
    return spell


if __name__ == "__main__":
    try:
        print("\nTesting spell reducer...")
        print("Sum:", spell_reducer([10, 9, 10, 11, 12, 13], "add"))
        print("Product:", spell_reducer([60, 10, 40, 5, 2], "multiply"))
        print("Max:", spell_reducer([1, 2, 3, 4, 32, 40, 12], "MAX"))
        print("Min:", spell_reducer([1, 2, 3, 4, 32, 40, 12], "MiN"))

        def base_enchantment(power: int, element: str, target: str) -> str:
            return (f"{element} spell with {power} power hits {target}")

        print("\nTesting partial enchanter...")
        enchants = partial_enchanter(base_enchantment)
        print(enchants["fire_enchant"]("dragon"))
        print(enchants["fire_enchant"]("wizard"))
        print(enchants["fire_enchant"]("goblin"))

        print("\nTesting memoized fibonacci...")
        print("Fib(10):", memoized_fibonacci(10))
        print("Fib(15):", memoized_fibonacci(15))

        print("\nTesting spell dispatcher...")
        dispatcher = spell_dispatcher()
        print(dispatcher(5))
        print(dispatcher("fire"))
        print(dispatcher([1, 2, "fire", 4]))
    except Exception as e:
        print(e)
