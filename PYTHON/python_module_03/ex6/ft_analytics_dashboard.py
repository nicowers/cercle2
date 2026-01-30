#!/usr/bin/env python3

players = {
    'alice':
    {
        "score": 2300,
        "active_player": True,
        "region": "north",
        "achievements": [
            'first_kill', 'level_10', 'boss_slayer', 'level_10', 'boss_slayer'
            ]
    },
    'bob':
    {
        "score": 1800,
        "active_player": True,
        "region": "east",
        "achievements": ['first_kill', 'level_10', 'boss_slayer']
    },
    'charlie':
    {
        "score": 2150,
        "active_player": True,
        "region": "central",
        "achievements": [
            'first_kill', 'first_kill', 'level_10',
            'boss_slayer', 'first_kill', 'level_10', 'boss_slayer'
            ]
    },
    'diana':
    {
        "score": 2050,
        "active_player": False,
        "region": "south",
        "achievements": ['first_kill']
    },
}


def score_categorie() -> dict[str, int]:
    return {
        categorie: (
            3 if categorie == "high"
            else 2 if categorie == "medium"
            else 1
        )
        for categorie in ("high", "medium", "low")
    }


def top_perfomer() -> str:
    top_player = "alice"
    for player in players:
        if players[player]["score"] > players[top_player]["score"]:
            top_player = player
    top_score = players[top_player]["score"]
    top_achievements = len(players[top_player]["achievements"])
    return (
        f"{top_player} ({top_score} points, {top_achievements} achievements)"
        )


if __name__ == "__main__":
    high = medium = low = 0
    print("=== Game Analytics Dashboard ===")
    print("\n=== List Comprehension Examples ===")
    print("High scorers (>2000):",
          [player for player in players if players[player]["score"] > 2000])
    print("Scores doubled:",
          [players[player]["score"] * 2 for player in players])
    print("Active players:",
          [player
           for player in players if players[player]["active_player"] is True])
    print("\n=== Dict Comprehension Examples ===")
    print("Player scores:",
          {player: players[player]["score"]
           for player in players if players[player]["active_player"] is True})
    print("Score categories:", score_categorie())
    print("Achievement counts:",
          {player: len(players[player]["achievements"])
           for player in players if players[player]["active_player"] is True})
    print("\n=== Set Comprehension Examples ===")
    print("Unique players:", {player for player in players})
    print("Unique achievements:",
          {
              achievements
              for player in players
              for achievements in players[player]["achievements"]})
    print("Active regions:",
          {
              players[player]["region"]
              for player in players
              if players[player]["active_player"] is True})
    print("\n=== Combined Analysis ===")
    print("Total players:", len(players))
    print("Total unique achievements:",
          len({
              achievements
              for player in players
              for achievements in players[player]["achievements"]
              }))
    print("Average score:",
          sum(players[player]["score"]for player in players) / len(players))
    print("Top performer:", top_perfomer())
