from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
import random


class GameEngine():
    def __init__(self):
        self.deck = []
        self.battlefield = []
        self.hand = []
        self.player_health = 20
        self.player_mana = 0
        self.factory = None
        self.strategy = None
        self.turn_count = 0

    def configure_engine(self,
                         factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        for _ in range(5):
            card = random.choice([
                factory.create_creature(None),
                factory.create_spell(None),
                factory.create_artifact(None)
            ])
            self.deck.append(card)

    def simulate_turn(self) -> dict:
        self.turn_count += 1

        # Piocher une carte
        if self.deck:
            card = self.deck.pop(0)
            self.hand.append(card)

        # Décider de l'action avec la stratégie
        action = self.strategy.execute_turn(self.hand, self.battlefield)

        # Jouer les cartes depuis la main
        for card_name in action.get("cards_played", []):
            card = next((c for c in self.hand if c.name == card_name), None)
            if (
                card is not None
                and self.player_mana >= getattr(card, "cost", 0)
            ):
                self.player_mana -= getattr(card, "cost", 0)
                self.hand.remove(card)
                self.battlefield.append(card)

        return {
            "turn": self.turn_count,
            "player_health": self.player_health,
            "player_mana": self.player_mana,
            "hand": [card.name for card in self.hand],
            "battlefield": [card.name for card in self.battlefield],
            "action": action
        }

    def get_engine_status(self) -> dict:
        total_damage = sum(getattr(card, "attack", 0)
                           for card in self.battlefield)
        return {
            'turns_simulated': self.turn_count,
            'strategy_used': "AggressiveStrategy",
            'total_damage': total_damage,
            'cards_created': len(self.hand) + len(self.battlefield)
        }
