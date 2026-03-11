from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == "__main__":
    try:
        platform = TournamentPlatform()
        card1 = TournamentCard("Fire Dragon", 5, "rare", 10101001)
        card2 = TournamentCard("Ice Wizard", 2, "epic", 10)
        print("\n=== DataDeck Tournament Platform ===\n")
        print("Registering Tournament Cards...\n")

        card1_id = platform.register_card(card1)
        card2_id = platform.register_card(card2)
        match_result = platform.create_match(card1_id, card2_id)

        game_state = {
            "player1": platform.cards[card1_id],
            "player2": platform.cards[card2_id]
        }

        result = platform.cards[card1_id].play(game_state)

        print("Creating tournament match...")
        print("Match result:", result)

        print("\nTournament Leaderboard:")

        leaderboard = platform.get_leaderboard()

        position = 1
        for name in leaderboard:
            for card in platform.cards.values():
                if card.name == name:
                    info = card.get_rank_info()
                    print(f"{position}. {info['name']} ", end="")
                    print(f"- Rating: {info['rating']}", end="")
                    print(f" ({info['wins']}-{info['losses']})")
                    position += 1

        generate_platform_report = platform.generate_tournament_report()

        print("\nPlatform Report:")
        print(generate_platform_report)

        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except ValueError as e:
        print(e)
