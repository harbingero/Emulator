class Pokemon:

    def __init__(self, name, number, type1, level_moves, evolutions, tm, type2=None):
        self.name = name
        self.number = number
        self.type1 = type1
        self.type2 = type2
        self.level_moves = level_moves
        self.evolutions = evolutions
        self.tm = tm


lmoves_bulbasaur = {1: ["Tackle", "Growl"],
                    7: ["Leech Seed"],
                    13: ["Vine Whip"],
                    20: ["Poisonpowder"],
                    27: ["Razor Leaf"],
                    34: ["Growth"],
                    41: ["Sleep Powder"],
                    48: ["Solarbeam"]}
tmoves_bulbasaur = ["Swords Dance",
                    "Toxic",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "Rage",
                    "Mega Drain",
                    "Solarbeam",
                    "Mimic",
                    "Double Team",
                    "Reflect",
                    "Bide",
                    "Rest",
                    "Substitute"]
hmoves_bulbasaur = ["Cut"]
lmoves_ivysaur = {1: ["Tackle", "Growl", "Leech Seed"],
                  7: ["Leech Seed"],
                  13: ["Vine Whip"],
                  22: ["Poisonpowder"],
                  30: ["Razor Leaf"],
                  38: ["Growth"],
                  46: ["Sleep Powder"],
                  54: ["Solarbeam"]}
tmoves_ivysaur = ["Swords Dance",
                  "Toxic",
                  "Body Slam",
                  "Take Down",
                  "Double-Edge",
                  "Rage",
                  "Mega Drain",
                  "Solarbeam",
                  "Mimic",
                  "Double Team",
                  "Reflect",
                  "Bide",
                  "Rest",
                  "Substitute"]
hmoves_ivysaur = ["Cut"]
lmoves_venusaur = {1: ["Tackle", "Growl", "Leech Seed", "Vine Whip"],
                   7: ["Leech Seed"],
                   13: ["Vine Whip"],
                   22: ["Poisonpowder"],
                   30: ["Razor Leaf"],
                   43: ["Growth"],
                   55: ["Sleep Powder"],
                   65: ["Solarbeam"]}
tmoves_venusaur = ["Swords Dance",
                   "Toxic",
                   "Body Slam",
                   "Take Down",
                   "Double-Edge",
                   "Hyper Beam",
                   "Rage",
                   "Mega Drain",
                   "Solarbeam",
                   "Mimic",
                   "Double Team",
                   "Reflect",
                   "Bide",
                   "Rest",
                   "Substitute"]
hmoves_venusaur = ["Cut"]
lmoves_charmander = {1: ["Scratch", "Growl"],
                     9: ["Ember"],
                     15: ["Leer"],
                     22: ["Rage"],
                     30: ["Slash"],
                     38: ["Flamethrower"],
                     46: ["Fire Spin"]}
tmoves_charmander = ["Mega Punch",
                     "Swords Dance",
                     "Mega Kick",
                     "Toxic",
                     "Body Slam",
                     "Take Down",
                     "Double-Edge",
                     "Submission",
                     "Counter",
                     "Seismic Toss",
                     "Rage",
                     "Dragon Rage",
                     "Dig",
                     "Mimic",
                     "Double Team",
                     "Reflect",
                     "Bide",
                     "Fire Blast",
                     "Swift",
                     "Skull Bash",
                     "Rest",
                     "Substitute"]
hmoves_charmander = ["Cut",
                     "Strength"]
lmoves_charmeleon = {1: ["Scratch", "Growl", "Ember"],
                     9: ["Ember"],
                     15: ["Leer"],
                     24: ["Rage"],
                     33: ["Slash"],
                     42: ["Flamethrower"],
                     56: ["Fire Spin"]}
tmoves_charmeleon = ["Mega Punch",
                     "Swords Dance",
                     "Mega Kick",
                     "Toxic",
                     "Body Slam",
                     "Take Down",
                     "Double-Edge",
                     "Submission",
                     "Counter",
                     "Seismic Toss",
                     "Rage",
                     "Dragon Rage",
                     "Dig",
                     "Mimic",
                     "Double Team",
                     "Reflect",
                     "Bide",
                     "Fire Blast",
                     "Swift",
                     "Skull Bash",
                     "Rest",
                     "Substitute"]
