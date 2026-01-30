#!/usr/bin/env python3
import sys


def max_min(dico: dict) -> tuple:
    maxi = 0
    weapon_abundant = ""
    weapon_less_abundant = ""
    for item in dico:
        if dico[item] > maxi:
            maxi = dico[item]
            weapon_abundant = item
    mini = maxi
    for item in dico:
        if dico[item] < mini:
            mini = dico[item]
            weapon_less_abundant = item
    return (weapon_abundant, weapon_less_abundant, mini, maxi)


def restock(dico: dict) -> list:
    need_to_restock = []
    for item in dico:
        if dico[item] == 1:
            need_to_restock.append(item)
    return (need_to_restock)


def all_keys(dico: dict) -> list:
    keys = []
    for item in dico:
        keys.append(item)
    return (keys)


def all_values(dico: dict) -> list:
    values = []
    for item in dico:
        values.append(dico[item])
    return (values)


def there_is_sword(dico: dict, bool: bool = False) -> bool:
    for item in dico:
        if item == "sword":
            bool = True
    return (bool)


def main() -> None:
    compteur = 0
    i = 0
    dico = dict()
    moderate_dict = dict()
    scarce_dict = dict()
    try:
        for item in sys.argv[1:]:
            dico[item.split(":")[0]] = int(item.split(":")[1])
    except ValueError:
        print("Enter a key associate to a value in the", end="")
        print("following format : \"weapon:value\"")
        return
    for key, value in dico.items():
        if value >= 5:
            moderate_dict[key] = value
        else:
            scarce_dict[key] = value
    print("=== Inventory System Analysis ===")
    weapon_abundant, weapon_less_abundant, mini, maxi = max_min(dico)
    for item in dico:
        compteur = compteur + dico[item]
        i += 1
    print(f"Total items in inventory: {compteur}")
    print(f"Unique item types: {i}\n")
    print("=== Current Inventory ===")
    i = 0
    for item in dico:
        percentage = round(dico[item] / compteur * 100, 1)
        i += 1
        print(f"{sys.argv[i]} units ({percentage}%)")
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {weapon_abundant} ({maxi} units)")
    if mini == 1:
        print(f"Least abundant: {weapon_less_abundant} ({mini} unit)")
    else:
        print(f"Least abundant: {weapon_less_abundant} ({mini} units)")
    print("\n=== Item Categories ===")
    print(f"Moderate: {moderate_dict}")
    print(f"Scarce: {scarce_dict}")
    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock(dico)}")
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {all_keys(dico)}")
    print(f"Dictionary values: {all_values(dico)}")
    print(f"Sample lookup - 'sword' in inventory: {there_is_sword(dico)}")


if __name__ == "__main__":
    main()
