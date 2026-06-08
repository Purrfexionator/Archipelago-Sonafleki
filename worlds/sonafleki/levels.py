from __future__ import annotations
from .Data import ItemNames

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import SonaflekiWorld

class LevelSegment:
    name: str
    num_checkpoints : int

    difficulty = 0
    jump_type = 0

    def __init__(self, name: str, num_checkpoints: int = 1):
        self.name = name
        self.num_checkpoints = num_checkpoints

class Level:
    name: str
    difficulty_min : int
    difficulty_max : int
    jump_types: list[int]
    segments : list[LevelSegment]

    num_segments = 0
    num_checkpoints = 0
    num_gratitudes = 0

    def __init__(self, name: str, difficulty : int, jump_types: list[int], segments: list[LevelSegment]):
        self.name = name
        self.difficulty_min = difficulty
        self.difficulty_max = difficulty
        self.num_gratitudes = difficulty + 1
        self.jump_types = jump_types
        self.segments = segments

        for segment in self.segments:
            self.num_segments += 1
            self.num_checkpoints += segment.num_checkpoints
            segment.jump_type = self.jump_types[0]
            segment.difficulty = difficulty

    def segment_list(self):
        final_list = []
        for segment in self.segments:
            final_list.append(segment.name)
        return final_list

    def get_mapping(self):
        return {
            "name" : self.name,
            "difficulty" : [self.difficulty_min, self.difficulty_max],
            "gratitudes" : self.num_gratitudes,
            "jump_types" : self.jump_types,
            "segments" : self.segment_list()
        }

