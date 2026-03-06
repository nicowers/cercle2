from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

if __name__ == "__main__":
    platform = TournamentPlatform()
    card1 = TournamentCard("Fire Dragon", 5, "rare", 10101001)
    card2 = TournamentCard("Ice Wizard", 2, "epic", 10)
    print("\n=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")

    card1_id = platform.register_card(card1)
    card2_id = platform.register_card(card2)
    match_result = platform.create_match(card1_id, card2_id)
    print("Creating tournament match...")
    print("Match result:", match_result)