def healing_potion():
    from .elements import create_fire, create_water
    return_value = "Healing potion brewed with "
    return_value += f"{create_fire()} and {create_water()}"
    return (return_value)


def strength_potion():
    from .elements import create_earth, create_fire
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion():
    from .elements import create_air, create_water
    return_value = "Invisibility potion brewed with "
    return_value += f"{create_air()} and {create_water()}"
    return (return_value)


def wisdom_potion():
    from .elements import create_water, create_air, create_earth, create_fire
    all = create_water(), create_air(), create_earth(), create_fire()
    return ("Wisdom potion brewed with all elements:", all)
