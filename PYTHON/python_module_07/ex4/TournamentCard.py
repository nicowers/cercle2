from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard (Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int,
                 rarity: str, damage: int) -> None:
        super().__init__(name, cost, rarity)
        self.wins = 0
        self.losses = 0
        self.rating = 1200
        self.damage = damage
        if self.cost <= 0:
            raise ValueError("Cost needs to be positive")
        if self.damage <= 0:
            raise ValueError("Damage needs to be positiv")

    def play(self, game_state: dict) -> dict:
        player1 = game_state["player1"]
        player2 = game_state["player2"]
        player1_id = player1.name.split(" ")[1].lower() + "_001"
        player2_id = player2.name.split(" ")[1].lower() + "_001"
        winner = None
        loser = None
        if player1.damage >= player2.damage:
            player1.update_wins(player1.wins)
            player2.update_losses(player2.losses)
            winner = player1_id
            loser = player2_id
        else:
            player1.update_losses(player1.losses)
            player2.update_wins(player2.wins)
            winner = player2_id
            loser = player1_id
        winner_rating = player1.calculate_rating()
        loser_rating = player2.calculate_rating()
        return {"winner": winner, "loser": loser,
                "winner_rating": winner_rating, "loser_rating": loser_rating}

    def defend(self, incoming_damage: int) -> dict:
        return {
            "defender": self.name,
            "damage_received": incoming_damage
        }

    def attack(self, target: Card | Combatable) -> dict:
        result = target.defend(self.damage)

        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.damage,
            "result": result
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "damage": self.damage,
            "wins": self.wins,
            "losses": self.losses
        }

    def calculate_rating(self) -> int:
        self.rating += self.wins * 16 - self.losses * 16
        return (self.rating)

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.rating
        }

    def update_wins(self, wins: int) -> None:
        self.wins += 1

    def update_losses(self, losses: int) -> None:
        self.losses += 1

    def get_rank_info(self) -> dict:
        return {"name": self.name, "rating": self.rating,
                "wins": self.wins, "losses": self.losses}
