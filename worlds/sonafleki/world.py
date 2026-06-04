from typing import Mapping, Any

from worlds.AutoWorld import World
from . import web_world
from . import options as sonafleki_options

class SonaflekiWorld(World):
    """
    SONAFLEKI is a precision-platforming collectathon that controls like the genesis game "Flicky".
    Explore a massive overworld, play linear levels, collect new double jump types, and get lost.
    """

    game = "SONAFLEKI"
    web = web_world.SonaflekiWebWorld()
    options_dataclass = sonafleki_options.SonaflekiOptions
    options: sonafleki_options.SonaflekiOptions

    # TODO: randomizer

    def create_regions(self) -> None:
        # TODO: create regions
        pass

    def set_rules(self) -> None:
        # TODO: set rules
        pass

    def create_items(self) -> None:
        # TODO: create items
        pass

    def create_item(self, name: str):
        # TODO: create item
        pass

    def get_filler_item_name(self) -> str:
        return "Egg"

    def fill_slot_data(self) -> Mapping[str, Any]:
        # TODO: write room ordering and options
        return {}