hmoves_charmeleon = ["Cut",
                     "Strength"]
lmoves_charizard = {1: ["Scratch", "Growl", "Ember", "Leer"],
                    9: ["Ember"],
                    15: ["Leer"],
                    24: ["Rage"],
                    36: ["Slash"],
                    46: ["Flamethrower"],
                    55: ["Fire Spin"]}
tmoves_charizard = ["Mega Punch",
                    "Swords Dance",
                    "Mega Kick",
                    "Toxic",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "Hyper Beam",
                    "Submission",
                    "Counter",
                    "Seismic Toss",
                    "Rage",
                    "Dragon Rage",
                    "Earthquake",
                    "Fissure",
                    "Dig",
                    "Mimic",
                    "Double Team",
                    "Reflect",
                    "Bide",
                    "Fire Blast",
                    "Swift",
                    "Skull Bash",
                    "Rest",
                    "Substitute"]
hmoves_charizard = ["Cut",
                    "Fly",
                    "Strength"]
lmoves_squirtle = {1: ["Tackle", "Tail Whip"],
                   8: ["Bubble"],
                   15: ["Water Gun"],
                   22: ["Bite"],
                   28: ["Withdraw"],
                   35: ["Skull Bash"],
                   42: ["Hydro Pump"]}
tmoves_squirtle = ["Mega Punch",
                   "Mega Kick",
                   "Toxic",
                   "Body Slam",
                   "Take Down",
                   "Double-Edge",
                   "Bubblebeam",
                   "Water Gun",
                   "Ice Beam",
                   "Blizzard",
                   "Submission",
                   "Counter",
                   "Seismic Toss",
                   "Rage",
                   "Dig",
                   "Mimic",
                   "Double Team",
                   "Reflect",
                   "Bide",
                   "Skull Bash",
                   "Rest",
                   "Substitue"]
hmoves_squirtle = ["Surf",
                   "Strength"]
lmoves_wartortle = {1: ["Tackle", "Tail Whip", "Bubble"],
                    8: ["Bubble"],
                    15: ["Water Gun"],
                    24: ["Bite"],
                    31: ["Withdraw"],
                    39: ["Skull Bash"],
                    47: ["Hydro Pump"]}
tmoves_wartortle = ["Mega Punch",
                    "Mega Kick",
                    "Toxic",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "Bubblebeam",
                    "Water Gun",
                    "Ice Beam",
                    "Blizzard",
                    "Submission",
                    "Counter",
                    "Seismic Toss",
                    "Rage",
                    "Dig",
                    "Mimic",
                    "Double Team",
                    "Reflect",
                    "Bide",
                    "Skull Bash",
                    "Rest",
                    "Substitute"]
hmoves_wartortle = ["Surf",
                    "Strength"]
lmoves_blastoise = {1: ["Tackle", "Tail Whip", "Bubble", "Water Gun"],
                    8: ["Bubble"],
                    15: ["Water Gun"],
                    24: ["Bite"],
                    31: ["Withdraw"],
                    42: ["Skull Bash"],
                    52: ["Hydro Pump"]}
tmoves_blastoise = ["Mega Punch",
                    "Mega Kick",
                    "Toxic",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "Bubblebeam",
                    "Water Gun",
                    "Ice Beam",
                    "Blizzard",
                    "Hyper Bean",
                    "Submission",
                    "Counter",
                    "Seismic Toss",
                    "Rage",
                    "Earthquake",
                    "Fissure",
                    "Dig",
                    "Mimic",
                    "Double Team",
                    "Reflect",
                    "Bide",
                    "Skull Bash",
                    "Rest",
                    "Substitute"]
hmoves_blastoise = ["Surf",
                    "Strength"]
lmoves_caterpie = {1: ["Tackle", "String Shot"]}
tmoves_caterpie = []
hmoves_caterpie = []
lmoves_metapod = {1: ["Harden"]}
tmoves_metapod = []
hmoves_metapod = []
lmoves_butterfree = {1: ["Confusion"],
                     12: ["Confusion"],
                     15: ["Poisonpowder"],
                     16: ["Stun Spore"],
                     17: ["Sleep Powder"],
                     21: ["Supersonic"],
                     26: ["Whirlwind"],
                     32: ["Psybeam"]}
