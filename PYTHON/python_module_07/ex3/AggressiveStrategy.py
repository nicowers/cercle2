# from ex3.GameStrategy import GameStrategy

# class AggressiveStrategy(GameStrategy):
#     def execute_turn(self, hand: list, battlefield: list) -> dict:
#         mana = 10
#         cards_played = []
#         mana_used = 0
#         damage_dealt = 0
#         hand.sort(key =lambda card: card.cost)
#         for card in hand:
#             if card.cost <= mana:
#                 mana -= card.cost
#                 mana_used += card.cost
#                 cards_played.append(card.name)
#                 damage_dealt += card.attack
#                 battlefield.append(card)
#         return {
#         "strategy": self.get_strategy_name(),
#         "cards_played": cards_played,
#         "mana_used": mana_used,
#         "targets_attacked": ["Enemy Player"],
#         "damage_dealt": damage_dealt
#         }


#     def get_strategy_name(self) -> str:
#         return "AgressiveStrategy"

#     def prioritize_targets(self, available_targets: list) -> list:
#         return sorted(available_targets, key=lambda target: target["hp"])

# from ex3.GameStrategy import GameStrategy
# from ex0.CreatureCard import CreatureCard

# class AggressiveStrategy(GameStrategy):
#     def execute_turn(self, hand: list, battlefield: list) -> dict:
#         mana = 10
#         cards_played = []
#         mana_used = 0
#         damage_dealt = 0

#         # jouer les cartes les moins chères d'abord
#         hand.sort(key=lambda card: card.cost)

#         for card in hand[:]:  # [:] pour copier la liste et pouvoir retirer ensuite si nécessaire
#             if card.cost <= mana:
#                 mana -= card.cost
#                 mana_used += card.cost
#                 cards_played.append(card.name)
                
#                 # calculer les dégâts uniquement si c'est une créature
#                 if isinstance(card, CreatureCard):
#                     damage_dealt += getattr(card, "attack", 0)  # ou card.power si tu utilises power
                
#                 battlefield.append(card)

#         return {
#             "strategy": self.get_strategy_name(),
#             "cards_played": cards_played,
#             "mana_used": mana_used,
#             "targets_attacked": ["Enemy Player"],
#             "damage_dealt": damage_dealt
#         }

#     def get_strategy_name(self) -> str:
#         return "AggressiveStrategy"

#     def prioritize_targets(self, available_targets: list) -> list:
#         return sorted(available_targets, key=lambda target: target["hp"])

from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana = 10  # mana disponible pour le tour
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        # On trie la main pour prioriser les cartes avec attaque (ex: créatures)
        hand_sorted = sorted(hand, key=lambda c: getattr(c, "attack", 0), reverse=True)

        for card in hand_sorted:
            cost = getattr(card, "cost", 0)
            attack = getattr(card, "attack", 0)  # Créatures ont attack, sorts/artifacts peuvent avoir 0

            if cost <= mana:
                mana -= cost
                mana_used += cost
                cards_played.append(card.name)
                damage_dealt += attack
                battlefield.append(card)

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets, key=lambda target: target["hp"])