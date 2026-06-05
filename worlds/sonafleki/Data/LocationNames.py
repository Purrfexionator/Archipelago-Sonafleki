levels = [
    "Touring Optimist",
    "Bamboo Catching Water",
    "Screen Time",
    "Bluebottles",
    "Art Museum",
    "Butterfly Knife",
    "Urban Sift",
    "How I Feel",
    "Nanoseconds",
    "Voices",
    "Oil Slick",
    "6ft Pool End",
    "Bird Bath",
    "Pheromones",
    "Ozone"
]

houses = [
    "House 1",
    "House 2",
    "House 3",
    "House 4",
    "House 5"
]

tutorials = [
    "Double Jump Tutorial",
    "Quad Jump Tutorial",
    "Flutter Jump Tutorial",
    "Dip Jump Tutorial",
    "Invert Jump Tutorial",
    "Dive Jump Tutorial"
]

statue_prefixes = ["Frog Statue ", "Eagle Statue ", "Cat Statue ", "Arch Statue "]
statue_suffixes = ["A", "B", "C", "D"]

teleporter_prefix = "Teleporter "
teleporter_suffixes = ["A", "B", "C", "D", "E"]

fetch_items = ["Rose", "Basket", "Controller", "Rake", "Pickaxe"]

overworld_gratitude_prefix = "Overworld Gratitude "

gratitude_prefix = " - Gratitude "
level_gratitude_suffixes = ["1", "2", "3", "4", "5", "6"]
fetch_gratitude_suffixes = ["1", "2"]
overworld_gratitude_suffixes = ["1", "2", "3", "4", "5"]
single_gratitude_suffix = " - Gratitude"

token_prefix = " - Token "
level_token_suffixes = ["1", "2", "3", "4", "5"]
house_token_suffixes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

checkpoint_prefix = " - Checkpoint "
checkpoint_suffixes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]


def get_mapping():
    mapping = {}
    index = 0

    for level in levels:
        for suffix in level_gratitude_suffixes:
            name = level + gratitude_prefix + suffix
            mapping[index] = name
            index += 1
        for suffix in level_token_suffixes:
            name = level + token_prefix + suffix
            mapping[index] = name
            index += 1
        for suffix in checkpoint_suffixes:
            name = level + checkpoint_prefix + suffix
            mapping[index] = name
            index += 1

    for house in houses:
        for suffix in house_token_suffixes:
            name = house + token_prefix + suffix
            mapping[index] = name
            index += 1

    for tutorial in tutorials:
        name = tutorial + single_gratitude_suffix
        mapping[index] = name
        index += 1

    for statue_prefix in statue_prefixes:
        for statue_suffix in statue_suffixes:
            name = statue_prefix + statue_suffix + single_gratitude_suffix
            mapping[index] = name
            index += 1

    for teleporter_suffix in teleporter_suffixes:
        name = teleporter_prefix + teleporter_suffix + single_gratitude_suffix
        mapping[index] = name
        index += 1

    for fetch_item in fetch_items:
        for suffix in fetch_gratitude_suffixes:
            name = fetch_item + gratitude_prefix + suffix
            mapping[index] = name
            index += 1

    for suffix in overworld_gratitude_suffixes:
        name = overworld_gratitude_prefix + suffix
        mapping[index] = name
        index += 1

    return mapping