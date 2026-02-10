from ex0.Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        if attack <= 0:
            raise ValueError("The creature needs to inflige damage")
        self.health = health
        if health <= 0:
            raise ValueError("The creature needs HP to live")

    def play(self, game_state: dict) -> dict:
        game_state = {'card_played': self.name, 'mana_used': self.cost,'effect': 'Creature summoned to battlefield'}
        return game_state

    def get_card_info(self) -> dict:
        print("CreatureCard Info:")
        card_info = {'name': self.name,
                      'cost': self.cost, 'rarity': self.rarity,
                      'type': 'Creature', 'attack': self.attack, 'health': self.health}
        return (card_info)

    def attack_target(self, target) -> dict:
        attack_dict = {'attacker': self.name, 'target': target.name,'damage_dealt': self.attack, 'combat_resolved': False}
        if target.health <= self.attack:
            attack_dict['combat_resolved'] = True
            print(f"\n{self.name} attacks {target.name}")
        return attack_dict
