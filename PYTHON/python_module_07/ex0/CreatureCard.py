from Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        if attack <= 0:
            raise ValueError("The creature needs to inflige damage")
        self.health = health
        if health <= 0:
            raise ValueError("The creature needs HP to live")

    def play(self, game_state: dict) -> dict:
        pass

    # def attack_target(self, target) -> dict:

