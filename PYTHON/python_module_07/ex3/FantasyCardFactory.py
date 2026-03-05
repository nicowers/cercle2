from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex2.EliteCard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex3.CardFactory import CardFactory
import random

class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creature_types = ["dragon", "goblin"]
        self.spell_types = ["fireball", "icebolt"]
        self.artifact_types = ["mana_ring", "magic_staff"]

    def create_creature(self, name_or_power) -> CreatureCard:
        creatures = ["Goblin Warrior", "Fire Dragon"]
        cost = random.choice([2, 4, 3, 5])
        rarity = random.choice(["rare", "super rare", "epic", "legendary"])
        hp = random.randint(3, 10)
        if isinstance(name_or_power, int):
            name = random.choice(creatures)
            power = name_or_power
        elif isinstance(name_or_power, str):
            power = random.randint(2, 5)
            name = name_or_power
        else:
            name = random.choice(creatures)
            power = random.randint(2, 5)
        return CreatureCard(name, cost, rarity, power, hp)
    
    def create_spell(self, name_or_mana_cost) -> SpellCard:
        spells = ["Lightning Bolt", "Ice Spell"]
        rarity = random.choice(["rare", "super rare", "epic", "legendary"])
        effect_type = random.choice(["buff", "heal", "damage", "debuff"])
        if isinstance(name_or_mana_cost, str):
            name = name_or_mana_cost
            cost = random.randint(2, 5)
        elif isinstance(name_or_mana_cost, int):
            name = random.choice(spells)
            cost =name_or_mana_cost
        else:
            name = random.choice(spells)
            cost = random.randint(2, 5)
        return SpellCard(name, cost, rarity, effect_type)
    
    def create_artifact(self, name_or_durability) -> ArtifactCard:
        rarity = random.choice(["rare", "super rare", "epic", "legendary"])
        cost = random.randint(2, 6)
        effect = random.choice(["mana", "heal", "damage"])
        if isinstance(name_or_durability, str):
            name = name_or_durability
            durability = random.randint(2, 4)
        elif isinstance(name_or_durability, int):
            name = random.choice(["Mana Ring", "Gold Medallion"])
            durability = name_or_durability
        else:
            name = random.choice(["Mana Ring", "Gold Medallion"])
            durability = random.randint(2, 4)
        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        
        for _ in range(size):
            roll = random.random()
            
            if roll < 0.6:
                deck.append(self.create_creature(None))
            elif roll < 0.85:
                deck.append(self.create_spell(None))
            else:
                deck.append(self.create_artifact(None))
        
        return {
            "theme": "Fantasy",
            "size": size,
            "cards": deck
        }

    def get_supported_types(self) -> dict:
        return {
            "creatures": self.creature_types,
            "spells": self.spell_types,
            "artifacts": self.artifact_types
        }