from abc import ABC
from ex0 import Card

class Spellcard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        
    def play(self, game_state: dict) -> dict:



    # def resolve_effect(self, targets: list) -> dict:
