from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana = 10
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        def get_attack(card):
            return getattr(card, "attack", 0)

        hand_sorted = sorted(hand, key=get_attack, reverse=True)

        for card in hand_sorted:
            cost = getattr(card, "cost", 0)
            attack = getattr(card, "attack", 0)

            if cost <= mana:
                mana -= cost
                mana_used += cost
                cards_played.append(card.name)
                damage_dealt += attack
                battlefield.append(card)
        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets, key=lambda target: target["hp"])
