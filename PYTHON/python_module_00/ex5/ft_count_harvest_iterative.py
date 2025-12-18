def ft_count_harvest_iterative():
    remaining_days = int(input("Days until harvest: "))
    for i in range(remaining_days):
        i += 1
        print("Day", i)
    print("Harvest time!")
