from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups

class SonaflekiWebWorld(WebWorld):
    game = "SONAFLEKI"
    theme = "grassFlowers"

    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Sonafleki in Archipelago.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["Purrfexionator"]
    )

    tutorials = [setup_en]

    option_groups = option_groups