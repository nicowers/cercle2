if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===\n")
    from alchemy.grimoire.validator import validate_ingredients
    print("Testing ingredient validation:")
    print(
        "validate_ingredients(\"fire air\"):",
        validate_ingredients("fire air"))
    print(
        "validate_ingredients(\"dragon scales\"):",
        validate_ingredients("dragon scales"))
    print("\nTesting spell recording with validation:")
    from alchemy.grimoire.spellbook import record_spell
    print(
        "record_spell(\"Fireball\", \"fire air\"):",
        record_spell("Fireball", "fire air"))
    print(
        "record_spell(\"Dark Magic\", \"shadow\"):",
        record_spell("Dark Magic", "shadow"))

    print("\nTesting late import technique:")
    print("record_spell(\"Lightning\", \"air\"):",
          record_spell("Lightning", "air"))
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
