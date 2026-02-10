
if __name__ == "__main__":
    from ex0.CreatureCard import CreatureCard
    creature1 = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    creature2 = CreatureCard('Goblin Warrior', 5, 'Common', 1, 6)
    game_state = {}
    available_mana = 6
    insufficient_mana = 3
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    print(creature1.get_card_info())
    print(f"\nPlaying {creature1.name} with {available_mana} mana available:")
    print("Playable:", creature1.is_playable(available_mana))
    print(creature1.play(game_state))
    print(creature1.attack_target(creature2))
    print("\nTesting insufficient mana (3 available):")
    print("Playable:",creature1.is_playable(insufficient_mana))
    print("\nAbstract pattern successfully demonstrated!")