from __future__ import annotations
from BaseClasses import Item, ItemClassification
from .Data import ItemNames

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import SonaflekiWorld

class SonaflekiItem(Item):
    game = "SONAFLEKI"

def create_and_classify_item(world : SonaflekiWorld, name : str):
    mapping = world.item_name_to_id
    if name not in mapping:
        name = ItemNames.egg

    item_id = mapping[name]
    grat_id = mapping[ItemNames.gratitude]
    egg_id = mapping[ItemNames.egg]

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

    # add gratitudes
    for i in range(world.options.total_gratitudes):
        item_pool.append(world.create_item(ItemNames.gratitude))

    # add jump types
    for i in range(5):
        if i != world.starting_jump:
            name = ItemNames.jump_types[i]
            item_pool.append(world.create_item(name))
    if world.options.include_tidepool:
        name = ItemNames.jump_types[-1]
        item_pool.append(world.create_item(name))

    # add statues (depending on statue sanity level)
    statue_sanity = world.options.statue_sanity_level
    match statue_sanity:
        case 1:
            item_pool.append(world.create_item(ItemNames.all_statues))
        case 2:
            for statue_type in ItemNames.statue_types:
                item_pool.append(world.create_item(statue_type))
        case 3:
            prefixes = ItemNames.statue_prefixes
            suffixes = ItemNames.statue_suffixes
            for prefix in prefixes:
                for suffix in suffixes:
                    name = prefix + suffix
                    item_pool.append(world.create_item(name))

    # add teleporters (depending on teleport sanity level)
    teleport_sanity = world.options.teleport_sanity_level
    match teleport_sanity:
        case 1:
            item_pool.append(world.create_item(ItemNames.all_teleporters))
        case 2:
            prefix = ItemNames.teleporter_prefix
            suffixes = ItemNames.teleporter_suffixes
            for suffix in suffixes:
                name = prefix + suffix
                item_pool.append(world.create_item(name))

    # add fetch quest items (depending on fetch sanity level)
    fetch_sanity = world.options.fetch_sanity_level
    match fetch_sanity:
        case 1:
            item_pool.append(world.create_item(ItemNames.all_fetch_items))
        case 2:
            for fetch_item in ItemNames.fetch_items:
                item_pool.append(world.create_item(fetch_item))

    # add filler items
    num_items = len(item_pool)
    num_unfilled = len(world.multiworld.get_unfilled_locations(world.player))
    filler_count = num_unfilled - num_items
    item_pool += [world.create_filler() for _ in range(filler_count)]

    #TODO: traps

    world.multiworld.itempool += item_pool