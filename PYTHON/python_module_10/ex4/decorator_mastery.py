from functools import wraps
from time import perf_counter as pc
import functools

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
def get_power(power):
    return power

def retry_spell(max_attempts: int) -> callable:
    return 


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return

    def cast_spell(self, spell_name: str, power: int) -> str:
        return 


if __name__ == "__main__":
    print("\nTesting spell timer...")
    result = spell_cast("Fireball")
    print(result)

    print("\nTesting power validator")
    print(get_power(power=51))

    print('\nTesting retry spell')