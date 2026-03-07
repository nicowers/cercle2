from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


if __name__ == "__main__":
    spell1 = SpellCard("Lightning Bolt", 3, "rare", "damage")
    artifact1 = ArtifactCard("medallion", 3, "legendary", 3, "mana")
    # spell2 = Spell("blade", 2, "rare", "attack")
    creature1 = CreatureCard("Fire Dragon", 5, "Super rare", 5, 7)
    deck = Deck()

    deck.add_card(spell1)
    deck.add_card(artifact1)
    deck.add_card(creature1)
    stats = deck.get_deck_stats()

    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    print("Deck stats:", stats)

    print("\nDrawing and playing cards:\n")
    game_stats = {"mana": 6, "targets": [{"name": "Goblin",
                                          "hp": 10, "attack": 2}]}
    for elt in stats:
        card_drawn = deck.draw_card()
        if card_drawn:
            print("Drew:", card_drawn.name, end="")
            if isinstance(card_drawn, SpellCard):
                print(" (Spell)")
            elif isinstance(card_drawn, CreatureCard):
                print(" (Creature)")
            elif isinstance(card_drawn, ArtifactCard):
                print(" (Artifact)")
            result = card_drawn.play(game_stats)
            print("Play result:", result)
            print()
    print("Polymorphism in action: Same interface, different card behaviors!")
