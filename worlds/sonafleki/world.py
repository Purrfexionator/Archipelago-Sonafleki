from typing import Mapping, Any
from unittest import case

from worlds.AutoWorld import World
from . import web_world, items, levels, locations
from . import options as sonafleki_options
from .Data import ItemNames, LocationNames


class SonaflekiWorld(World):
    """
    SONAFLEKI is a precision-platforming collectathon that controls like the genesis game "Flicky".
    Explore a massive overworld, play linear levels, collect new double jump types, and get lost.
    """

    game = "SONAFLEKI"
    web = web_world.SonaflekiWebWorld()
    options_dataclass = sonafleki_options.SonaflekiOptions
    options: sonafleki_options.SonaflekiOptions

    item_name_to_id = ItemNames.get_mapping()
    location_name_to_id = LocationNames.get_mapping()
    origin_region_name = "Overworld"

    level_data : levels.SonaflekiLevels
    starting_jump : int

    existing_gratitudes : int
    gratitudes_required : int
    gratitudes_per_house : int
    gratitudes_added = 0

    def generate_early(self) -> None:
        # get level data and pick starting jump
        self.level_data = levels.SonaflekiLevels(self)
        self.starting_jump = self.random.randint(0, 4)
        randomization = self.options.level_randomization.value
        if randomization > 0:
            self.level_data.randomize(randomization)

        # count slots based on settings
        slots = 100 # base game gratitude slots

        # token slots
        token_count = 5 * self.options.tokens_per_house.value
        level_count = 15 if self.options.include_five_stars else 13
        token_count += level_count * self.options.extra_tokens_per_level.value
        slots += token_count

        # tutorial slots
        if not self.options.skip_tutorials:
            slots += 6 if self.options.include_tidepool else 5

        # checkpoint slots
        if self.options.checkpoint_sanity:
            checkpoint_count = 0

            included_levels = self.level_data.base_levels
            if self.options.include_five_stars:
                included_levels += self.level_data.hard_levels

            for level in included_levels:
                checkpoint_count += level.num_checkpoints

            slots += checkpoint_count

        # count items based on settings
        item_count = 5 # base jump types

        #statues
        match self.options.statue_sanity_level:
            case 1: item_count += 1
            case 2: item_count += 4
            case 3: item_count += 16

        # teleporters
        match self.options.teleport_sanity_level:
            case 1: item_count += 1
            case 2: item_count += 5

        # fetch items
        match self.options.fetch_sanity_level:
            case 1: item_count += 1
            case 2: item_count += 4

        # determine available slots, resolve flicky count
        available_slots = slots - item_count
        self.existing_gratitudes = min(self.options.total_gratitudes.value, available_slots)
        self.gratitudes_required = round(self.existing_gratitudes * (self.options.gratitudes_required.value / 100.0))
        self.gratitudes_per_house = round(self.existing_gratitudes * (self.options.gratitudes_per_house.value / 100.0))

    def create_regions(self) -> None:
        locations.create_and_connect_regions(self)
        locations.create_locations(self)

    def set_rules(self) -> None:
        # TODO: set rules
        pass

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str):
        return items.create_and_classify_item(self, name)

    def get_filler_item_name(self) -> str:
        return ItemNames.egg

    def fill_slot_data(self) -> Mapping[str, Any]:
        # TODO: write room ordering and options
        return {}