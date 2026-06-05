from typing import Mapping, Any

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

    level_data : levels.SonaflekiLevels
    starting_jump : int

    def generate_early(self) -> None:
        level_data = levels.SonaflekiLevels(self)
        starting_jump = self.random.randint(0, 4)
        randomization = self.options.level_randomization.value
        if randomization > 0:
            level_data.randomize(randomization)

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