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
    default = 80

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

class IncludeTidepool(Toggle):
    """
    Determines whether the "tidepool" area is included.
    """
    display_name = "Include Tidepool"

class TrueEnding(Toggle):
    """
    Determines whether the true finale must be completed.
    """
    display_name = "True Ending"

class JumpTypeSpawning(Choice):
    """
    When receiving a jump type, rather than gaining access to it immediately,
    it will spawn somewhere in the overworld and trigger its respective cutscene
    and tutorial level when found. This setting determines where and how new
    jump types are spawned.

    Consistent: Jump types always spawn outside the house where you'd normally get them.
    Semirandom: Each jump type will spawn outside a random house.
    Everywhere: Jump types will spawn in every screen until you pick them up.
    Hidden: Jump types will spawn in a random location on the map.
    """
    display_name = "Jump Type Spawning"
    option_consistent = 0
    option_semirandom = 1
    option_everywhere = 2
    option_hidden = 3
    default = option_consistent

class TokensPerHouse(Range):
    """
    Amount of tokens that will spawn in each house. Each token grants a location check.
    """
    display_name = "Tokens Per House"
    range_start = 1
    range_end = 10
    default = 3

class ExtraTokensPerLevel(Range):
    """
    Amount of extra tokens awarded for completing any level. Each token grants a location check.
    """
    display_name = "Extra Tokens Per Level"
    range_start = 0
    range_end = 5
    default = 0

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

class TeleportSanityLevel(Choice):
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

class LevelRandomization(Choice):
    """
    Determines if and how the structuring of levels is randomized.

    None: Levels have no randomization.
    Low: Each level has the order of its own gameplay segments shuffled.
    Medium: Gameplay segments are shuffled between levels with the same jump type.
    High: Gameplay segments are shuffled between all levels.
    """
    display_name = "Level Randomization"
    option_none = 0
    option_low = 1
    option_medium = 2
    option_high = 3
    default = option_none

class MaxVarietyOnHigh(Range):
    """
    The maximum amount of different jump types a level can contain when "high" randomization is enabled.
    """
    display_name = "Max Variety On High"
    range_start = 2
    range_end = 5
    default = 2

class GratitudeDistribution(Choice):
    """
    Determines how gratitude rewards (and thus location checks) are distributed among levels.
    Note that the total amount of gratitudes available from levels will remain the same.

    Standard: Each level gives the amount of gratitudes it normally would.
    Even: All levels gives the exact same amount of gratitudes.
    Random: Each level gives a random amount of gratitudes.
    """
    display_name = "Gratitude Distribution"
    option_standard = 0
    option_even = 1
    option_randomized = 2

class RandomizeLevelLocations(Toggle):
    """
    Determines whether the locations of levels on the map are randomized.
    """
    display_name = "Randomize Level Locations"

class RandomizeMusic(Toggle):
    """
    Determines whether the music for each level is randomized.
    """
    display_name = "Randomize Music"

class TrapFillPercentage(Range):
    """
    Replace a percentage of junk items in the item pool with random traps
    """
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0

class BaseTrapWeight(Choice):
    """
    Base Class for Trap Weights
    """
    option_none = 0
    option_low = 1
    option_medium = 2
    option_high = 4
    default = 2

class TrapExpirationTime(Range):
    """
    The amount of time (in minutes) that it takes for traps to wear off.
    """
    display_name = "Trap Expiration Time"
    range_start = 1
    range_end = 10
    default = 2

class SlowTrapWeight(BaseTrapWeight):
    """
    Likelihood of receiving a trap which slows down the game speed.
    """
    display_name = "Slow Trap Weight"

class FastTrapWeight(BaseTrapWeight):
    """
    Likelihood of receiving a trap which speeds up the game speed.
    """
    display_name = "Fast Trap Weight"

class ReverseTrapWeight(BaseTrapWeight):
    """
    Likelihood of receiving a trap which reverses the controls.
    """
    display_name = "Reverse Trap Weight"

class IceTrapWeight(BaseTrapWeight):
    """
    Likelihood of receiving a trap which makes the ground slippery.
    """
    display_name = "Ice Trap Weight"

class LiteratureTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which causes the player to read literature.
    """
    display_name = "Literature Trap Weight"

class BounceTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which greatly increases wall bounce.
    """
    display_name = "Bounce Trap Weight"

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
    include_tidepool : IncludeTidepool
    true_ending : TrueEnding
    jump_type_spawning : JumpTypeSpawning
    tokens_per_house : TokensPerHouse
    extra_tokens_per_level : ExtraTokensPerLevel

    #sanity options
    statue_sanity_level: StatueSanityLevel
    teleport_sanity_level: TeleportSanityLevel
    fetch_sanity_level: FetchSanityLevel
    checkpoint_sanity: CheckpointSanity

    #randomization options
    level_randomization: LevelRandomization
    max_variety_on_high: MaxVarietyOnHigh
    gratitude_distribution: GratitudeDistribution
    randomize_level_locations: RandomizeLevelLocations
    randomize_music: RandomizeMusic

    #traps
    trap_fill_percentage: TrapFillPercentage
    trap_expiration_time: TrapExpirationTime
    slow_trap_weight: SlowTrapWeight
    fast_trap_weight: FastTrapWeight
    reverse_trap_weight: ReverseTrapWeight
    ice_trap_weight: IceTrapWeight
    literature_trap_weight: LiteratureTrapWeight
    bounce_trap_weight: BounceTrapWeight

option_groups = [
    OptionGroup("General Options", [
        TotalGratitudes,
        GratitudesRequiredPercentage,
        SkipTutorials,
        IncludeFiveStars,
        IncludeTidepool,
        TrueEnding,
        JumpTypeSpawning,
        TokensPerHouse,
        ExtraTokensPerLevel
    ]),
    OptionGroup("Sanity Options", [
        StatueSanityLevel,
        TeleportSanityLevel,
        FetchSanityLevel,
        CheckpointSanity
    ]),
    OptionGroup("Randomization Options", [
        LevelRandomization,
        MaxVarietyOnHigh,
        GratitudeDistribution,
        RandomizeLevelLocations,
        RandomizeMusic
    ]),
    OptionGroup("Trap Options", [
        TrapFillPercentage,
        TrapExpirationTime,
        SlowTrapWeight,
        FastTrapWeight,
        ReverseTrapWeight,
        IceTrapWeight,
        LiteratureTrapWeight,
        BounceTrapWeight
    ])
]

# TODO: option presets
# - vanilla, standard, odd, chaotic