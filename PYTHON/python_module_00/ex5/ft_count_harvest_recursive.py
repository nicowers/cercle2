def ft_count_harvest_recursive(days: int, count=1):
    if days is None:
        days = int(input("Days until harvest: "))
    if days == 0:
        return print("Harvest Time!")
    else:
        print(f"Day {count}")
        return ft_count_harvest_recursive(days - 1, count + 1)