from typing import Any, List, Dict, Union, Optional
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card

class EliteCard(Card, Combatable, Magical):
    def __init__(
            self, name: str, cost: int, rarity: str,
            damage: int, defense: int, hp: int, mana: int):
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.defense = defense
        self.hp = hp
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        targets = game_state.get("targets", [])
        spell_name = game_state.get("spell_name", "Arcane Blast")
        
        mana_cost = 3
        if self.mana >= mana_cost:
            result = self.cast_spell(spell_name, targets)
        else:
            result = {"card_played": self.name, "effect": "Not enough mana to cast spell"}
        
        return result

    def attack(self, target) -> dict:
        defense = target.get("defense", 0)

        blocked = min(defense, self.damage)
        damage_taken = self.damage - blocked

        target["hp"] -= damage_taken
        if target["hp"] < 0:
            target["hp"] = 0

        is_dead = target["hp"] == 0

        return {
            "attacker": self.name,
            "target": target["name"],
            "damage": damage_taken,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.defense, incoming_damage)
        damage_taken = incoming_damage - blocked
        self.hp -= damage_taken
        if self.hp < 0:
            self.hp = 0

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": blocked,
            "still_alive": self.hp > 0
        }

    def get_combat_stats(self) -> dict:
        return {"damage": self.damage,
                "defense": self.defense,
                "hp_remaining": self.hp
                }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        target_names = []
        mana_cost = 3
        if self.mana < mana_cost:
            return {"error": "Not enough mana"}

        self.mana -= mana_cost
        for t in targets:
            if isinstance(t, dict):
                target_names.append(t["name"])

            else:
                target_names.append(str(t))
        return {
        "caster": self.name,
        "spell": spell_name,
        "targets": target_names,
        "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {"channeled": amount, "mana": self.mana}

    def get_magic_stats(self) -> dict:
        return {"mana": self.mana}
