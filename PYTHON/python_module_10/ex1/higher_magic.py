def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined_spell(*args, **kwargs):
        spell_a = spell1(*args, **kwargs)
        spell_b = spell2(*args, **kwargs)
        return spell_a, spell_b
    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def spell_amplifier(*args, **kwargs):
        result = base_spell(*args, **kwargs)
        amplified_spell = result * multiplier
        return amplified_spell
    return spell_amplifier


def conditional_caster(condition: callable, spell: callable) -> callable:
    def casted_spell(*args, **kwargs):
        if condition(*args, **kwargs):
            result = spell(*args, **kwargs)
            return result
        return "Spell fizzled"
    return casted_spell


def spell_sequence(spells: list[callable]) -> callable:
    def sequenced_spell(*args, **kwargs):
        results = []
        for spell in spells:
            result = spell(*args, **kwargs)
            results.append(result)
        return results
    return sequenced_spell


if __name__ == "__main__":
    def spell1(ennemi):
        return (f"Fireball hits {ennemi}")

    def spell2(ennemi):
        return (f"Heals {ennemi}")

    result1 = (spell_combiner(spell1, spell2))
    final_result1 = result1("Dragon")

    print("\nTesting spell combiner...")
    print(f"Combined spell result: {final_result1[0]}, {final_result1[1]}")

    actuel_power = 10
    result2 = power_amplifier(
       lambda damage: actuel_power, 3
        )

    print("\nTesting power amplifier...")
    print(f"Original: {actuel_power}, Amplified: {result2(10)}")

    def spell():
        return "Spell blinding"

    def condition():
        return ""

    result3 = (conditional_caster(condition=condition,
                                  spell=spell
                                  ))

    print("\nTesting conditional caster")
    print(result3())

    result4 = [
        lambda : "Hello",
        lambda : "World"
    ]
    final_result4 = spell_sequence(result4)
    print("\nTesting spell sequence")
    print(final_result4())
