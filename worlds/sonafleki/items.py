from BaseClasses import Item, ItemClassification
from .world import SonaflekiWorld

ITEM_NAME_TO_ID = {
    "Double Jump": 1,
    "Quad Jump": 2,
    "Flutter Jump": 3,
    "Dip Jump": 4,
    "Invert Jump": 5,

    "All Statues": 6,
    "All Teleporters": 7,
    "All Fetch Items": 8,

    "Frog Statues": 9,
    "Eagle Statues": 10,
    "Cat Statues": 11,
    "Arch Statues": 12,

    "Frog Statue A" : 13,
    "Frog Statue B" : 14,
    "Frog Statue C" : 15,
    "Frog Statue D" : 16,

    "Eagle Statue A" : 17,
    "Eagle Statue B" : 18,
    "Eagle Statue C" : 19,
    "Eagle Statue D" : 20,

    "Cat Statue A" : 21,
    "Cat Statue B" : 22,
    "Cat Statue C" : 23,
    "Cat Statue D" : 24,

    "Arch Statue A" : 25,
    "Arch Statue B" : 26,
    "Arch Statue C" : 27,
    "Arch Statue D" : 28,

    "Teleporter A": 29,
    "Teleporter B": 30,
    "Teleporter C": 31,
    "Teleporter D": 32,
    "Teleporter E": 33,

    "Fetch Item A": 34,
    "Fetch Item B": 35,
    "Fetch Item C": 36,
    "Fetch Item D": 37,
    "Fetch Item E": 38,

    "Gratitude" : 39,
    "Egg" : 40,

    "Trap" : 41
}

class SonaflekiItem(Item):
    game = "SONAFLEKI"

def create_and_classify_item(world : SonaflekiWorld, name : str):
    if name not in ITEM_NAME_TO_ID:
        name = "Egg"

    item_id = ITEM_NAME_TO_ID[name]
    grat_id = ITEM_NAME_TO_ID["Gratitude"]
    egg_id = ITEM_NAME_TO_ID["Egg"]

    if item_id < grat_id:
        item_class = ItemClassification.progression
    elif item_id == grat_id:
        item_class = ItemClassification.useful
    elif item_id == egg_id:
        item_class = ItemClassification.filler
    else:
        item_class = ItemClassification.trap

    return SonaflekiItem(name, item_class, item_id, world.player)

def create_all_items(world : SonaflekiWorld):

    item_pool = []

    for i in range(world.options.total_gratitudes):
        item_pool.append(world.create_item("Gratitude"))

    item_pool.append(world.create_item("Double Jump"))
    item_pool.append(world.create_item("Quad Jump"))
    item_pool.append(world.create_item("Flutter Jump"))
    item_pool.append(world.create_item("Dip Jump"))
    item_pool.append(world.create_item("Invert Jump"))

    statue_sanity = world.options.statue_sanity_level
    match statue_sanity:
        case 1:
            item_pool.append(world.create_item("All Statues"))
        case 2:
            item_pool.append(world.create_item("Frog Statues"))
            item_pool.append(world.create_item("Eagle Statues"))
            item_pool.append(world.create_item("Cat Statues"))
            item_pool.append(world.create_item("Arch Statues"))
        case 3:
            item_pool.append(world.create_item("Frog Statue A"))
            item_pool.append(world.create_item("Frog Statue B"))
            item_pool.append(world.create_item("Frog Statue C"))
            item_pool.append(world.create_item("Frog Statue D"))
            item_pool.append(world.create_item("Eagle Statue A"))
            item_pool.append(world.create_item("Eagle Statue B"))
            item_pool.append(world.create_item("Eagle Statue C"))
            item_pool.append(world.create_item("Eagle Statue D"))
            item_pool.append(world.create_item("Cat Statue A"))
            item_pool.append(world.create_item("Cat Statue B"))
            item_pool.append(world.create_item("Cat Statue C"))
            item_pool.append(world.create_item("Cat Statue D"))
            item_pool.append(world.create_item("Arch Statue A"))
            item_pool.append(world.create_item("Arch Statue B"))
            item_pool.append(world.create_item("Arch Statue C"))
            item_pool.append(world.create_item("Arch Statue D"))

    teleport_sanity = world.options.teleport_sanity_level
    match teleport_sanity:
        case 1:
            item_pool.append(world.create_item("All Teleporters"))
        case 2:
            item_pool.append(world.create_item("Teleporter A"))
            item_pool.append(world.create_item("Teleporter B"))
            item_pool.append(world.create_item("Teleporter C"))
            item_pool.append(world.create_item("Teleporter D"))
            item_pool.append(world.create_item("Teleporter E"))

    fetch_sanity = world.options.fetch_sanity_level
    match fetch_sanity:
        case 1:
            item_pool.append(world.create_item("All Fetch Items"))
        case 2:
            item_pool.append(world.create_item("Fetch Item A"))
            item_pool.append(world.create_item("Fetch Item B"))
            item_pool.append(world.create_item("Fetch Item C"))
            item_pool.append(world.create_item("Fetch Item D"))
            item_pool.append(world.create_item("Fetch Item E"))

    num_items = len(item_pool)
    num_unfilled = len(world.multiworld.get_unfilled_locations(world.player))
    filler_count = num_items - num_unfilled
    item_pool += [world.create_filler() for _ in range(filler_count)]

    #TODO: traps

    world.multiworld.itempool += item_pool