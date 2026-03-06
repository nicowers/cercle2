from ex4.TournamentCard import TournamentCard

# class TournamentPlatform:
#     def __init__(self):
#         self.cards = {}

    # def register_card(self, card: TournamentCard) -> str:
    #     id = self.id
    #     name = self.name
    #     result = ""
    #     result += f"{name} (ID:, {id})\n"
    #     result += "- Interfaces: [Card, Combatable, Rankable]\n"
    #     result += f"- Rating: self.rating\n"
    #     result += f"- Record: {self.wins}-{self.loses}\n"
    #     return result

    # def register_card(self, card: TournamentCard) -> str:
    #     self.cards["card_id"] = card.id
    #     return card.id

class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.match_played = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = card.name.split(" ")[1].lower() + "_001"
        self.cards[card_id] = card
        print(f"{card.name} (ID: {card_id})")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: self.rating")
        print(f"- Record: {card.wins}-{card.losses}\n")
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards["card_id"]
        card2 = self.cards["card_id"]

        damage1 = card1.damage(card2)
        damage2 = card2.damage(card1)
        self.match_played += 1
        return {
            "card1": card1.name,
            "card2": card2.name,
            "damage1": damage1,
            "damage2": damage2
        }

    def get_leaderboard(self) -> list:
        cards_list = list(self.cards.values())
        leaderboard = []

        while len(cards_list) > 0:
            best_card = cards_list[0]

            for card in cards_list:
                if card.rating > best_card.rating:
                    best_card = card

            leaderboard.append(best_card.name)
            cards_list.remove(best_card)

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        matches_played = self.match_played
        avg_rating = 0
        if total_cards > 0:
            for card in self.cards.values():
                avg_rating += card.rating
            avg_rating /= len(self.cards)
        return {
                "total_cards": total_cards,
                "matches_played": matches_played,
                "avg_rating": avg_rating,
                "platform_status": "active"
                }