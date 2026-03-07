from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str,
                 cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if game_state.get("mana", 0) < self.cost:
            return {"error": "Not enough mana"}
        game_state["mana"] -= self.cost
        if "artifacts_in_play" not in game_state:
            game_state["artifacts_in_play"] = []
        game_state["artifacts_in_play"].append(self)
        return {"card_play": self.name,
                "mana_used": self.cost,
                "effect": f"Permananent: +1 {self.effect} per turn"}

    def activate_ability(self, game_state: dict) -> dict:
        if self.durability <= 0:
            return {"error": f"{self.name} is broken"}

        self.durability -= 1
        result = {}
        if self.effect == "mana":
            game_state["mana"] += 1
            result = {"effect_applied": "+1 mana"}
        elif self.effect == "heal":
            if "players" in game_state:
                for player in game_state["players"]:
                    player["hp"] += 3
            result = {"effect_applied": "Healed 3 HP to all players"}
        elif self.effect == "damage":
            if "targets" in game_state:
                for target in game_state["targets"]:
                    target["hp"] -= 2
            result = {"effect_applied": "Dealt 2 damage to all targets"}

        return {
            "artifact": self.name,
            "remaining_durability": self.durability,
            "effect": self.effect,
            "result": result,
            "game_state": game_state
        }
