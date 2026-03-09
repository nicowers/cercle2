from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

if __name__ == "__main__":
    # Création de la factory et du moteur de jeu

    factory = FantasyCardFactory()
    engine = GameEngine()
    strategy = engine.get_engine_status()["strategy_used"]
    # Configuration du moteur avec la stratégie
    engine.configure_engine(factory, AggressiveStrategy())
    creature1 = factory.create_creature("Dragon King")
    creature2 = factory.create_creature(6),
    spell1 = factory.create_spell("Fire Blast"),
    spell2 = factory.create_spell(3),
    artifact1 = factory.create_artifact("Ancient Ring"),
    artifact2 = factory.create_artifact(5)
    card_created = [creature1, creature2, spell1, spell2,
                    artifact1, artifact2]
    engine.deck.extend(card_created)
    card = engine.deck.pop(0)
    engine.hand.append(card)
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    print("Factory: FantasyCardFactory")
    print("Strategy:", strategy)
    print("Available types:", factory.get_supported_types())

    print("\nSimulating aggressive turn...")

    # Simulation du tour
    result = engine.simulate_turn()

    # Affichage de la main et du battlefield après le tour
    print("Hand:", result["hand"])

    print("\nTurn execution:")
    print("Strategy:", strategy)
    print("Actions:", result["action"])

    # Statistiques finales
    report = engine.get_engine_status()
    print("\nGame Report:")
    print(report)

    print("\nAbstract Factory + Strategy Pattern: ", end="")
    print("Maximum flexibility achieved!")
