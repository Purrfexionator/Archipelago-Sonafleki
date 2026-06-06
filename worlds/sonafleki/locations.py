from __future__ import annotations
from BaseClasses import Region, Location
from .Data import LocationNames
from . import items, levels

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import SonaflekiWorld

class SonaflekiLocation(Location):
    game = "SONAFLEKI"

def create_and_connect_regions(world : SonaflekiWorld):
    regions = []

    # overworld and ascension are always guaranteed to be present
    overworld = Region("Overworld", world.player, world.multiworld)
    ascension = Region("Ascension", world.player, world.multiworld)
    regions += [overworld, ascension]

    # add house regions
    for house in LocationNames.houses:
        region = Region(house, world.player, world.multiworld)
        regions.append(region)

    # add tutorial regions if included
    if not world.options.skip_tutorials:
        tutorials = LocationNames.tutorials if world.options.include_tidepool else LocationNames.tutorials[:-1]
        for tutorial in tutorials:
            region = Region(tutorial, world.player, world.multiworld)
            regions.append(region)

    # retrieve level data
    active_levels = world.level_data.base_levels
    if world.options.include_five_stars:
        active_levels += world.level_data.hard_levels

    # create level regions
    for level in active_levels:
        region = Region(level.name, world.player, world.multiworld)
        regions.append(region)

    # add regions to multiworld
    world.multiworld.regions += regions

    # create connections
    overworld_region = world.get_region("Overworld")
    ascension_region = world.get_region("Ascension")
    overworld_region.connect(ascension_region, "to Ascension")
    for house in LocationNames.houses:
        region = world.get_region(house)
        overworld_region.connect(region, "to " + house)
    if not world.options.skip_tutorials:
        tutorials = LocationNames.tutorials if world.options.include_tidepool else LocationNames.tutorials[:-1]
        for tutorial in tutorials:
            region = world.get_region(tutorial)
            overworld_region.connect(region, "to " + tutorial)
    for level in active_levels:
        region = world.get_region(level.name)
        overworld_region.connect(region, "to " + level.name)

def get_location_names_with_ids(world : SonaflekiWorld, location_names : list[str]):
    return {location_name: world.location_name_to_id[location_name] for location_name in location_names}

def create_locations(world : SonaflekiWorld):
    # start by populating overworld
    overworld = world.get_region("Overworld")

    # first, create overworld gratitudes (5 total)
    overworld_gratitudes = []
    for suffix in LocationNames.overworld_gratitude_suffixes:
        name = LocationNames.overworld_gratitude_prefix + suffix
        overworld_gratitudes.append(name)
    overworld.add_locations(get_location_names_with_ids(world, overworld_gratitudes), SonaflekiLocation)

    # next, create fetch quest gratitudes (2 each)
    fetch_gratitudes = []
    for fetch_item in LocationNames.fetch_items:
        for suffix in LocationNames.fetch_gratitude_suffixes:
            name = fetch_item + LocationNames.gratitude_prefix + suffix
            fetch_gratitudes.append(name)
    overworld.add_locations(get_location_names_with_ids(world, fetch_gratitudes), SonaflekiLocation)

    # lastly, create statue and teleporter gratitudes (one per every statue and teleporter)
    challenge_gratitudes = []
    for statue_prefix in LocationNames.statue_prefixes:
        for statue_suffix in LocationNames.statue_suffixes:
            name = statue_prefix + statue_suffix + LocationNames.single_gratitude_suffix
            challenge_gratitudes.append(name)
    for teleporter_suffix in LocationNames.teleporter_suffixes:
        name = LocationNames.teleporter_prefix + teleporter_suffix + LocationNames.single_gratitude_suffix
        challenge_gratitudes.append(name)
    overworld.add_locations(get_location_names_with_ids(world, challenge_gratitudes), SonaflekiLocation)

    # next up, populate each house with the amount of tokens specified in options
    for house in LocationNames.houses:
        region = world.get_region(house)
        tokens = []
        token_count = world.options.tokens_per_house.value
        for i in range(token_count):
            token = house + LocationNames.token_prefix + LocationNames.house_token_suffixes[i]
            tokens.append(token)
        region.add_locations(get_location_names_with_ids(world, tokens), SonaflekiLocation)

    # now that overworld is done, create gratitude and token locations for each level
    active_levels = world.level_data.base_levels
    if world.options.include_five_stars:
        active_levels += world.level_data.hard_levels

    for level in active_levels:
        region = world.get_region(level.name)
        rewards = []

        for i in range(level.num_gratitudes):
            gratitude = level.name + LocationNames.gratitude_prefix + LocationNames.level_gratitude_suffixes[i]
            rewards.append(gratitude)

        token_count = world.options.extra_tokens_per_level.value
        if (token_count > 0):
            for i in range(token_count):
                token = level.name + LocationNames.token_prefix + LocationNames.level_token_suffixes[i]
                rewards.append(token)

        if world.options.checkpoint_sanity:
            for i in range(level.num_checkpoints):
                checkpoint = level.name + LocationNames.checkpoint_prefix + LocationNames.checkpoint_suffixes[i]
                rewards.append(checkpoint)

        region.add_locations(get_location_names_with_ids(world, rewards), SonaflekiLocation)

    # final step: add victory event
    ascension = world.get_region("Ascension")
    ascension.add_event("Game Completed", "Victory", location_type = SonaflekiLocation, item_type = items.SonaflekiItem)