
if __name__ == "__main__":
    from CreatureCard import CreatureCard
    creature1 = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing insufficient mana (3 available):")
    print("Playable:", creature1.is_playable(2))