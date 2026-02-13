def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    if validate_ingredients(ingredients) == f"{ingredients} - VALID":
        value_return = f"Spell recorded: {spell_name} "
        value_return += f"({validate_ingredients(ingredients)})"
        return (value_return)
    value_return = f"Spell rejected: {spell_name} "
    value_return += f"({validate_ingredients(ingredients)})"
    return (value_return)