class SonaflekiLevels:
    # double jump levels
    touring_optimist = Level("Touring Optimist", 2, [0], [
        LevelSegment("to1", 0),
        LevelSegment("to2"),
        LevelSegment("to3"),
        LevelSegment("to4"),
        LevelSegment("to5"),
        LevelSegment("to6"),
        LevelSegment("to7"),
        LevelSegment("to8"),
        LevelSegment("to9", 2)
    ])

    bamboo_catching_water = Level("Bamboo Catching Water", 2, [0], [
        LevelSegment("bcw1", 0),
        LevelSegment("bcw2", 2),
        LevelSegment("bcw3"),
        LevelSegment("bcw4", 3),
        LevelSegment("bcw5"),
        LevelSegment("bcw6"),
        LevelSegment("bcw7", 2),
        LevelSegment("bcw8"),
        LevelSegment("bcw9")
    ])

    screen_time = Level("Screen Time", 3, [0], [
        LevelSegment("st1", 0),
        LevelSegment("st2"),
        LevelSegment("st3"),
        LevelSegment("st4"),
        LevelSegment("st5"),
        LevelSegment("st6", 2),
        LevelSegment("st7"),
        LevelSegment("st8"),
        LevelSegment("st9")
    ])

    # flutter jump levels
    urban_sift = Level("Urban Sift", 2, [1], [
        LevelSegment("us1", 0),
        LevelSegment("us2"),
        LevelSegment("us3"),
        LevelSegment("us4"),
        LevelSegment("us5"),
        LevelSegment("us6"),
        LevelSegment("us7"),
        LevelSegment("us8"),
        LevelSegment("us9"),
        LevelSegment("us10")
    ])

    how_i_feel = Level("How I Feel", 3, [1], [
        LevelSegment("hif1", 0),
        LevelSegment("hif2"),
        LevelSegment("hif3"),
        LevelSegment("hif4", 2),
        LevelSegment("hif5"),
        LevelSegment("hif6"),
        LevelSegment("hif7"),
        LevelSegment("hif8"),
        LevelSegment("hif9")
    ])

    nanoseconds = Level("Nanoseconds", 4, [1], [
        LevelSegment("ns1", 0),
        LevelSegment("ns2"),
        LevelSegment("ns3"),
        LevelSegment("ns4"),
        LevelSegment("ns5"),
        LevelSegment("ns6"),
        LevelSegment("ns7"),
        LevelSegment("ns8"),
        LevelSegment("ns9")
    ])

    # quad jump levels
    bluebottles = Level("Bluebottles", 2, [2], [
        LevelSegment("bb1"),
        LevelSegment("bb2"),
        LevelSegment("bb3"),
        LevelSegment("bb4"),
        LevelSegment("bb5"),
        LevelSegment("bb6"),
        LevelSegment("bb7"),
        LevelSegment("bb8")
    ])

    art_museum = Level("Art Museum", 2, [2], [
        LevelSegment("am1", 0),
        LevelSegment("am2"),
        LevelSegment("am3"),
        LevelSegment("am4"),
        LevelSegment("am5"),
        LevelSegment("am6"),
        LevelSegment("am7"),
        LevelSegment("am8"),
        LevelSegment("am9"),
        LevelSegment("am10"),
        LevelSegment("am11")
    ])

    butterfly_knife = Level("Butterfly Knife", 5, [2], [
        LevelSegment("bk1", 0),
        LevelSegment("bk2"),
        LevelSegment("bk3"),
        LevelSegment("bk4"),
        LevelSegment("bk5"),
        LevelSegment("bk6"),
        LevelSegment("bk7")
    ])

    # invert jump
    bird_bath = Level("Bird Bath", 2, [3], [
        LevelSegment("bb1", 0),
        LevelSegment("bb2"),
        LevelSegment("bb3"),
        LevelSegment("bb4"),
        LevelSegment("bb5"),
        LevelSegment("bb6"),
        LevelSegment("bb7"),
        LevelSegment("bb8"),
        LevelSegment("bb9")
    ])

    pheromones = Level("Pheromones", 3, [3], [
        LevelSegment("ph1", 0),
        LevelSegment("ph2"),
        LevelSegment("ph3"),
        LevelSegment("ph4"),
        LevelSegment("ph5"),
        LevelSegment("ph6"),
        LevelSegment("ph7"),
        LevelSegment("ph8"),
        LevelSegment("ph9"),
        LevelSegment("ph10")
    ])

    ozone = Level("Ozone", 5, [3], [
        LevelSegment("oz1"),
        LevelSegment("oz2"),
        LevelSegment("oz3", 2),
        LevelSegment("oz4"),
        LevelSegment("oz5", 2),
        LevelSegment("oz6"),
        LevelSegment("oz7"),
        LevelSegment("oz8")
    ])

    # dip jump
    voices = Level("Voices", 2, [4], [
        LevelSegment("vc1", 0),
        LevelSegment("vc2"),
        LevelSegment("vc3"),
        LevelSegment("vc4"),
        LevelSegment("vc5"),
        LevelSegment("vc6"),
        LevelSegment("vc7", 2),
        LevelSegment("vc8"),
        LevelSegment("vc9")
    ])

    oil_slick = Level("Oil Slick", 3, [4], [
        LevelSegment("os1"),
        LevelSegment("os2"),
        LevelSegment("os3"),
        LevelSegment("os4"),
        LevelSegment("os5"),
        LevelSegment("os6"),
        LevelSegment("os7"),
        LevelSegment("os8"),
        LevelSegment("os9"),
        LevelSegment("os10")
    ])

    six_ft_pool_end = Level("6ft Pool End", 4, [4], [
        LevelSegment("6ft1", 0),
        LevelSegment("6ft2"),
        LevelSegment("6ft3"),
        LevelSegment("6ft4"),
        LevelSegment("6ft5"),
        LevelSegment("6ft6", 2),
        LevelSegment("6ft7"),
        LevelSegment("6ft8"),
        LevelSegment("6ft9")
    ])

    base_levels = [
        touring_optimist,
        bamboo_catching_water,
        screen_time,
        urban_sift,
        how_i_feel,
        nanoseconds,
        bluebottles,
        art_museum,
        bird_bath,
        pheromones,
        voices,
        oil_slick,
        six_ft_pool_end
    ]

    hard_levels = [
        butterfly_knife,
        ozone
    ]

    world : SonaflekiWorld

    def __init__(self, world : SonaflekiWorld):
        self.world = world

    def randomize(self, amount : int):
        all_levels = self.base_levels.copy()
        if self.world.options.include_five_stars:
            all_levels += self.hard_levels.copy()

        # per level randomization
        if amount == 1:
            for level in all_levels:
                # assemble pool (ignoring endpoints)
                pool = []
                for i in range(1, level.num_segments - 1):
                    pool.append(level.segments[i])

                # randomize pool
                self.world.random.shuffle(pool)

                # assign new midpoint segments from pool
                for i in range(1, level.num_segments - 1):
                    level.segments[i] = pool.pop()

        # matching jump types
        if amount >= 2:
            # initialize pools
            openers = [[], [], [], [], []]
            middles = [[], [], [], [], []]
            closers = [[], [], [], [], []]

            # populate pools
            for level in all_levels:
                jump_type = level.jump_types[0]
                openers[jump_type].append(level.segments[0])
                closers[jump_type].append(level.segments[-1])
                for i in range(1, level.num_segments - 1):
                    middles[jump_type].append(level.segments[i])

            # randomize pools
            for i in range(5):
                self.world.random.shuffle(openers[i])
                self.world.random.shuffle(middles[i])
                self.world.random.shuffle(closers[i])

            # assemble new levels
            for level in all_levels:
                jump_type = level.jump_types[0]
                level.segments[0] = openers[jump_type].pop()
                level.segments[-1] = closers[jump_type].pop()
                for i in range(1, level.num_segments - 1):
                    level.segments[i] = middles[jump_type].pop()

        # all levels (uses type 2 as a starting point)
        if amount == 3:
            max_variety = self.world.options.max_variety_on_high

            level_pool = all_levels.copy()
            shuffle_groups = []

            self.world.random.shuffle(level_pool)

            # create "shuffle groups" to ensure max_variety rules are respected and
            # every level is guaranteed access to the exact amount of segments it needs
            while not len(level_pool) == 0:
                if len(level_pool) >= max_variety:
                    shuffle_group = level_pool[:max_variety]
                    level_pool = level_pool[max_variety:]
                    shuffle_groups.append(shuffle_group)
                else:
                    shuffle_group = level_pool
                    level_pool = []
                    shuffle_groups.append(shuffle_group)

            for group in shuffle_groups:
                # initialize group pools
                openers = []
                middles = []
                closers = []

                # populate group pools
                for level in group:
                    openers.append(level.segments[0])
                    closers.append(level.segments[-1])
                    for i in range(1, level.num_segments - 1):
                        middles.append(level.segments[i])

                # randomize pools
                self.world.random.shuffle(openers)
                self.world.random.shuffle(middles)
                self.world.random.shuffle(closers)

                # shuffle levels in group
                for level in group:
                    level.segments[0] = openers.pop()
                    level.segments[-1] = closers.pop()
                    for i in range(1, level.num_segments - 1):
                        level.segments[i] = middles.pop()

        for level in all_levels:
            level.jump_types = []
            level.num_checkpoints = 0
            level.difficulty_min = level.segments[0].difficulty
            level.difficulty_max = level.difficulty_min
            for segment in level.segments:
                level.num_checkpoints += segment.num_checkpoints
                level.difficulty_min = min(level.difficulty_min, segment.difficulty)
                level.difficulty_max = max(level.difficulty_max, segment.difficulty)
                if segment.jump_type not in level.jump_types:
                    level.jump_types.append(segment.jump_type)

    def get_level_string(self):
        all_levels = self.base_levels.copy()
        if self.world.options.include_five_stars:
            all_levels += self.hard_levels.copy()

        string = ""
        for level in all_levels:
            string += "\n\n" + level.name + "\n"
            string += "Checkpoints: " + str(level.num_checkpoints) + " | "
            string += "Difficulty: " + str(level.difficulty_min) + " to " + str(level.difficulty_max) + " | "
            string += "Gratitudes: " + str(level.num_gratitudes) + " | "
            string += "Jump Types: " + ", ".join([ItemNames.jump_types[i] for i in level.jump_types]) + "\n"
            string += "Segments: " + ", ".join(level.segment_list())

        return string

    def get_mapping(self):
        mapping = {
            # double jump levels
            "touring_optimist" : self.touring_optimist.get_mapping(),
            "bamboo_catching_water" : self.bamboo_catching_water.get_mapping(),
            "screen_time" : self.screen_time.get_mapping(),

            # flutter jump levels
            "urban_sift" : self.urban_sift.get_mapping(),
            "how_i_feel" : self.how_i_feel.get_mapping(),
            "nanoseconds" : self.nanoseconds.get_mapping(),

            # quad jump levels
            "bluebottles" : self.bluebottles.get_mapping(),
            "art_museum" : self.art_museum.get_mapping(),

            # invert jump levels
            "bird_bath" : self.bird_bath.get_mapping(),
            "pheromones" : self.pheromones.get_mapping(),

            # dip jump levels
            "voices" : self.voices.get_mapping(),
            "oil_slick" : self.oil_slick.get_mapping(),
            "six_ft_pool_end" : self.six_ft_pool_end.get_mapping()
        }

        # hard levels
        if self.world.options.include_five_stars:
            mapping["butterfly_knife"] = self.butterfly_knife.get_mapping()
            mapping["ozone"] = self.ozone.get_mapping()

        return mapping