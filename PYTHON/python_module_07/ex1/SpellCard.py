from abc import ABC
from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        
    def play(self, game_state: dict) -> dict:
        #si mana n'existe pas on le mets a 0
        if game_state.get("mana", 0) < self.cost:
            return {"error": "Not enough mana"}
        targets = game_state.get("targets", [])
        game_state["mana"] -= self.cost
        effect_result = self.resolve_effect(targets)["result"]
        return {"card_play": self.name,
                "mana_used": self.cost,
                "effect": effect_result}


    def resolve_effect(self, targets: list) -> dict:
        result = ""
        for target in targets:
            if self.effect_type == "heal":
                target["hp"] += 3
                result += f"{target['name']} healed 3 HP "
            elif self.effect_type == "buff":
                target["attack"] += 2
                result += f"{target['attack']} buffed by 2"
            elif self.effect_type == "damage":
                target["hp"] -= 3
                result += f"Deal 3 damage to {target['name']}"
            elif self.effect_type == "debuff":
                target["attack"] -= 1
                result += f"{target['name']}'s attack reduced by 1"
            else:
                result.append("Unknown effect")
        return {
            "result": result
        }