tmoves_butterfree = ["Razor Wind",
                     "Whirlwind",
                     "Toxic",
                     "Take Down",
                     "Double-Edge",
                     "Hyper Beam",
                     "Rage",
                     "Mega Drain",
                     "Solarbeam",
                     "Psychic",
                     "Teleport",
                     "Mimic",
                     "Double Team",
                     "Reflect",
                     "Bide",
                     "Swift",
                     "Rest",
                     "Psywave",
                     "Substitute"]
hmoves_butterfree = ["Flash"]
lmoves_weedle = {1: ["Poison Sting", "String Shot"]}
tmoves_weedle = []
hmoves_weedle = []
lmoves_kakuna = {1: ["Harden"]}
tmoves_kakuna = []
hmoves_kakuna = []
lmoves_beedrill = {1: ["Fury Attack"],
                   12: ["Fury Attack"],
                   16: ["Focus Energy"],
                   20: ["Twineedle"],
                   25: ["Rage"],
                   30: ["Pin Missile"],
                   35: ["Agility"]}
tmoves_beedrill = ["Swords Dance",
                   "Toxic",
                   "Take Down",
                   "Double-Edge",
                   "Hyper Beam",
                   "Rage",
                   "Mega Drain",
                   "Mimic",
                   "Double Team",
                   "Reflect",
                   "Bide",
                   "Swift",
                   "Skull Bash",
                   "Rest",
                   "Substitute"]
hmoves_beedrill = ["Cut"]
lmoves_pidgey = {1: "Gust",
                 5: "Sand-Attack",
                 12: "Quick Attack",
                 19: "Whirlwind",
                 28: "Wing Attack",
                 36: "Agility",
                 44: "Mirror Move"}
tmoves_pidgey = ["Razor Wind",
                 "Whirlwind",
                 "Toxic",
                 "Take Down",
                 "Double-Edge",
                 "Rage",
                 "Mimic",
                 "Double Team",
                 "Reflect",
                 "Bide",
                 "Swift",
                 "Sky Attack",
                 "Rest",
                 "Substitute"]
hmoves_pidgey = ["Fly"]
lmoves_pidgeotto = {1: ["Gust", "Sand-Attack"],
                    5: ["Sand-Attack"],
                    12: ["Quick Attack"],
                    21: ["Whirlwind"],
                    31: ["Wing Attack"],
                    40: ["Agility"],
                    49: ["Mirror Move"]}
tmoves_pidgeotto = ["Razor Wind",
                    "Whirlwind",
                    "Toxic",
                    "Take Down",
                    "Double-Edge",
                    "Rage",
                    "Mimic",
                    "Double Team",
                    "Reflect",
                    "Bide",
                    "Swift",
                    "Sky Attack",
                    "Rest",
                    "Substitute"]
hmoves_pidgeotto = ["Fly"]
lmoves_ = {1: ["Gust", "Sand-Attack", "Quick Attack"],
           5: ["Sand-Attack"],
           12: ["Quick Attack"],
           21: ["Whirlwind"],
           31: ["Wing Attack"],
           44: ["Agility"],
           54: ["Mirror Move"]}
tmoves_ = ["Razor Wind",
           "Whirlwind",
           "Toxic",
           "Take Down",
           "Double-Edge",
           "Hyper Beam",
           "Rage",
           "Mimic",
           "Double Team",
           "Reflect",
           "Bide",
           "Swift",
           "Sky Attack",
           "Rest",
           "Substitute"]
hmoves_ = []
lmoves_ = {}
tmoves_ = []
hmoves_ = []

# https://bulbapedia.bulbagarden.net/wiki/Weedle_(Pok%C3%A9mon)/Generation_I_learnset#By_leveling_up

bulbasaur = Pokemon("Bulbasaur", 1, "Grass", lmoves_bulbasaur, {16: "Ivysaur", 32: "Venusaur"}, tmoves_bulbasaur,
                    "Poison")
ivysaur = Pokemon("Ivysaur", 2, "Grass", lmoves_ivysaur, {32: "Venusaur"}, tmoves_ivysaur, "Poison")
venusaur = Pokemon("Venusaur", 3, "Grass", lmoves_venusaur, {}, tmoves_venusaur, "Poison")
