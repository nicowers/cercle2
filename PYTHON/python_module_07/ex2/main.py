from ex2.EliteCard import EliteCard

if __name__ == "__main__":
    try:
        arcane_warrior = EliteCard("Arcane Warrior", 5,
                                   "legendary", 5, 3, 10, 4)

        enemy = {"name": "Enemy", "hp": 5}

        print("\n=== DataDeck Ability System ===\n")
        print("EliteCard capabilities:")
        print("- Card: ['play', 'get_card_info', 'is_playable']")
        print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
        print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

        print("\nPlaying Arcane Warrior (Elite Card):\n")
        print("Combat phase:")

        attack_result = arcane_warrior.attack(enemy)
        print("Attack result:", attack_result)

        defense_result = arcane_warrior.defend(5)
        print("Defense result:", defense_result)
        print("\nMagic phase:")

        spell_targets = [{"name": "Enemy1"}, {"name": "Enemy2"}]
        spell_result = arcane_warrior.cast_spell("Fireball", spell_targets)
        print("Spell cast:", spell_result)

        mana_result = arcane_warrior.channel_mana(3)
        print("Mana channel:", mana_result)
        print("\nMultiple interface implementation successful!")
    except Exception as e:
        print(e)
