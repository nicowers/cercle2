import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    # inventory = {

    # }

    compteur = 0
    i = 0
    for item in sys.argv[1:]:
        compteur = compteur + int(item.split(":")[1])
        i += 1
    print(f"Total items in inventory: {compteur}")
    print(f"Unique item types: {i}\n")
    print(f"=== Current Inventory ===")
    i = 0
    for item in sys.argv[1:]:
        percentage = round((int(item.split(':')[1]) / compteur) * 100, 1)
        i += 1
        print(f"{sys.argv[i]} units ({percentage}%)")
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant:")