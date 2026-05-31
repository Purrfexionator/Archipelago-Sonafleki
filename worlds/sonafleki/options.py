from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, DeathLink, Range, Toggle, DefaultOnToggle

class DeathLinkAmnesty(Range):
    """
    How many deaths it takes to send a DeathLink
    """
    display_name = "Death Link Amnesty"
    range_start = 1
    range_end = 30
    default = 10

class TotalGratitudes(Range):
    """
    Maximum number of how many Gratitudes can exist
    """
    display_name = "Total Gratitudes"
    range_start = 0
    range_end = 100
    default = 50

class GratitudesRequiredPercentage(Range):
    """
    Percentage of existing Gratitudes you must receive to access your Goal Area
    """
    display_name = "Gratitudes Required Percentage"
    range_start = 0
    range_end = 100
    default = 50

class SkipTutorials(Toggle):
    """
    Determines whether tutorial stages after obtaining jump types are skipped.
    """
    display_name = "Include Tutorials"

class IncludeFiveStars(Toggle):
    """
    Determines whether five-star optional challenge stages are included.
    """
    display_name = "Include Five-Star Stages"

class StatueSanityLevel(Choice):
    """
    Determines if and how overworld statues are shuffled into the item pool.

    None: Statues simply exist in the world by default.
    Tame: Statues are shuffled into the item pool as a singular item.
    Standard: Each individual statue type is shuffled into the item pool.
    Insane: Every single individual statue is shuffled into the item pool.
    """
    display_name = "Statuesanity Level"
    option_none = 0
    option_tame = 1
    option_standard = 2
    option_insane = 3
    default = option_standard

class TeleportSanityLevel(Toggle):
    """
    Determines if and how overworld teleporters are shuffled into the item pool.

    None: Teleporters simply exist in the world by default.
    Standard: Teleporters are shuffled into the item pool as a singular item.
    Insane: Each individual teleporter is shuffled into the item pool.
    """
    display_name = "Teleportsanity Level"
    option_none = 0
    option_standard = 1
    option_insane = 2
    default = option_standard

class FetchSanityLevel(Choice):
    """
    Determines if and how overworld fetch quest items are shuffled into the item pool.
    None: Fetch quest items simply exist in the world by default.
    Standard: Fetch quest items are shuffled into the item pool as a singular item.
    Insane: Each individual fetch quest item is shuffled into the item pool.
    """
    display_name = "Fetchsanity level"
    option_none = 0
    option_standard = 1
    option_insane = 2
    default = option_standard

class CheckpointSanity(Toggle):
    """
    Determines whether individual checkpoints grant location checks.
    """
    display_name = "Checkpointsanity"

@dataclass
class SonaflekiOptions(PerGameCommonOptions):
    #game options
    death_link: DeathLink
    death_link_amnesty: DeathLinkAmnesty

    #general options
    total_gratitudes: TotalGratitudes
    gratitudes_required: GratitudesRequiredPercentage
    skip_tutorials: SkipTutorials
    include_five_stars: IncludeFiveStars
    # TODO: jump type spawning
    # spawning style (consistent, semirandom, everywhere, hidden)
    # - consistent is outside usual house
    # - semirandom is outside at random house
    # - everywhere spawns on every screen until picked up
    # - hidden spawns in a random point on the map
    # TODO: token and gratitude distribution
    # number of tokens in each house
    # number of extra tokens rewarded for completing a level

    #sanity options
    statue_sanity_level: StatueSanityLevel
    teleport_sanity_level: TeleportSanityLevel
    fetch_sanity_level: FetchSanityLevel
    checkpoint_sanity: CheckpointSanity

    # TODO: randomization options
    # level randomization (none, low, medium, high)
    # - low shuffles segments per-level
    # - medium shuffles segments between levels with matching jump types
    # - high shuffles segments entirely randomly
    # - "variety" setting for max different jump types that can exist in a level on high (default is 2, goes up to 5)
    # randomize level locations (on the map)
    # randomize music
    # gratitude distribution (standard, even, or random)

    # TODO: traps
    # trap fill percentage
    # design individual traps and give weights

#TODO: option groups