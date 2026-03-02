from typing import Any, List, Dict, Union, Optional
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card

class EliteCard(Card, Combatable, Magical):
    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        pass


    def defend(self, incoming_damage: int) -> dict:
        pass


    def get_combat_stats(self) -> dict:
        pass


    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass


    def channel_mana(self, amount: int) -> dict:
        pass


    def get_magic_stats(self) -> dict:
        pass