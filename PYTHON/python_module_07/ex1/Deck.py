from ex0.Card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only Card objects can be added to the deck")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        total_cost = 0
        spells = 0
        artifacts = 0
        creatures = 0

        for card in self.cards:
            total_cost += card.cost
            if card.__class__.__name__ == "SpellCard":
                spells += 1
            elif card.__class__.__name__ == "ArtifactCard":
                artifacts += 1
            elif card.__class__.__name__ == "CreatureCard":
                creatures += 1

        avg_cost = round(total_cost / total, 1) if total > 0 else 0

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }
