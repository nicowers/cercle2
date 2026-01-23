#!/usr/bin/env python3

if __name__ == "__main__":
    s = {
        "alice" : {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'},
        "bob" : {'first_kill', 'level_10', 'boss_slayer', 'collector'},
        "charlie" : {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
        }
    print("=== Achievement Tracker System ===")
    for players in s:
        print(f"Player {players}: {s[players]}")
    print("\n=== Achievement Analytics ===")
    all_unique_achievements = set()
    common_to_all_players = s['alice']
    for players in s:
        all_unique_achievements = all_unique_achievements.union(s[players])
        common_to_all_players = common_to_all_players.intersection(s[players])
    print(f"All unique achievements: {all_unique_achievements}")
    print("Total unique achievements:", len(all_unique_achievements))
    print("\nCommon to all players:", common_to_all_players)
    achievement_count = {}
    for achievements in s.values():
        for achievement in achievements:
            achievement_count[achievement] = achievement_count.get(achievement, 0) + 1
    unique_achievements = set()
    for achievement, count in achievement_count.items():
        if count == 1:
            unique_achievements.add(achievement)
    print(f"Rare achievements: {unique_achievements}\n")
    a_and_b_common = s['alice'].intersection(s['bob'])
    a_unique = s['alice'].difference(a_and_b_common)
    b_unique = s['bob'].difference(a_and_b_common)
    print(f"Alice vs Bob common: {a_and_b_common}")
    print(f"Alice unique: {a_unique}")
    print(f"Bob unique: {b_unique}")
