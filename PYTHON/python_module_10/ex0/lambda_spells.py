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
    artifacts = [{'name': 'Storm Crown', 'power': 64, 'type': 'relic'}, {'name': 'Shadow Blade', 'power': 106, 'type': 'armor'}, {'name': 'Storm Crown', 'power': 68, 'type': 'focus'}, {'name': 'Water Chalice', 'power': 74, 'type': 'focus'}]
    mages = [{'name': 'Kai', 'power': 74, 'element': 'ice'}, {'name': 'River', 'power': 59, 'element': 'lightning'}, {'name': 'Sage', 'power': 86, 'element': 'ice'}, {'name': 'Morgan', 'power': 75, 'element': 'lightning'}, {'name': 'Sage', 'power': 54, 'element': 'fire'}]
    spells = ['darkness', 'tornado', 'flash', 'lightning']

    print("\nTesting artifacts sorter...")
    print(f"{artifacts[0]['name']}", end="")
    print(f" ({artifact_sorter(artifacts)[0]['power']} ", end="")
    print(f"power) comes before {artifacts[1]['name']} ", end="")
    print(f"({artifact_sorter(artifacts)[1]['power']} power)")

    print("\nTesting power filter")
    print(power_filter(mages, 70))

    result = spell_transformer(spells)
    print("\nTesting spell transformer...")
    for i in range(len(result)):
        if i < len(spells) - 1:
            print(result[i], end=" ")
        else:
            print(result[i])

    print("\nTesting mage stats")
    print(mage_stats(mages))
