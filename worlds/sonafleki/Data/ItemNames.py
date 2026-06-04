jump_types = [ "Double Jump", "Quad Jump", "Flutter Jump", "Dip Jump", "Invert Jump"]

all_statues = "All Statues"
all_teleporters = "All Teleporters"
all_fetch_items = "All Fetch Items"

statue_types = ["Frog Statues", "Eagle Statues", "Cat Statues", "Arch Statues"]
statue_prefixes = ["Frog Statue ", "Eagle Statue ", "Cat Statue ", "Arch Statue "]
statue_suffixes = ["A", "B", "C", "D"]

teleporter_prefix = "Teleporter "
teleporter_suffixes = ["A", "B", "C", "D", "E"]

fetch_items = ["Rose", "Basket", "Controller", "Rake", "Pickaxe"]

gratitude = "Gratitude"
egg = "Egg"

traps = ["Trap 1", "Trap 2", "Trap 3"]

def get_mapping():
    mapping = {}
    index = 0

    standard_names = (jump_types + statue_types + fetch_items +
                      [all_statues, all_teleporters, all_fetch_items])

    for name in standard_names:
        mapping[index] = name
        index += 1

    for statue_prefix in statue_prefixes:
        for statue_suffix in statue_suffixes:
            name = statue_prefix + statue_suffix
            mapping[index] = name
            index += 1

    for teleporter_suffix in teleporter_suffixes:
        name = teleporter_prefix + teleporter_suffix
        mapping[index] = name
        index += 1

    mapping[index] = gratitude
    mapping[index + 1] = egg
    index += 2

    for trap in traps:
        mapping[index] = trap
        index += 1