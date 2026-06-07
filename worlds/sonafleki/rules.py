from __future__ import annotations
from rule_builder.rules import Has, HasAll, HasAllCounts
from .Data import ItemNames, LocationNames

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import SonaflekiWorld

def set_all_rules(world: SonaflekiWorld):
    # get active levels
    active_levels = world.level_data.base_levels
    if world.options.include_five_stars:
        active_levels += world.level_data.hard_levels

    # set jump requirements for each level
    for level in active_levels:
        # get rule for having necessary jump types
        jump_map = {}
        for jump in level.jump_types:
            jump_map[ItemNames.jump_types[jump]] = 1
        has_jumps = HasAllCounts(jump_map)

        # for some reason the locations need their rules set individually
        locations = world.get_region(level.name).get_locations()
        for location in locations:
            world.set_rule(location, has_jumps)

    #set house requirements
    requirement = 0
    for house in LocationNames.houses:
        if requirement != 0:
            entrance = world.get_entrance("to " + house)
            has_gratitudes = HasAllCounts({ItemNames.gratitude: requirement})
            world.set_rule(entrance, has_gratitudes)
        requirement += world.gratitudes_per_house

    # set final level requirements
    jump_types = ItemNames.jump_types
    has_jumps = HasAll(jump_types[0], jump_types[1], jump_types[2], jump_types[3], jump_types[4])
    has_gratitudes = HasAllCounts({ItemNames.gratitude : world.gratitudes_required})
    ascension = world.get_entrance("to Ascension")
    world.set_rule(ascension, has_jumps & has_gratitudes)

    # set statue rules based on statue sanity level
    for i in range(4):
        statue_prefix = LocationNames.statue_prefixes[i]
        for statue_suffix in LocationNames.statue_suffixes:
            statue_name = statue_prefix + statue_suffix
            gratitude_name = statue_name + LocationNames.single_gratitude_suffix
            gratitude = world.get_location(gratitude_name)
            match world.options.statue_sanity_level:
                case 1:
                    world.set_rule(gratitude, Has(ItemNames.all_statues))
                case 2:
                    world.set_rule(gratitude, Has(ItemNames.statue_types[i]))
                case 3:
                    world.set_rule(gratitude, Has(statue_name))

    # set teleporter rules based on teleport sanity level
    for teleporter_suffix in LocationNames.teleporter_suffixes:
        teleporter_name = LocationNames.teleporter_prefix + teleporter_suffix
        gratitude_name = teleporter_name + LocationNames.single_gratitude_suffix
        gratitude = world.get_location(gratitude_name)
        match world.options.teleport_sanity_level:
            case 1:
                world.set_rule(gratitude, Has(ItemNames.all_teleporters))
            case 2:
                world.set_rule(gratitude, Has(teleporter_name))

    # set fetch item rules based on fetch sanity level
    for fetch_item in LocationNames.fetch_items:
        for suffix in LocationNames.fetch_gratitude_suffixes:
            name = fetch_item + LocationNames.gratitude_prefix + suffix
            gratitude = world.get_location(name)
            match world.options.fetch_sanity_level:
                case 1:
                    world.set_rule(gratitude, Has(ItemNames.all_fetch_items))
                case 2:
                    world.set_rule(gratitude, Has(fetch_item))

    # set victory condition
    world.set_completion_rule(Has("Victory"))