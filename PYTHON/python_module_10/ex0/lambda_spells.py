def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact['power'],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    min_power = min(mages, key=lambda mage: mage["power"])
    max_power = max(mages, key=lambda mage: mage["power"])

    int_power = [elemt["power"] for elemt in mages]
    avg_power = round(sum(int_power) / len(mages), 2)
    return {"max_power": max_power["power"],
            "min_power": min_power["power"], "avg_power": avg_power}


if __name__ == "__main__":
    artifact = [{"name": "Fire Staff", "power": 92},
                {"name": "Crystal Orb", "power": 85}]
    mages = [{"power": 89}, {"power": 312}, {"power": 212},
             {"power": 3102}, {"power": 214542}]
    spells = ["Fireball", "Snowball", "Zap"]

    print("\nTesting artifact sorter...")
    print(f"{artifact[0]['name']}", end="")
    print(f" ({artifact_sorter(artifact)[0]['power']} ", end="")
    print(f"power) comes before {artifact[1]['name']} ", end="")
    print(f"({artifact_sorter(artifact)[1]['power']} power)")

    print("\nTesting power filter")
    print(power_filter(mages, 92))

    print("\nTesting spell transformer...")
    print(spell_transformer(spells))

    print("\nTesting mage stats")
    print(mage_stats(mages))
