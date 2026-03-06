from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

class TournamentCard (Card, Combatable, Rankable):
    def __init__(self, name, cost, rarity, damage):
        super().__init__(name, cost, rarity)
        self.wins = 0
        self.losses = 0
        self.rating = 1200
        self.damage = damage

    def play(self, game_state: dict) -> dict:
        player1 = game_state["player1"]
        player2 = game_state["player2"]
        winner = None
        loser = None
        if player1.power >= player2.power:
            player1.update_wins()
            player2.update_losses()
            winner = player1
            loser = player2
        else:
            player2.update_losses()
            player2.update_wins()
            winner = player2
            loser = player1
        player1.calculate_rating()
        player2.calculate_rating()
        return {"winner": winner.name, "loser": loser.name, "winner_rating": winner.rating, "loser_rating": loser.rating}

    def attack(self, target) -> dict:
        result = target.defend(self.damage)

        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.damage,
            "result": result
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            "defender": self.name,
            "damage_received": incoming_damage
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "damage": self.damage,
            "wins": self.wins,
            "losses": self.losses
        }

    def calculate_rating(self) -> int:
        self.rating += self.wins * 16 - self.loses * 16
        return (self.rating)

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating()
        }

    def update_wins(self, wins: int) -> None:
        self.wins += 1

    def update_losses(self, losses: int) -> None:
        self.losses += 1

    def get_rank_info(self) -> dict:
        return {"name": self.name, "rating": self.rating, "wins": self.wins, "losses":self.losses}
