from functools import wraps
from time import perf_counter as pc


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = pc()
        print("Casting", func.__name__)
        result = func(*args, **kwargs)
        end = pc()
        print(f"Spell completed in {round((end - start) * 1000, 5)} ms")
        return result
    return wrapper


@spell_timer
def spell_cast(spell: str):
    return (f"{spell} cast")


def power_validator(min_power: int) -> callable:
    def decorator(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if "power" in kwargs:
                if kwargs["power"] >= min_power:
                    return func(*args, **kwargs)
                else:
                    return "Insufficient power for this spell"
            else:
                return "No power, please make sure to have power=..."
        return wrapper
    return decorator


@power_validator(30)
def get_power(power: int):
    return power


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, max_attempts + 1):
                try:
                    res = func(*args, **kwargs)
                    return res
                except ValueError:
                    print(f"Spell failed, retrying attempt {i}", end="")
                    print(f" on {max_attempts}")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


attempts = {"n": 0}


@retry_spell(50)
def trying_spell():
    attempts["n"] += 1
    if attempts["n"] < 10:
        raise ValueError("Spell failed")
    return "Spell success"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for elt in name:
            if elt.isalpha() or elt == " ":
                continue
            else:
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("\nTesting spell timer...")
    result = spell_cast("Fireball")
    print(result)

    print("\nTesting power validator")
    print(get_power(power=50))

    print('\nTesting retry spell')
    print(trying_spell())

    mage = MageGuild()
    print("\nTesting cast spell")
    print(mage.validate_mage_name("Dumbledore"))
    print(mage.validate_mage_name("Chi1"))
    print(mage.cast_spell("fireball", power=20))
    print(mage.cast_spell("fireball", power=5))
