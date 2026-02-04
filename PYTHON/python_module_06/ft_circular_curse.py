if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===\n")
    from alchemy.grimoire.validator import validate_ingredients
    print("Testing ingredient validation:")
    print("validate_ingredients(\"fire air\"):", validate_ingredients("fire air"))
    print("validate_ingredients(\"dragon scales\"):", validate_ingredients("dragon scales"))
    from alchemy.grimoire.spellbook import late_record_spell
    print("\nTesting spell recording with validation:")
    print("record_spell(\"Fireball\", \"fire air\"):", late_record_spell("Fireball", "fire air"))
    print("record_spell(\"Dark Magic\", \"shadow\"):", late_record_spell("Dark Magic", "shadow"))
    from alchemy.grimoire.spellbook import record_spell
    print("\nTesting late import technique:")
    print("record_spell(\"Lightning\", \"air\"):", record_spell("Lightning", "air"))
    print("\nCircular dependency curse avoided using late imports!")
    print(" All spells processed safely!")