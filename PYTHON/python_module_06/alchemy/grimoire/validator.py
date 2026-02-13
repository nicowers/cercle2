def validate_ingredients(ingredients: str) -> str:
    ingredient = ["fire", "water", "earth", "air"]
    parts = ingredients.split(" ")
    for element in parts:
        if element not in ingredient:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
