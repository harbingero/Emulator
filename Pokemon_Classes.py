class Pokemon:

    def __init__(self, name, number, type1, level_moves, evolutions, tm, type2=None):
        self.name = name
        self.number = number
        self.type1 = type1
        self.type2 = type2
        self.level_moves = level_moves
        self.evolutions = evolutions
        self.tm = tm


lmoves_bulbasaur = {'01': ['Tackle', 'Growl'],
                    '07': ['Leech Seed'],
                    '13': ['Vine Whip'],
                    '20': ['PoisonPowder'],
                    '27': ['Razor Leaf'],
                    '34': ['Growth'],
                    '41': ['Sleep Powder'],
                    '48': ['SolarBeam']}
tmoves_bulbasaur = ["Swords Dance",
                    "Toxic",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "Rage",
                    "Mega Drain",
                    "SolarBeam",
                    "Mimic",
                    "Double Team",
                    "Reflect",
                    "Bide",
                    "Rest",
                    "Substitute"]
hmoves_bulbasaur = ["Cut"]
lmoves_ivysaur = {'01': ['Tackle', 'Growl', 'Leech Seed'],
                  '07': ['Leech Seed'],
                  '13': ['Vine Whip'],
                  '22': ['PoisonPowder'],
                  '30': ['Razor Leaf'],
                  '38': ['Growth'],
                  '46': ['Sleep Powder'],
                  '54': ['SolarBeam']}
tmoves_ivysaur = ["Swords Dance",
                  "Toxic",
                  "Body Slam",
                  "Take Down",
                  "Double-Edge",
                  "Rage",
                  "Mega Drain",
                  "SolarBeam",
                  "Mimic",
                  "Double Team",
                  "Reflect",
                  "Bide",
                  "Rest",
                  "Substitute"]
hmoves_ivysaur = ["Cut"]
lmoves_venusaur = {'01': ['Tackle', 'Growl', 'Leech Seed', 'Vine Whip'],
                   '07': ['Leech Seed'],
                   '13': ['Vine Whip'],
                   '22': ['PoisonPowder'],
                   '30': ['Razor Leaf'],
                   '43': ['Growth'],
                   '55': ['Sleep Powder'],
                   '65': ['SolarBeam']}
tmoves_venusaur = ["Swords Dance",
                   "Toxic",
                   "Body Slam",
                   "Take Down",
                   "Double-Edge",
                   "Hyper Beam",
                   "Rage",
                   "Mega Drain",
                   "SolarBeam",
                   "Mimic",
                   "Double Team",
                   "Reflect",
                   "Bide",
                   "Rest",
                   "Substitute"]
hmoves_venusaur = ["Cut"]
lmove_charmander = {'01': ['Scratch', 'Growl'],
                    '09': ['Ember'],
                    '15': ['Leer'],
                    '22': ['Rage'],
                    '30': ['Slash'],
                    '38': ['Flamethrower'],
                    '46': ['Fire Spin']}
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
hmoves_charmander = ["Cut", "Strength"]
lmove_charmeleon = {'01': ['Scratch', 'Growl', 'Ember'],
                    '09': ['Ember'],
                    '15': ['Leer'],
                    '24': ['Rage'],
                    '33': ['Slash'],
                    '42': ['Flamethrower'],
                    '56': ['Fire Spin']}
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
hmoves_charmeleon = ["Cut", "Strength"]
lmoves_charizard = {'01': ['Scratch', 'Growl', 'Ember', 'Leer'],
                    '09': ['Ember'],
                    '15': ['Leer'],
                    '24': ['Rage'],
                    '36': ['Slash'],
                    '46': ['Flamethrower'],
                    '55': ['Fire Spin']}
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
hmoves_charizard = ["Cut", "Fly", "Strength"]
lmoves_squirtle = {'01': ['Tackle', 'Tail Whip'],
                   '08': ['Bubble'],
                   '15': ['Water Gun'],
                   '22': ['Bite'],
                   '28': ['Withdraw'],
                   '35': ['Skull Bash'],
                   '42': ['Hydro Pump']}
tmoves_squirtle = ["Mega Punch",
                   "Mega Kick",
                   "Toxic",
                   "Body Slam",
                   "Take Down",
                   "Double-Edge",
                   "BubbleBeam",
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
hmoves_squirtle = ["Surf", "Strength"]
lmoves_wartortle = {'01': ['Tackle', 'Tail Whip', 'Bubble'],
                    '08': ['Bubble'],
                    '15': ['Water Gun'],
                    '24': ['Bite'],
                    '31': ['Withdraw'],
                    '39': ['Skull Bash'],
                    '47': ['Hydro Pump']}
tmoves_wartortle = ["Mega Punch",
                    "Mega Kick",
                    "Toxic",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "BubbleBeam",
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
hmoves_wartortle = ["Surf", "Strength"]
lmoves_blastoise = {'01': ['Tackle', 'Tail Whip', 'Bubble', 'Water Gun'],
                    '08': ['Bubble'],
                    '15': ['Water Gun'],
                    '24': ['Bite'],
                    '31': ['Withdraw'],
                    '42': ['Skull Bash'],
                    '52': ['Hydro Pump']}
tmoves_blastoise = ["Mega Punch",
                    "Mega Kick",
                    "Toxic",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "BubbleBeam",
                    "Water Gun",
                    "Ice Beam",
                    "Blizzard",
                    "Hyper Beam",
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
hmoves_blastoise = ["Surf", "Strength"]
lmoves_caterpie = {'01': ['Tackle', 'String Shot']}
tmoves_caterpie = []
hmoves_caterpie = []
lmoves_metapod = {1: ["Harden"]}
tmoves_metapod = []
hmoves_metapod = []
lmoves_butterfree = {1: ["Confusion"],
                     12: ["Confusion"],
                     15: ["PoisonPowder"],
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
                     "SolarBeam",
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
lmoves_weedle = {'01': ['Poison Sting', 'String Shot'],
                 '9': ["Bug Bite"]}
tmoves_weedle = []
hmoves_weedle = []
lmoves_kakuna = {'01': ['Harden']}
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
                   "Toxid",
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
lmoves_pidgey = {'01': ['Gust'],
                 '05': ['Sand-Attack'],
                 '12': ['Quick Attack'],
                 '19': ['Whirlwind'],
                 '28': ['Wing Attack'],
                 '36': ['Agility'],
                 '44': ['Mirror Move']}
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
lmoves_pidgeotto = {'01': ['Gust', 'Sand-Attack'],
                    '05': ['Sand-Attack'],
                    '12': ['Quick Attack'],
                    '21': ['Whirlwind'],
                    '31': ['Wing Attack'],
                    '40': ['Agility'],
                    '49': ['Mirror Move']}
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
lmoves_pidgeot = {'01': ['Gust', 'Sand-Attack', 'Quick Attack'],
                  '05': ['Sand-Attack'],
                  '12': ['Quick Attack'],
                  '21': ['Whirlwind'],
                  '31': ['Wing Attack'],
                  '44': ['Agility'],
                  '54': ['Mirror Move']}
tmoves_pidgeot = ["Razor Wind",
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
hmoves_pidgeot = ["Fly"]
lmoves_rattata = {'01': ['Tackle', 'Tail Whip'],
                  '07': ['Quick Attack'],
                  '14': ['Hyper Fang'],
                  '23': ['Focus Energy'],
                  '34': ['Super Fang']}
tmoves_rattata = ["Toxic",
                  "Body Slam",
                  "Take Down",
                  "Double-Edge",
                  "BubbleBeam",
                  "Water Gun",
                  "Blizzard",
                  "Rage",
                  "Thunderbolt",
                  "Thunder",
                  "Dig",
                  "Mimic",
                  "Double Team",
                  "Bide",
                  "Swift",
                  "Skull Bash",
                  "Rest",
                  "Substitute"]
hmoves_rattata = []
lmoves_raticate = {'01': ['Tackle', 'Tail Whip', 'Quick Attack'],
                   '07': ['Quick Attack'],
                   '14': ['Hyper Fang'],
                   '27': ['Focus Energy'],
                   '41': ['Super Fang']}
tmoves_raticate = ["Toxic",
                   "Body Slam",
                   "Take Down",
                   "Double-Edge",
                   "BubbleBeam",
                   "Water Gun",
                   "Ice Beam",
                   "Blizzard",
                   "Hyper Beam",
                   "Rage",
                   "Thunderbolt",
                   "Thunder",
                   "Dig",
                   "Mimic",
                   "Double Team",
                   "Bide",
                   "Swift",
                   "Skull Bash",
                   "Rest",
                   "Substitute"]
hmoves_raticate = []
lmoves_spearow = {'01': ['Peck', 'Growl'],
                  '09': ['Leer'],
                  '15': ['Fury Attack'],
                  '22': ['Mirror Move'],
                  '29': ['Drill Peck'],
                  '36': ['Agility']}
tmoves_spearow = ["Razor Wind",
                  "Whirlwind",
                  "Toxic",
                  "Take Down",
                  "Double-Edge",
                  "Rage",
                  "Mimic",
                  "Double Team",
                  "Bide",
                  "Swift",
                  "Sky Attack",
                  "Rest",
                  "Substitute"]
hmoves_spearow = ["Fly"]
lmoves_fearow = {'01': ['Peck', 'Growl', 'Leer'],
                 '09': ['Leer'],
                 '15': ['Fury Attack'],
                 '25': ['Mirror Move'],
                 '34': ['Drill Peck'],
                 '43': ['Agility']}
tmoves_fearow = ["Razor Wind",
                 "Whirlwind",
                 "Toxic",
                 "Take Down",
                 "Double-Edge",
                 "Hyper Beam",
                 "Rage",
                 "Mimic",
                 "Double Team",
                 "Bide",
                 "Swift",
                 "Sky Attack",
                 "Rest",
                 "Substitute"]
hmoves_fearow = ["Fly"]
lmoves_ekans = {'01': ['Wrap', 'Leer'],
                '10': ['Poison Sting'],
                '17': ['Bite'],
                '24': ['Glare'],
                '31': ['Screech'],
                '38': ['Acid']}
tmoves_ekans = ["Toxic",
                "Body Slam",
                "Take Down",
                "Double-Edge",
                "Rage",
                "Mega Drain",
                "Earthquake",
                "Fissure",
                "Dig",
                "Mimic",
                "Double Team",
                "Bide",
                "Skull Bash",
                "Rest",
                "Rock Slide",
                "Substitute"]
hmoves_ekans = ["Strength"]
lmoves_arbok = {'01': ['Wrap', 'Leer', 'Poison Sting'],
                '10': ['Poison Sting'],
                '17': ['Bite'],
                '27': ['Glare'],
                '36': ['Screech'],
                '47': ['Acid']}
tmoves_arbok = ["Toxic",
                "Body Slam",
                "Take Down",
                "Double-Edge",
                "Hyper Beam",
                "Rage",
                "Mega Drain",
                "Earthquake",
                "Fissure",
                "Dig",
                "Mimic",
                "Double Team",
                "Bide",
                "Skull Bash",
                "Rest",
                "Rock Slide",
                "Substitute"]
hmoves_arbok = ["Strength"]
lmoves_pikachu = {1: ["ThunderShock", "Growl"],
                  9: ["Thunder Wave"],
                  16: ["Quick Attack"],
                  26: ["Swift"],
                  33: ["Agility"],
                  43: ["Thunder"]}
tmoves_pikachu = ["Mega Punch",
                  "Mega Kick",
                  "Toxic",
                  "Body Slam",
                  "Take Down",
                  "Double-Edge",
                  "Pay Day",
                  "Submission",
                  "Seismic Toss",
                  "Rage",
                  "Thunderbolt",
                  "Thunder",
                  "Mimic",
                  "Double Team",
                  "Reflect",
                  "Bide",
                  "Swift",
                  "Skull Bash",
                  "Rest",
                  "Thunder Wave",
                  "Substitute"]
hmoves_pikachu = ["Flash"]
lmoves_raichu = {1: ['ThunderShock', 'Growl', 'Thunder Wave']}
tmoves_raichu = ["Mega Punch",
                 "Mega Kick",
                 "Toxic",
                 "Body Slam",
                 "Take Down",
                 "Double-Edge",
                 "Hyper Beam",
                 "Pay Day",
                 "Submission",
                 "Seismic Toss",
                 "Rage",
                 "Thunderbolt",
                 "Thunder",
                 "Mimic",
                 "Double Team",
                 "Reflect",
                 "Bide",
                 "Swift",
                 "Skull Bash",
                 "Rest",
                 "Thunder Wave",
                 "Substitute"]
hmoves_raichu = ["Flash"]
lmoves_sandshrew = {1: ['Scratch'],
                    10: ['Sand-Attack'],
                    17: ['Slash'],
                    24: ['Poison Sting'],
                    31: ['Swift'],
                    38: ['Fury Swipes']}
tmoves_sandshrew = ["Swords Dance",
                    "Toxic",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "Submission",
                    "Seismic Toss",
                    "Rage",
                    "Earthquake",
                    "Fissure",
                    "Dig",
                    "Mimic",
                    "Double Team",
                    "Bide",
                    "Swift",
                    "Skull Bash",
                    "Rest",
                    "Rock Slide",
                    "Substitute"]
hmoves_sandshrew = ["Cut",
                    "Strength"]
lmoves_sandslash = {'01': ['Scratch', 'Sand-Attack'],
                    '10': ['Sand-Attack'],
                    '17': ['Slash'],
                    '27': ['Poison Sting'],
                    '36': ['Swift'],
                    '47': ['Fury Swipes']}
tmoves_sandslash = ["Swords Dance",
                    "Toxic",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "Hyper Beam",
                    "Submission",
                    "Seismic Toss",
                    "Rage",
                    "Earthquake",
                    "Fissure",
                    "Dig",
                    "Mimic",
                    "Double Team",
                    "Bide",
                    "Swift",
                    "Skull Bash",
                    "Rest",
                    "Rock Slide",
                    "Substitute"]
hmoves_sandslash = ["Cut",
                    "Strength"]
lmoves_nidoran_f = {1: ["Growl", "Tackle"],
                    8: ["Scratch"],
                    14: ["Poison Sting"],
                    21: ["Tail Whip"],
                    29: ["Bite"],
                    36: ["Fury Swipes"],
                    43: ["Double Kick"],}
tmoves_nidoran_f = ["Toxic",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "Blizzard",
                    "Rage",
                    "Thunderbolt",
                    "Thunder",
                    "Mimic",
                    "Double Team",
                    "Reflect",
                    "Bide",
                    "Skull Bash",
                    "Rest",
                    "Substitute"]
hmoves_nidoran_f = []
lmoves_nidorina = {1: ["Growl", "Tackle", "Scratch"],
                   8: ["Scratch"],
                   14: ["Poison Sting"],
                   23: ["Tail Whip"],
                   32: ["Bite"],
                   41: ["Fury Swipes"],
                   50: ["Double Kick"]}
tmoves_nidorina = ["Toxic",
                   "Horn Drill",
                   "Body Slam",
                   "Take Down",
                   "Double-Edge",
                   "BubbleBeam",
                   "Water Gun",
                   "Ice Beam",
                   "Blizzard",
                   "Rage",
                   "Thunderbolt",
                   "Thunder",
                   "Mimic",
                   "Double Team",
                   "Reflect",
                   "Bide",
                   "Skull Bash",
                   "Rest",
                   "Substitute"]
hmoves_nidorina = []
lmoves_nidoqueen = {1: ["Tackle", "Scracth", "Tail Whip", "Body Slam"],
                    8: ["Scratch"],
                    14: ["Poison Sting"],
                    23: ["Body Slam"]}
tmoves_nidoqueen = ["Mega Punch",
                    "Mega Kick",
                    "Toxic",
                    "Horn Drill",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "BubbleBeam",
                    "Water Gun",
                    "Ice Beam",
                    "Blizzard",
                    "Hyper Beam",
                    "Pay Day",
                    "Submission",
                    "Counter",
                    "Seismic Toss",
                    "Rage",
                    "Thunderbolt",
                    "Thunder",
                    "Earthquake",
                    "Fissure",
                    "Mimic",
                    "Double Team",
                    "Reflect",
                    "Bide",
                    "Fire Blast",
                    "Skull Bash",
                    "Rest",
                    "Rock Slide",
                    "Substitute"]
hmoves_nidoqueen = ["Surf",
                    "Strength"]
lmoves_nidoran_m = {1: ["Leer", "Tackle"],
                    8: ["Horn Attack"],
                    14: ["Poison Sting"],
                    21: ["Focus Energy"],
                    29: ["Fury Attack"],
                    36: ["Horn Drill"],
                    43: ["Double Kick"]}
tmoves_nidoran_m = ["Toxic",
                    "Horn Drill",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "Blizzard",
                    "Rage",
                    "Thunderbolt",
                    "Thunder",
                    "Mimic",
                    "Double Team",
                    "Reflect",
                    "Bide",
                    "Skull Bash",
                    "Rest",
                    "Substitute"]
hmoves_nidoran_m = []
lmoves_nidorino = {1: ["Leer", "Tackle", "Horn Attack"],
                   8: ["Horn Attack"],
                   14: ["Poison Sting"],
                   23: ["Focus Energy"],
                   32: ["Fury Attack"],
                   41: ["Horn Drill"],
                   50: ["Double Kick"]}
tmoves_nidorino = ["Toxic",
                   "Horn Drill",
                   "Body Slam",
                   "Take Down",
                   "Double-Edge",
                   "BubbleBeam",
                   "Water Gun",
                   "Ice Beam",
                   "Blizzard",
                   "Rage",
                   "Thunderbolt",
                   "Thunder",
                   "Mimic",
                   "Double Team",
                   "Reflect",
                   "Bide",
                   "Skull Bash",
                   "Rest",
                   "Substitute"]
hmoves_nidorino = []
lmoves_nidoking = {1: ["Tackle", "Horn Attack", "Poison Sting", "Thrash"],
                   8: ["Thrash"],
                   14: ["Poison Sting"],
                   23: ["Thrash"]}
tmoves_nidoking = ["Mega Punch",
                   "Mega Kick",
                   "Toxic",
                   "Horn Drill",
                   "Body Slam",
                   "Take Down",
                   "Double-Edge",
                   "BubbleBeam",
                   "Water Gun",
                   "Ice Beam",
                   "Blizzard",
                   "Hyper Beam",
                   "Pay Day",
                   "Submission",
                   "Counter",
                   "Seismic Toss",
                   "Rage",
                   "Thunderbolt",
                   "Thunder",
                   "Earthquake",
                   "Fissure",
                   "Mimic",
                   "Double Team",
                   "Reflect",
                   "Bide",
                   "Fire Blast",
                   "Skull Bash",
                   "Rest",
                   "Rock Slide",
                   "Substitute"]
hmoves_nidoking = ["Surf",
                   "Strength"]
lmoves_clefairy = {1: ["Pound", "Growl"],
                   13: ["Sing"],
                   18: ["DoubleSlap"],
                   24: ["Minimize"],
                   31: ["Metronome"],
                   39: ["Defense Curl"],
                   48: ["Light Screen"]}
tmoves_clefairy = ["Mega Punch",
                   "Mega Kick",
                   "Toxic",
                   "Body Slam",
                   "Take Down",
                   "Double-Edge",
                   "BubbleBeam",
                   "Water Gun",
                   "Ice Beam",
                   "Blizzard",
                   "Submission",
                   "Rage",
                   "SolarBeam",
                   "Thunderbolt",
                   "Thunder",
                   "Psychic",
                   "Teleport",
                   "Mimic",
                   "Double Team",
                   "Reflect",
                   "Bide",
                   "Metronome",
                   "Fire Blast",
                   "Skull Bash",
                   "Skull Bash",
                   "Rest",
                   "Thunder Wave",
                   "Psywave",
                   "Tri Attack",
                   "Substitute"]
hmoves_clefairy = ["Strength",
                   "Flash"]
lmoves_clefable = {1: ["Sing", "DoubleSlap", "Minimize", "Metronome"]}
tmoves_clefable = ["Mega Punch",
                   "Mega Kick",
                   "Toxic",
                   "Body Slam",
                   "Take Down",
                   "Double-Edge",
                   "BubbleBeam",
                   "Water Gun",
                   "Ice Beam",
                   "Blizzard",
                   "Hyper Beam",
                   "Submission",
                   "Counter",
                   "Seismic Toss",
                   "Rage",
                   "SolarBeam",
                   "Thunderbolt",
                   "Thunder",
                   "Psychic",
                   "Teleport",
                   "Mimic",
                   "Double Team",
                   "Reflect",
                   "Bide",
                   "Metronome",
                   "Fire Blast",
                   "Skull Bash",
                   "Rest",
                   "Thunder Wave",
                   "Psywave",
                   "Tri Attack",
                   "Substitute"]
hmoves_clefable = ["Strength",
                   "Flash"]
lmoves_vulpix = {'01': ['Ember', 'Tail Whip'],
                 '16': ['Quick Attack'],
                 '21': ['Roar'],
                 '28': ['Confuse Ray'],
                 '35': ['Flamethrower'],
                 '42': ['Fire Spin']}
tmoves_vulpix = ["Toxic",
                 "Body Slam",
                 "Take Down",
                 "Double-Edge",
                 "Rage",
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
hmoves_vulpix = []
lmoves_ninetales = {'01': ['Ember', 'Tail Whip', 'Quick Attack', 'Roar']}
tmoves_ninetales = ["Toxic",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "Hyper Beam",
                    "Rage",
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
hmoves_ninetales = []
lmoves_jigglypuff = {1: ["Sing"],
                     9: ["Pound"],
                     14: ["Disable"],
                     19: ["Defense Curl"],
                     24: ["DoubleSlap"],
                     29: ["Rest"],
                     34: ["Body Slam"],
                     39: ["Double-Edge"]}
tmoves_jigglypuff = ["Mega Punch",
                     "Mega Kick",
                     "Toxic",
                     "Body Slam",
                     "Take Down",
                     "Double-Edge",
                     "BubbleBeam",
                     "Water Gun",
                     "Ice Beam",
                     "Blizzard",
                     "Submission",
                     "Counter",
                     "Seismic Toss",
                     "Rage",
                     "SolarBeam",
                     "Thunderbolt",
                     "Thunder",
                     "Psychic",
                     "Teleport",
                     "Mimic",
                     "Double Team",
                     "Reflect",
                     "Bide",
                     "Fire Blast",
                     "Skull Bash",
                     "Rest",
                     "Thunder Wave",
                     "Psywave",
                     "Tri Attack",
                     "Substitute"]
hmoves_jigglypuff = ["Strength",
                     "Flash"]
lmoves_wigglytuff = {1: ["Sing", "Disable", "Defense Curl", "DoubleSlap"]}
tmoves_wigglytuff = ["Mega Punch",
                     "Mega Kick",
                     "Toxic",
                     "Body Slam",
                     "Take Down",
                     "Double-Edge",
                     "BubbleBeam",
                     "Water Gun",
                     "Ice Beam",
                     "Blizzard",
                     "Hyper Beam",
                     "Submission",
                     "Counter",
                     "Seismic Toss",
                     "Rage",
                     "SolarBeam",
                     "Thunderbolt",
                     "Thunder",
                     "Psychic",
                     "Teleport",
                     "Mimic",
                     "Double Team",
                     "Reflect",
                     "Bide",
                     "Fire Blast",
                     "Skull Bash",
                     "Rest",
                     "Thunder Wave",
                     "Psywave",
                     "Tri Attack",
                     "Substitute"]
hmoves_wigglytuff = ["Strength",
                     "Flash"]
lmoves_zubat = {'01': ['Leech Life'],
                '10': ['Supersonic'],
                '15': ['Bite'],
                '21': ['Confuse Ray'],
                '28': ['Wing Attack'],
                '36': ['Haze']}
tmoves_zubat = ["Razor Wind",
                "Whirlwind",
                "Toxic",
                "Take Down",
                "Double-Edge",
                "Rage",
                "Mega Drain",
                "Mimic",
                "Double Team",
                "Bide",
                "Swift",
                "Rest",
                "Substitute"]
hmoves_zubat = []
lmoves_golbat = {'01': ['Leech Life', 'Screech', 'Bite'],
                 '10': ['Supersonic'],
                 '15': ['Bite'],
                 '21': ['Confuse Ray'],
                 '32': ['Wing Attack'],
                 '43': ['Haze']}
tmoves_golbat = ["Razor Wind",
                 "Whirlwind",
                 "Toxic",
                 "Take Down",
                 "Double-Edge",
                 "Hyper Beam",
                 "Rage",
                 "Mega Drain",
                 "Mimic",
                 "Double Team",
                 "Bide",
                 "Swift",
                 "Rest",
                 "Substitute"]
hmoves_golbat = []
lmoves_oddish = {'01': ['Absorb'],
                 '15': ['PoisonPowder'],
                 '17': ['Stun Spore'],
                 '19': ['Sleep Powder'],
                 '24': ['Acid'],
                 '33': ['Petal Dance'],
                 '46': ['SolarBeam']}
tmoves_oddish = ["Swords Dance",
                 "Toxic",
                 "Take Down",
                 "Double-Edge",
                 "Rage",
                 "Mega Drain",
                 "SolarBeam",
                 "Mimic",
                 "Double Team",
                 "Reflect",
                 "Bide",
                 "Rest",
                 "Substitute"]
hmoves_oddish = ["Cut"]
lmoves_gloom = {'01': ['Absorb', 'PoisonPowder', 'Stun Spore'],
                '15': ['PoisonPowder'],
                '17': ['Stun Spore'],
                '19': ['Sleep Powder'],
                '28': ['Acid'],
                '38': ['Petal Dance'],
                '52': ['SolarBeam']}
tmoves_gloom = ["Swords Dance",
                "Toxic",
                "Take Down",
                "Double-Edge",
                "Rage",
                "Mega Drain",
                "SolarBeam",
                "Mimic",
                "Double Team",
                "Reflect",
                "Bide",
                "Rest",
                "Substitute"]
hmoves_gloom = ["Cut"]
lmoves_vileplume = {'01': ['Stun Spore', 'Sleep Powder', 'Acid', 'Petal Dance'],
                    '15': ['PoisonPowder'],
                    '17': ['Stun Spore'],
                    '19': ['Sleep Powder']}
tmoves_vileplume = ["Swords Dance",
                    "Toxic",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "Hyper Beam",
                    "Rage",
                    "Mega Drain",
                    "SolarBeam",
                    "Mimic",
                    "Double Team",
                    "Reflect",
                    "Bide",
                    "Rest",
                    "Substitute"]
hmoves_vileplume = ["Cut"]
lmoves_paras = {'01': ['Scratch'],
                '13': ['Stun Spore'],
                '20': ['Leech Life'],
                '27': ['Spore'],
                '34': ['Slash'],
                '41': ['Growth']}
tmoves_paras = ["Swords Dance",
                "Toxic",
                "Body Slam",
                "Take Down",
                "Double-Edge",
                "Rage",
                "Mega Drain",
                "SolarBeam",
                "Dig",
                "Mimic",
                "Double Team",
                "Reflect",
                "Bide",
                "Skull Bash",
                "Rest",
                "Substitute"]
hmoves_paras = ["Cut"]
lmoves_parasect = {'01': ['Scratch', 'Stun Spore', 'Leech Life'],
                   '13': ['Stun Spore'],
                   '20': ['Leech Life'],
                   '30': ['Spore'],
                   '39': ['Slash'],
                   '48': ['Growth']}
tmoves_parasect = ["Swords Dance",
                   "Toxic",
                   "Body Slam",
                   "Take Down",
                   "Double-Edge",
                   "Hyper Beam",
                   "Rage",
                   "Mega Drain",
                   "SolarBeam",
                   "Dig",
                   "Mimic",
                   "Double Team",
                   "Reflect",
                   "Bide",
                   "Skull Bash",
                   "Rest",
                   "Substitute"]
hmoves_parasect = ["Cut"]
lmoves_venonat = {1: ["Tackle", "Disable"],
                  24: ["PoisonPowder"],
                  27: ["Leech Life"],
                  30: ["Stun Spore"],
                  35: ["Psybeam"],
                  38: ["Sleep Powder"],
                  43: ["Psychic"]}
tmoves_venonat = ["Toxic",
                  "Take Down",
                  "Double-Edge",
                  "Rage",
                  "Mega Drain",
                  "SolarBeam",
                  "Psychic",
                  "Mimic",
                  "Double Team",
                  "Reflect",
                  "Bide",
                  "Rest",
                  "Psywave",
                  "Substitute"]
hmoves_venonat = ["Flash"]
lmoves_venomoth = {1: ["Tackle", "Disable", "PoisonPowder", "Leech Life"],
                   24: ["PoisonPowder"],
                   27: ["Leech Life"],
                   30: ["Stun Spore"],
                   38: ["Psybeam"],
                   43: ["Sleep Powder"],
                   50: ["Psychic"]}
tmoves_venomoth = ["Razor Wind",
                   "Whirlwind",
                   "Toxic",
                   "Take Down",
                   "Double-Edge",
                   "Hyper Beam",
                   "Rage",
                   "Mega Drain",
                   "SolarBeam",
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
hmoves_venomoth = ["Flash"]
lmoves_diglett = {'01': ['Scratch'],
                  '15': ['Growl'],
                  '19': ['Dig'],
                  '24': ['Sand-Attack'],
                  '31': ['Slash'],
                  '40': ['Earthquake']}
tmoves_diglett = ["Toxic",
                  "Body Slam",
                  "Take Down",
                  "Double-Edge",
                  "Rage",
                  "Earthquake",
                  "Fissure",
                  "Dig",
                  "Mimic",
                  "Double Team",
                  "Bide",
                  "Rest",
                  "Rock Slide",
                  "Substitute"]
hmoves_diglett = ["Cut"]
lmoves_dugtrio = {'01': ['Scratch', 'Growl', 'Dig'],
                  '15': ['Growl'],
                  '19': ['Dig'],
                  '24': ['Sand-Attack'],
                  '35': ['Slash'],
                  '47': ['Earthquake']}
tmoves_dugtrio = ["Toxic",
                  "Body Slam",
                  "Take Down",
                  "Double-Edge",
                  "Hyper Beam",
                  "Rage",
                  "Earthquake",
                  "Fissure",
                  "Dig",
                  "Mimic",
                  "Double Team",
                  "Bide",
                  "Rest",
                  "Rock Slide",
                  "Substitute"]
hmoves_dugtrio = ["Cut"]
lmoves_meowth = {'01': ['Scratch', 'Growl'],
                 '12': ['Bite'],
                 '17': ['Pay Day'],
                 '24': ['Screech'],
                 '33': ['Fury Swipes'],
                 '44': ['Slash']}
tmoves_meowth = ["Toxic",
                 "Body Slam",
                 "Take Down",
                 "Double-Edge",
                 "BubbleBeam",
                 "Water Gun",
                 "Pay Day",
                 "Rage",
                 "Thunderbolt",
                 "Thunder",
                 "Mimic",
                 "Double Team",
                 "Bide",
                 "Swift",
                 "Skull Bash",
                 "Rest",
                 "Substitute"]
hmoves_meowth = []
lmoves_persian = {'01': ['Scratch', 'Growl', 'Bite', 'Screech'],
                  '12': ['Bite'],
                  '17': ['Pay Day'],
                  '24': ['Screech'],
                  '37': ['Fury Swipes'],
                  '51': ['Slash']}
tmoves_persian = ["Toxic",
                  "Body Slam",
                  "Take Down",
                  "Double-Edge",
                  "BubbleBeam",
                  "Water Gun",
                  "Hyper Beam",
                  "Pay Day",
                  "Rage",
                  "Thunderbolt",
                  "Thunder",
                  "Mimic",
                  "Double Team",
                  "Bide",
                  "Swift",
                  "Skull Bash",
                  "Rest",
                  "Substitute"]
hmoves_persian = []
lmoves_psyduck = {'01': ['Scratch'],
                  '28': ['Tail Whip'],
                  '31': ['Disable'],
                  '36': ['Confusion'],
                  '43': ['Fury Swipes'],
                  '52': ['Hydro Pump']}
tmoves_psyduck = ["Mega Punch",
                  "Mega Kick",
                  "Toxic",
                  "Body Slam",
                  "Take Down",
                  "Double-Edge",
                  "BubbleBeam",
                  "Water Gun",
                  "Ice Beam",
                  "Blizzard",
                  "Pay Day",
                  "Submission",
                  "Counter",
                  "Seismic Toss",
                  "Rage",
                  "Dig",
                  "Mimic",
                  "Double Team",
                  "Bide",
                  "Swift",
                  "Skull Bash",
                  "Rest",
                  "Substitute"]
hmoves_psyduck = ["Surf",
                  "Strength"]
lmoves_golduck = {'01': ['Scratch', 'Tail Whip', 'Disable'],
                  '28': ['Tail Whip'],
                  '31': ['Disable'],
                  '39': ['Confusion'],
                  '48': ['Fury Swipes'],
                  '59': ['Hydro Pump']}
tmoves_golduck = ["Mega Punch",
                  "Mega Kick",
                  "Toxic",
                  "Body Slam",
                  "Take Down",
                  "Double-Edge",
                  "BubbleBeam",
                  "Water Gun",
                  "Ice Beam",
                  "Blizzard",
                  "Hyper Beam",
                  "Pay Day",
                  "Submission",
                  "Counter",
                  "Seismic Toss",
                  "Rage",
                  "Dig",
                  "Mimic",
                  "Double Team",
                  "Bide",
                  "Swift",
                  "Skull Bash",
                  "Rest",
                  "Substitute"]
hmoves_golduck = ["Surf",
                  "Strength"]
lmoves_mankey = {1: ["Scratch", "Leer"],
                 15: ["Karate Chop"],
                 21: ["Fury Swipes"],
                 27: ["Focus Energy"],
                 33: ["Seismic Toss"],
                 39: ["Thrash"]}
tmoves_mankey = ["Mega Punch",
                 "Mega Kick",
                 "Toxic",
                 "Body Slam",
                 "Take Down",
                 "Double-Edge",
                 "Pay Day",
                 "Submission",
                 "Counter",
                 "Seismic Toss",
                 "Rage",
                 "Thunderbolt",
                 "Thunder",
                 "Dig",
                 "Mimic",
                 "Double Team",
                 "Bide",
                 "Metronome",
                 "Swift",
                 "Skull Bash",
                 "Rest",
                 "Rock Slide",
                 "Substitute"]
hmoves_mankey = ["Strength"]
lmoves_primeape = {1: ["Scratch", "Leer", "Karate Chop", "Fury Swipes"],
                   15: ["Karate Chop"],
                   21: ["Fury Swipes"],
                   27: ["Focus Energy"],
                   37: ["Seismic Toss"],
                   46: ["Thrash"]}
tmoves_primeape = ["Mega Punch",
                   "Mega Kick",
                   "Toxic",
                   "Body Slam",
                   "Take Down",
                   "Double-Edge",
                   "Hyper Beam",
                   "Pay Day",
                   "Submission",
                   "Counter",
                   "Seismic Toss",
                   "Rage",
                   "Thunderbolt",
                   "Thunder",
                   "Dig",
                   "Mimic",
                   "Double Team",
                   "Bide",
                   "Metronome",
                   "Swift",
                   "Skull Bash",
                   "Rest",
                   "Rock Slide",
                   "Substitute"]
hmoves_primeape = ["Strength"]
lmoves_growlithe = {'01': ['Bite', 'Roar'],
                    '18': ['Ember'],
                    '23': ['Leer'],
                    '30': ['Take Down'],
                    '39': ['Agility'],
                    '50': ['Flamethrower']}
tmoves_growlithe = ["Toxic",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
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
hmoves_growlithe = []
lmoves_arcanine = {'01': ['Roar', 'Ember', 'Leer', 'Take Down']}
tmoves_arcanine = ["Toxic",
                   "Body Slam",
                   "Take Down",
                   "Double-Edge",
                   "Hyper Beam",
                   "Rage",
                   "Dragon Rage",
                   "Dig",
                   "Teleport",
                   "Mimic",
                   "Double Team",
                   "Reflect",
                   "Bide",
                   "Fire Blast",
                   "Swift",
                   "Skull Bash",
                   "Rest",
                   "Substitute"]
hmoves_arcanine = []
lmoves_poliwag = {1: ["Bubble"],
                  16: ["Hypnosis"],
                  19: ["Water Gun"],
                  25: ["DoubleSlap"],
                  31: ["Body Slam"],
                  38: ["Amnesia"],
                  45: ["Hydro Pump"]}
tmoves_poliwag = ["Toxic",
                  "Body Slam",
                  "Take Down",
                  "Double-Edge",
                  "BubbleBeam",
                  "Water Gun",
                  "Ice Beam",
                  "Blizzard",
                  "Rage",
                  "Psychic",
                  "Mimic",
                  "Double Team",
                  "Bide",
                  "Skull Bash",
                  "Rest",
                  "Psywave",
                  "Substitute"]
hmoves_ = ["Surf"]
lmoves_poliwhirl = {1: ["Bubble", "Hypnosis", "Water Gun"],
                    16: ["Hypnosis"],
                    19: ["Water Gun"],
                    26: ["DoubleSlap"],
                    33: ["Body Slam"],
                    41: ["Amnesia"],
                    49: ["Hydro Pump"]}
tmoves_poliwhirl = ["Mega Punch",
           "Mega Kick",
           "Toxic",
           "Body Slam",
           "Take Down",
           "Double-Edge",
           "BubbleBeam",
           "Water Gun",
           "Ice Beam",
           "Blizzard",
           "Submission",
           "Counter",
           "Seismic Toss",
           "Rage",
           "Earthquake",
           "Fissure",
           "Psychic",
           "Mimic",
           "Double Team",
           "Bide",
           "Metronome",
           "Skull Bash",
           "Rest",
           "Spywave",
           "Substitute"]
hmoves_poliwhirl = ["Surf",
           "Strength"]
lmoves_poliwrath = {1: ["Hypnosis", "Water Gun", "Double Slap", "Body Slam"],
                    16: ["Hypnosis"],
                    19: ["Water Gun"]}
tmoves_poliwrath = ["Mega Punch",
                    "Mega Kick",
                    "Toxic",
                    "Body Slam",
                    "Take Down",
                    "Double-Edge",
                    "BubbleBeam",
                    "Water Gun",
                    "Ice Beam",
                    "Blizzard",
                    "Hyper Beam",
                    "Submission",
                    "Counter",
                    "Seismic Toss",
                    "Rage",
                    "Earthquake",
                    "Fissure",
                    "Psychic",
                    "Mimic",
                    "Double Team",
                    "Bide",
                    "Metronome",
                    "Skull Bash",
                    "Rest",
                    "Psywave",
                    "Substitute"]
hmoves_poliwrath = ["Surf",
                    "Strength"]
lmoves_abra = {'01': ['Teleport']}
tmoves_abra = ["Mega Punch",
               "Mega Kick",
               "Toxic",
               "Body Slam",
               "Take Down",
               "Double-Edge",
               "Submission",
               "Counter",
               "Seismic Toss",
               "Rage",
               "Psychic",
               "Teleport",
               "Mimic",
               "Double Team",
               "Reflect",
               "Bide",
               "Metronome",
               "Skull Bash",
               "Rest",
               "Thunder Wave",
               "Psywave",
               "Tri Attack",
               "Substitute"]
hmoves_abra = ["Flash"]
lmoves_kadabra = {1: ["Teleport", "Confusion", "Disable"],
                  16: ["Confusion"],
                  20: ["Disable"],
                  27: ["Psybeam"],
                  31: ["Recover"],
                  38: ["Psychic"],
                  42: ["Reflect"]}
tmoves_kadabra = ["Mega Punch",
                  "Mega Kick",
                  "Toxic",
                  "Body Slam",
                  "Take Down",
                  "Double-Edge",
                  "Submission",
                  "Counter",
                  "Seismic Toss",
                  "Rage",
                  "Dig",
                  "Psychic",
                  "Teleport",
                  "Mimic",
                  "Double Team",
                  "Reflect",
                  "Bide",
                  "Metronome",
                  "Skull Bash",
                  "Rest",
                  "Thunder Wave",
                  "Psywave",
                  "Tri Attack",
                  "Substitute"]
hmoves_kadabra = ["Flash"]
lmoves_alakazam = {1: ["Teleport", "Confusion", "Disable"],
                   16: ["Confusion"],
                   20: ["Disable"],
                   27: ["Psywave"],
                   31: ["Recover"],
                   38: ["Psychic"],
                   42: ["Reflect"]}
tmoves_alakazam = ["Mega Punch",
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
                   "Dig",
                   "Psychic",
                   "Teleport",
                   "Mimic",
                   "Double Team",
                   "Reflect",
                   "Bide",
                   "Metronome",
                   "Skull Bash",
                   "Rest",
                   "Thunder Wave",
                   "Psywave",
                   "Tri Attack",
                   "Substitute"]
hmoves_alakazam = ["Flash"]
lmoves_machop = {'01': ['Karate Chop'],
                 '20': ['Low Kick'],
                 '25': ['Leer'],
                 '32': ['Focus Energy'],
                 '39': ['Seismic Toss'],
                 '46': ['Submission']}
tmoves_machop = ["Mega Punch",
                 "Mega Kick",
                 "Toxic",
                 "Body Slam",
                 "Take Down",
                 "Double-Edge",
                 "Submission",
                 "Counter",
                 "Seismic Toss",
                 "Rage",
                 "Earthquake",
                 "Fissure",
                 "Dig",
                 "Mimic",
                 "Double Team",
                 "Bide",
                 "Metronome",
                 "Fire Blast",
                 "Skull Bash",
                 "Rest",
                 "Rock Slide",
                 "Substitute"]
hmoves_machop = ["Strength"]
lmoves_machoke = {'01': ['Karate Chop', 'Low Kick', 'Leer'],
                  '20': ['Low Kick'],
                  '25': ['Leer'],
                  '36': ['Focus Energy'],
                  '44': ['Seismic Toss'],
                  '52': ['Submission']}
tmoves_machoke = ["Mega Punch",
                  "Mega Kick",
                  "Toxic",
                  "Body Slam",
                  "Take Down",
                  "Double-Edge",
                  "Submission",
                  "Counter",
                  "Seismic Toss",
                  "Rage",
                  "Earthquake",
                  "Fissure",
                  "Dig",
                  "Mimic",
                  "Double Team",
                  "Bide",
                  "Metronome",
                  "Fire Blast",
                  "Skull Bash",
                  "Rest",
                  "Rock Slide",
                  "Substitute"]
hmoves_machoke = ["Strength"]
lmoves_machamp = {'01': ['Karate Chop', 'Low Kick', 'Leer'],
                  '20': ['Low Kick'],
                  '25': ['Leer'],
                  '36': ['Focus Energy'],
                  '44': ['Seismic Toss'],
                  '52': ['Submission']}
tmoves_machamp = ["Mega Punch",
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
                  "Earthquake",
                  "Fissure",
                  "Dig",
                  "Mimic",
                  "Double Team",
                  "Bide",
                  "Metronome",
                  "Fire Blast",
                  "Skull Bash",
                  "Rest",
                  "Rock Slide",
                  "Substitute"]
hmoves_machamp = ["Strength"]
lmoves_bellsprout = {'01': ['Vine Whip', 'Growth'],
                     '13': ['Wrap'],
                     '15': ['PoisonPowder'],
                     '18': ['Sleep Powder'],
                     '21': ['Stun Spore'],
                     '26': ['Acid'],
                     '33': ['Razor Leaf'],
                     '42': ['Slam']}
tmoves_bellsprout = ["Swords Dance",
                     "Toxic",
                     "Take Down",
                     "Double-Edge",
                     "Rage",
                     "Mega Drain",
                     "SolarBeam",
                     "Mimic",
                     "Double Team",
                     "Reflect",
                     "Bide",
                     "Rest",
                     "Substitute"]
hmoves_bellsprout = ["Cut"]
lmoves_weepinbell = {'01': ['Vine Whip', 'Growth', 'Wrap'],
                     '13': ['Wrap'],
                     '15': ['PoisonPowder'],
                     '18': ['Sleep Powder'],
                     '23': ['Stun Spore'],
                     '29': ['Acid'],
                     '38': ['Razor Leaf'],
                     '49': ['Slam']}
tmoves_weepinbell = ["Swords Dance",
                     "Toxic",
                     "Take Down",
                     "Double-Edge",
                     "Rage",
                     "Mega Drain",
                     "SolarBeam",
                     "Mimic",
                     "Double Team",
                     "Reflect",
                     "Bide",
                     "Rest",
                     "Substitute"]
hmoves_weepinbell = ["Cut"]
lmoves_victreebel = {'01': ['Sleep Powder', 'Stun Spore', 'Acid', 'Razor Leaf'],
                     '13': ['Wrap'],
                     '15': ['PoisonPowder'],
                     '18': ['Sleep Powder']}
tmoves_victreebel = ["Swords Dance",
                     "Toxic",
                     "Body Slam",
                     "Take Down",
                     "Double-Edge",
                     "Hyper Beam",
                     "Rage",
                     "Mega Drain",
                     "SolarBeam",
                     "Mimic",
                     "Double Team",
                     "Reflect",
                     "Bide",
                     "Rest",
                     "Substitute"]
hmoves_victreebel = ["Cut"]
lmoves_tentacool = {'01': ['Acid'],
                    '07': ['Supersonic'],
                    '13': ['Wrap'],
                    '18': ['Poison Sting'],
                    '22': ['Water Gun'],
                    '27': ['Constrict'],
                    '33': ['Barrier'],
                    '40': ['Screech'],
                    '48': ['Hydro Pump']}
tmoves_tentacool = ["Swords Dance",
                    "Toxic",
                    "Take Down",
                    "Double-Edge",
                    "BubbleBeam",
                    "Water Gun",
                    "Ice Beam",
                    "Blizzard",
                    "Rage",
                    "Mega Drain",
                    "Mimic",
                    "Double Team",
                    "Reflect",
                    "Bide",
                    "Skull Bash",
                    "Rest",
                    "Substitute"]
hmoves_tentacool = ["Cut",
                    "Surf"]
lmoves_tentacruel = {'01': ['Acid', 'Supersonic', 'Wrap'],
                     '07': ['Supersonic'],
                     '13': ['Wrap'],
                     '18': ['Poison Sting'],
                     '22': ['Water Gun'],
                     '27': ['Constrict'],
                     '35': ['Barrier'],
                     '43': ['Screech'],
                     '50': ['Hydro Pump']}
tmoves_tentacruel = ["Swords Dance",
                     "Toxic",
                     "Take Down",
                     "Double-Edge",
                     "BubbleBeam",
                     "Water Gun",
                     "Ice Beam",
                     "Blizzard",
                     "Hyper Beam",
                     "Rage",
                     "Mega Drain",
                     "Mimic",
                     "Double Team",
                     "Reflect",
                     "Bide",
                     "Skull Bash",
                     "Rest",
                     "Substitute"]
hmoves_tentacruel = ["Cut",
                     "Surf"]
lmoves_geodude = {}
tmoves_geodude = []
hmoves_geodude = []
lmoves_graveler = {}
tmoves_graveler = []
hmoves_graveler = []
lmoves_golem = {}
tmoves_golem = []
hmoves_golem = []
lmoves_ponyta = {'01': ['Ember'], '30': ['Tail Whip'], '32': ['Stomp'], '35': ['Growl'], '39': ['Fire Spin'], '43': ['Take Down'], '48': ['Agility']}
tmoves_ponyta = ["Toxic", "Horn Drill", "Body Slam", "Take Down", "Double-Edge", "Rage", "Mimic", "Double Team", "Reflect", "Bide", "Fire Blast", "Swift", "Skull Bash", "Rest", "Substitute"]
hmoves_ponyta = []
lmoves_rapidash = {'01': ['Ember', 'Tail Whip', 'Stomp', 'Growl'], '30': ['Tail Whip'], '32': ['Stomp'], '35': ['Growl'], '39': ['Fire Spin'], '47': ['Take Down'], '55': ['Agility']}
tmoves_rapidash = ["Toxic", "Horn Drill", "Body Slam", "Take Down", "Double-Edge", "Hyper Beam", "Rage", "Mimic", "Double Team", "Reflect", "Bide", "Fire Blast", "Swift", "Skull Bash", "Rest", "Substitute"]
hmoves_rapidash = []



lmoves_magnemite = {'01': ['Tackle'], '21': ['SonicBoom'], '25': ['ThunderShock'], '29': ['Supersonic'], '35': ['Thunder Wave'], '41': ['Swift'], '47': ['Screech']}
tmoves_magnemite = ["Toxic", "Take Down", "Double-Edge", "Rage", "Thunderbolt", "Thunder", "Teleport", "Mimic", "Double Team", "Reflect", "Bide", "Swift", "Rest", "Thunder Wave", "Substitute"]
hmoves_magnemite = ["Flash"]
lmoves_magneton = {'01': ['Tackle', 'SonicBoom', 'ThunderShock'], '21': ['SonicBoom'], '25': ['ThunderShock'], '29': ['Supersonic'], '38': ['Thunder Wave'], '46': ['Swift'], '54': ['Screech']}
tmoves_magneton = ["Toxic", "Take Down", "Double-Edge", "Hyper Beam", "Rage", "Thunderbolt", "Thunder", "Teleport", "Mimic", "Double Team", "Reflect", "Bide", "Swift", "Rest", "Thunder Wave", "Substitute"]
hmoves_magneton = ["Flash"]
lmoves_farfetchd = {'01': ['Peck', 'Sand-Attack'], '07': ['Leer'], '15': ['Fury Attack'], '23': ['Swords Dance'], '31': ['Agility'], '39': ['Slash']}
tmoves_farfetchd = ["Razor Wind", "Swords Dance", "Whirlwind", "Toxic", "Body Slam", "Take Down", "Double-Edge", "Rage", "Mimic", "Double Team", "Reflect", "Bide", "Swift", "Skull Bash", "Rest", "Substitute"]
hmoves_farfetchd = ["Cut", "Fly"]
lmoves_doduo = {'01': ['Peck'], '20': ['Growl'], '24': ['Fury Attack'], '30': ['Drill Peck'], '36': ['Rage'], '40': ['Tri Attack'], '44': ['Agility']}
tmoves_doduo = ["Whirlwind", "Toxic", "Body Slam", "Take Down", "Double-Edge", "Rage", "Mimic", "Double Team", "Reflect", "Bide", "Skull Bash", "Sky Attack", "Rest", "Tri Attack", "Substitute"]
hmoves_doduo = ["Fly"]
lmoves_dodrio = {'01': ['Peck', 'Growl', 'Fury Attack'], '20': ['Growl'], '24': ['Fury Attack'], '30': ['Drill Peck'], '39': ['Rage'], '45': ['Tri Attack'], '51': ['Agility']}
tmoves_dodrio = ["Whirlwind", "Toxic", "Body Slam", "Take Down", "Double-Edge", "Hyper Beam", "Rage", "Mimic", "Double Team", "Reflect", "Bide", "Skull Bash", "Sky Attack", "Rest", "Tri Attack", "Substitute"]
hmoves_dodrio = ["Fly"]
lmoves_seel = {'01': ['Headbutt'], '30': ['Growl'], '35': ['Aurora Beam'], '40': ['Rest'], '45': ['Take Down'], '50': ['Ice Beam']}
tmoves_seel = ["Toxic", "Horn Drill", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Pay Day", "Rage", "Mimic", "Double Team", "Bide", "Skull Bash", "Rest", "Substitute"]
hmoves_seel = ["Surf", "Strength"]
lmoves_dewgong = {'01': ['Headbutt', 'Growl', 'Aurora Beam'], '30': ['Growl'], '35': ['Aurora Beam'], '44': ['Rest'], '50': ['Take Down'], '56': ['Ice Beam']}
tmoves_dewgong = ["Toxic", "Horn Drill", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Pay Day", "Rage", "Mimic", "Double Team", "Bide", "Skull Bash", "Rest", "Substitute"]
hmoves_dewgong = ["Surf", "Strength"]
lmoves_grimer = {'01': ['Pound', 'Disable'], '30': ['Poison Gas'], '33': ['Minimize'], '37': ['Sludge'], '42': ['Harden'], '48': ['Screech'], '55': ['Acid Armor']}
tmoves_grimer = ["Toxic", "Body Slam", "Rage", "Mega Drain", "Thunderbolt", "Thunder", "Mimic", "Double Team", "Bide", "Selfdestruct", "Fire Blast", "Rest", "Explosion", "Substitute"]
hmoves_grimer = []
lmoves_muk = {'01': ['Pound', 'Disable', 'Poison Gas'], '30': ['Poison Gas'], '33': ['Minimize'], '37': ['Sludge'], '45': ['Harden'], '53': ['Screech'], '60': ['Acid Armor']}
tmoves_muk = ["Toxic", "Body Slam", "Hyper Beam", "Rage", "Mega Drain", "Thunderbolt", "Thunder", "Mimic", "Double Team", "Bide", "Selfdestruct", "Fire Blast", "Rest", "Explosion", "Substitute"]
hmoves_muk = []
lmoves_shellder = {'01': ['Tackle', 'Withdraw'], '18': ['Supersonic'], '23': ['Clamp'], '30': ['Aurora Beam'], '39': ['Leer'], '50': ['Ice Beam']}
tmoves_shellder = ["Toxic", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Rage", "Teleport", "Mimic", "Double Team", "Reflect", "Bide", "Selfdestruct", "Swift", "Rest", "Explosion", "Tri Attack", "Substitute"]
hmoves_shellder = ["Surf"]
lmoves_cloyster = {'01': ['Withdraw', 'Supersonic', 'Clamp', 'Aurora Beam'], '50': ['Spike Cannon']}
tmoves_cloyster = ["Toxic", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Rage", "Teleport", "Mimic", "Double Team", "Reflect", "Bide", "Selfdestruct", "Swift", "Rest", "Explosion", "Tri Attack", "Substitute", "Leer", "Tackle"]
hmoves_cloyster = ["Surf"]
lmoves_gastly = {'01': ['Lick', 'Confuse Ray', 'Night Shade'], '27': ['Hypnosis'], '35': ['Dream Eater']}
tmoves_gastly = ["Toxic", "Rage", "Mega Drain", "Thunderbolt", "Thunder", "Mimic", "Double Team", "Bide", "Selfdestruct", "Dream Eater", "Rest", "Psywave", "Explosion", "Substitute"]
hmoves_gastly = []
lmoves_haunter = {'01': ['Lick', 'Confuse Ray', 'Night Shade'], '29': ['Hypnosis'], '38': ['Dream Eater']}
tmoves_haunter = ["Toxic", "Rage", "Mega Drain", "Thunderbolt", "Thunder", "Mimic", "Double Team", "Bide", "Selfdestruct", "Dream Eater", "Rest", "Psywave", "Explosion", "Substitute"]
hmoves_haunter = []
lmoves_gengar = {'01': ['Lick', 'Confuse Ray', 'Night Shade'], '29': ['Hypnosis'], '38': ['Dream Eater']}
tmoves_gengar = ["Mega Punch", "Mega Kick", "Toxic", "Body Slam", "Take Down", "Double-Edge", "Hyper Beam", "Submission", "Counter", "Seismic Toss", "Rage", "Mega Drain", "Thunderbolt", "Thunder", "Mimic", "Double Team", "Bide", "Metronome", "Selfdestruct", "Skull Bash", "Dream Eater", "Rest", "Psywave", "Explosion", "Substitute"]
hmoves_gengar = ["Strength"]
lmoves_onix = {'01': ['Tackle', 'Screech'], '15': ['Bind'], '19': ['Rock Throw'], '25': ['Rage'], '33': ['Slam'], '43': ['Harden']}
tmoves_onix = ["Toxic", "Body Slam", "Take Down", "Double-Edge", "Rage", "Earthquake", "Fissure", "Dig", "Mimic", "Double Team", "Bide", "Selfdestruct", "Skull Bash", "Rest", "Explosion", "Rock Slide", "Substitute"]
hmoves_onix = ["Strength"]




lmoves_voltorb = {'01': ['Tackle', 'Screech'], '17': ['SonicBoom'], '22': ['Selfdestruct'], '29': ['Light Screen'], '36': ['Swift'], '43': ['Explosion']}
tmoves_voltorb = ["Toxic", "Take Down", "Rage", "Thunderbolt", "Thunder", "Teleport", "Mimic", "Double Team", "Reflect", "Bide", "Selfdestruct", "Swift", "Rest", "Thunder Wave", "Explosion", "Substitute"]
hmoves_voltorb = ["Flash"]
lmoves_electrode = {'01': ['Tackle', 'Screech', 'SonicBoom'], '17': ['SonicBoom'], '22': ['Selfdestruct'], '29': ['Light Screen'], '40': ['Swift'], '50': ['Explosion']}
tmoves_electrode = ["Toxic", "Take Down", "Hyper Beam", "Rage", "Thunderbolt", "Thunder", "Teleport", "Mimic", "Double Team", "Reflect", "Bide", "Selfdestruct", "Swift", "Skull Bash", "Rest", "Thunder Wave", "Explosion", "Substitute"]
hmoves_electrode = ["Flash"]
lmoves_exeggcute = {'01': ['Barrage', 'Hypnosis'], '25': ['Reflect'], '28': ['Leech Seed'], '32': ['Stun Spore'], '37': ['PoisonPowder'], '42': ['SolarBeam'], '48': ['Sleep Powder']}
tmoves_exeggcute = ["Toxic", "Take Down", "Double-Edge", "Rage", "Teleport", "Mimic", "Double Team", "Reflect", "Bide", "Selfdestruct", "Egg Bomb", "Rest", "Psywave", "Explosion", "Substitute"]
hmoves_exeggcute = []
lmoves_exeggutor = {'01': ['Barrage', 'Hypnosis'], '28': ['Stomp']}
tmoves_exeggutor = ["Toxic", "Take Down", "Double-Edge", "Hyper Beam", "Rage", "Mega Drain", "SolarBeam", "Teleport", "Mimic", "Double Team", "Reflect", "Bide", "Selfdestruct", "Egg Bomb", "Rest", "Psywave", "Explosion", "Substitute", "Leech Seed", "PoisonPowder", "Sleep Powder", "Stun Spore"]
hmoves_exeggutor = ["Strength"]
lmoves_cubone = {}
tmoves_cubone = ["Mega Punch", "Mega Kick", "Toxic", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Submission", "Counter", "Seismic Toss", "Rage", "Earthquake", "Fissure", "Dig", "Mimic", "Double Team", "Bide", "Fire Blast", "Skull Bash", "Rest", "Substitute"]
hmoves_cubone = ["Strength"]
lmoves_marowak = {}
tmoves_marowak = ["Mega Punch", "Mega Kick", "Toxic", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Submission", "Counter", "Seismic Toss", "Rage", "Earthquake", "Fissure", "Dig", "Mimic", "Double Team", "Bide", "Fire Blast", "Skull Bash", "Rest", "Substitute", "Growl"]
hmoves_marowak = ["Strength"]
lmoves_hitmonlee = {'01': ['Double Kick', 'Meditate'], '33': ['Rolling Kick'], '38': ['Jump Kick'], '43': ['Focus Energy'], '48': ['Hi Jump Kick'], '53': ['Mega Kick']}
tmoves_hitmonlee = ["Mega Punch", "Mega Kick", "Toxic", "Body Slam", "Take Down", "Double-Edge", "Submission", "Counter", "Seismic Toss", "Rage", "Mimic", "Double Team", "Bide", "Metronome", "Swift", "Skull Bash", "Rest", "Substitute"]
hmoves_hitmonlee = ["Strength"]




lmoves_koffing = {'01': ['Tackle', 'Smog'], '32': ['Sludge'], '37': ['SmokeScreen'], '40': ['Selfdestruct'], '45': ['Haze'], '48': ['Explosion']}
tmoves_koffing = ["Toxic", "Rage", "Thunderbolt", "Thunder", "Mimic", "Double Team", "Bide", "Selfdestruct", "Fire Blast", "Rest", "Explosion", "Substitute"]
hmoves_koffing = []
lmoves_weezing = {'01': ['Tackle', 'Smog', 'Sludge'], '32': ['Sludge'], '39': ['SmokeScreen'], '43': ['Selfdestruct'], '49': ['Haze'], '53': ['Explosion']}
tmoves_weezing = ["Toxic", "Hyper Beam", "Rage", "Thunderbolt", "Thunder", "Mimic", "Double Team", "Bide", "Selfdestruct", "Fire Blast", "Rest", "Explosion", "Substitute"]
hmoves_weezing = []
lmoves_rhyhorn = {'01': ['Horn Attack'], '30': ['Stomp'], '35': ['Tail Whip'], '40': ['Fury Attack'], '45': ['Horn Drill'], '50': ['Leer'], '55': ['Take Down']}
tmoves_rhyhorn = ["Toxic", "Horn Drill", "Body Slam", "Take Down", "Double-Edge", "Rage", "Thunderbolt", "Thunder", "Earthquake", "Fissure", "Dig", "Mimic", "Double Team", "Bide", "Fire Blast", "Skull Bash", "Rest", "Rock Slide", "Substitute"]
hmoves_rhyhorn = ["Strength"]
lmoves_rhydon = {'01': ['Horn Attack', 'Stomp', 'Tail Whip', 'Fury Attack'], '30': ['Stomp'], '35': ['Tail Whip'], '40': ['Fury Attack'], '48': ['Horn Drill'], '55': ['Leer'], '64': ['Take Down']}
tmoves_rhydon = ["Mega Punch", "Mega Kick", "Toxic", "Horn Drill", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Pay Day", "Submission", "Counter", "Seismic Toss", "Rage", "Thunderbolt", "Thunder", "Earthquake", "Fissure", "Dig", "Mimic", "Double Team", "Bide", "Fire Blast", "Skull Bash", "Rest", "Rock Slide", "Substitute"]
hmoves_rhydon = ["Surf", "Strength"]
lmoves_chansey = {}
tmoves_chansey = ["Mega Punch", "Mega Kick", "Toxic", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Submission", "Counter", "Seismic Toss", "Rage", "SolarBeam", "Thunderbolt", "Thunder", "Teleport", "Mimic", "Double Team", "Reflect", "Bide", "Metronome", "Egg Bomb", "Fire Blast", "Skull Bash", "Softboiled", "Rest", "Thunder Wave", "Psywave", "Tri Attack", "Substitute"]
hmoves_chansey = ["Strength", "Flash"]
lmoves_tangela = {}
tmoves_tangela = ["Swords Dance", "Toxic", "Body Slam", "Take Down", "Double-Edge", "Hyper Beam", "Rage", "Mega Drain", "SolarBeam", "Mimic", "Double Team", "Bide", "Skull Bash", "Rest", "Substitute"]
hmoves_tangela = ["Cut"]
lmoves_kangaskhan = {'01': ['Comet Punch', 'Rage'], '26': ['Bite'], '31': ['Tail Whip'], '36': ['Mega Punch'], '41': ['Leer'], '46': ['Dizzy Punch']}
tmoves_kangaskhan = ["Mega Punch", "Mega Kick", "Toxic", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Submission", "Counter", "Seismic Toss", "Rage", "Thunderbolt", "Thunder", "Earthquake", "Fissure", "Mimic", "Double Team", "Bide", "Fire Blast", "Skull Bash", "Rest", "Rock Slide", "Substitute"]
hmoves_kangaskhan = ["Surf", "Strength"]
lmoves_horsea = {'01': ['Bubble'], '19': ['SmokeScreen'], '24': ['Leer'], '30': ['Water Gun'], '37': ['Agility'], '45': ['Hydro Pump']}
tmoves_horsea = ["Toxic", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Rage", "Mimic", "Double Team", "Bide", "Swift", "Skull Bash", "Rest", "Substitute"]
hmoves_horsea = ["Surf"]
lmoves_seadra = {'01': ['Bubble', 'SmokeScreen'], '19': ['SmokeScreen'], '24': ['Leer'], '30': ['Water Gun'], '41': ['Agility'], '52': ['Hydro Pump']}
tmoves_seadra = ["Toxic", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Rage", "Mimic", "Double Team", "Bide", "Swift", "Skull Bash", "Rest", "Substitute"]
hmoves_seadra = ["Surf"]
lmoves_goldeen = {'01': ['Peck', 'Tail Whip'], '19': ['Supersonic'], '24': ['Horn Attack'], '30': ['Fury Attack'], '37': ['Waterfall'], '45': ['Horn Drill'], '54': ['Agility']}
tmoves_goldeen = ["Toxic", "Horn Drill", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Rage", "Mimic", "Double Team", "Bide", "Swift", "Skull Bash", "Rest", "Substitute"]
hmoves_goldeen = ["Surf"]
lmoves_seaking = {'01': ['Peck', 'Tail Whip', 'Supersonic'], '19': ['Supersonic'], '24': ['Horn Attack'], '30': ['Fury Attack'], '39': ['Waterfall'], '48': ['Horn Drill'], '54': ['Agility']}
tmoves_seaking = ["Toxic", "Horn Drill", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Rage", "Mimic", "Double Team", "Bide", "Swift", "Skull Bash", "Rest", "Substitute"]
hmoves_seaking = ["Surf"]
lmoves_staryu = {'01': ['Tackle'], '17': ['Water Gun'], '22': ['Harden'], '27': ['Recover'], '32': ['Swift'], '37': ['Minimize'], '42': ['Light Screen'], '47': ['Hydro Pump']}
tmoves_staryu = ["Toxic", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Rage", "Thunderbolt", "Thunder", "Teleport", "Mimic", "Double Team", "Reflect", "Bide", "Swift", "Skull Bash", "Rest", "Thunder Wave", "Psywave", "Tri Attack", "Substitute"]
hmoves_staryu = ["Surf", "Flash"]
lmoves_starmie = {'01': ['Tackle', 'Water Gun', 'Harden']}
tmoves_starmie = ["Toxic", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Rage", "Thunderbolt", "Thunder", "Teleport", "Mimic", "Double Team", "Reflect", "Bide", "Swift", "Skull Bash", "Rest", "Thunder Wave", "Psywave", "Tri Attack", "Substitute", "Hydro Pump", "Light Screen", "Minimize", "Recover"]
hmoves_starmie = ["Surf", "Flash"]




lmoves_scyther = {}
tmoves_scyther = ["Swords Dance", "Toxic", "Take Down", "Double-Edge", "Hyper Beam", "Rage", "Mimic", "Double Team", "Bide", "Swift", "Skull Bash", "Rest", "Substitute"]
hmoves_scyther = ["Cut"]




lmoves_magmar = {'01': ['Ember'], '36': ['Leer'], '39': ['Confuse Ray'], '43': ['Fire Punch'], '48': ['SmokeScreen'], '52': ['Smog'], '55': ['Flamethrower']}
tmoves_magmar = ["Mega Punch", "Mega Kick", "Toxic", "Body Slam", "Take Down", "Double-Edge", "Hyper Beam", "Submission", "Counter", "Seismic Toss", "Rage", "Teleport", "Mimic", "Double Team", "Bide", "Metronome", "Fire Blast", "Skull Bash", "Rest", "Psywave", "Substitute"]
hmoves_magmar = ["Strength"]
lmoves_pinsir = {}
tmoves_pinsir = ["Swords Dance", "Toxic", "Body Slam", "Take Down", "Double-Edge", "Hyper Beam", "Submission", "Seismic Toss", "Rage", "Mimic", "Double Team", "Bide", "Rest", "Substitute"]
hmoves_pinsir = ["Cut", "Strength"]
lmoves_tauros = {'01': ['Tackle'], '21': ['Stomp'], '28': ['Tail Whip'], '35': ['Leer'], '44': ['Rage'], '51': ['Take Down']}
tmoves_tauros = ["Toxic", "Horn Drill", "Body Slam", "Take Down", "Double-Edge", "Ice Beam", "Blizzard", "Hyper Beam", "Rage", "Thunderbolt", "Thunder", "Earthquake", "Fissure", "Mimic", "Double Team", "Bide", "Fire Blast", "Skull Bash", "Rest", "Substitute"]
hmoves_tauros = ["Strength"]
lmoves_magikarp = {'01': ['Splash'], '15': ['Tackle']}
tmoves_magikarp = []
hmoves_magikarp = []
lmoves_gyarados = {}
tmoves_gyarados = ["Toxic", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Rage", "Dragon Rage", "Thunderbolt", "Thunder", "Mimic", "Double Team", "Reflect", "Bide", "Fire Blast", "Skull Bash", "Rest", "Substitute", "Splash", "Tackle"]
hmoves_gyarados = ["Surf", "Strength"]
lmoves_lapras = {'01': ['Water Gun', 'Growl'], '16': ['Sing'], '20': ['Mist'], '25': ['Body Slam'], '31': ['Confuse Ray'], '38': ['Ice Beam'], '46': ['Hydro Pump']}
tmoves_lapras = ["Toxic", "Horn Drill", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Rage", "SolarBeam", "Dragon Rage", "Thunderbolt", "Thunder", "Mimic", "Double Team", "Reflect", "Bide", "Skull Bash", "Rest", "Psywave", "Substitute"]
hmoves_lapras = ["Surf", "Strength"]
lmoves_ditto = {'01': ['Transform']}
tmoves_ditto = []
hmoves_ditto = []
lmoves_eevee = {}
tmoves_eevee = ["Toxic", "Body Slam", "Take Down", "Double-Edge", "Rage", "Mimic", "Double Team", "Reflect", "Bide", "Swift", "Skull Bash", "Rest", "Substitute"]
hmoves_eevee = []
lmoves_vaporeon = {}
tmoves_vaporeon = ["Toxic", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Rage", "Mimic", "Double Team", "Reflect", "Bide", "Swift", "Skull Bash", "Rest", "Substitute", "Focus Energy", "Growl"]
hmoves_vaporeon = ["Surf"]
lmoves_jolteon = {}
tmoves_jolteon = ["Toxic", "Body Slam", "Take Down", "Double-Edge", "Hyper Beam", "Rage", "Thunderbolt", "Thunder", "Mimic", "Double Team", "Reflect", "Bide", "Swift", "Skull Bash", "Rest", "Thunder Wave", "Substitute", "Bite", "Focus Energy", "Growl"]
hmoves_jolteon = ["Flash"]
lmoves_flareon = {}
tmoves_flareon = ["Toxic", "Body Slam", "Take Down", "Double-Edge", "Hyper Beam", "Rage", "Mimic", "Double Team", "Reflect", "Bide", "Fire Blast", "Swift", "Skull Bash", "Rest", "Substitute", "Focus Energy", "Growl"]
hmoves_flareon = []
lmoves_porygon = {'01': ['Tackle', 'Sharpen', 'Conversion'], '23': ['Psybeam'], '28': ['Recover'], '35': ['Agility'], '42': ['Tri Attack']}
tmoves_porygon = ["Toxic", "Take Down", "Double-Edge", "Ice Beam", "Blizzard", "Hyper Beam", "Rage", "Thunderbolt", "Thunder", "Teleport", "Mimic", "Double Team", "Reflect", "Bide", "Swift", "Skull Bash", "Rest", "Thunder Wave", "Psywave", "Tri Attack", "Substitute"]
hmoves_porygon = ["Flash"]
lmoves_omanyte = {'01': ['Water Gun', 'Withdraw'], '34': ['Horn Attack'], '39': ['Leer'], '46': ['Spike Cannon'], '53': ['Hydro Pump']}
tmoves_omanyte = ["Toxic", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Rage", "Mimic", "Double Team", "Reflect", "Bide", "Rest", "Substitute"]
hmoves_omanyte = ["Surf"]
lmoves_omastar = {'01': ['Water Gun', 'Withdraw', 'Horn Attack'], '34': ['Horn Attack'], '39': ['Leer'], '44': ['Spike Cannon'], '49': ['Hydro Pump']}
tmoves_omastar = ["Toxic", "Horn Drill", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Submission", "Seismic Toss", "Rage", "Mimic", "Double Team", "Reflect", "Bide", "Skull Bash", "Rest", "Substitute"]
hmoves_omastar = ["Surf"]
lmoves_kabuto = {'01': ['Scratch', 'Harden'], '34': ['Absorb'], '39': ['Slash'], '44': ['Leer'], '49': ['Hydro Pump']}
tmoves_kabuto = ["Toxic", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Rage", "Mimic", "Double Team", "Reflect", "Bide", "Rest", "Substitute"]
hmoves_kabuto = ["Surf"]
lmoves_kabutops = {'01': ['Scratch', 'Harden', 'Absorb'], '34': ['Absorb'], '39': ['Slash'], '46': ['Leer'], '53': ['Hydro Pump']}
tmoves_kabutops = ["Razor Wind", "Swords Dance", "Mega Kick", "Toxic", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Submission", "Seismic Toss", "Rage", "Mimic", "Double Team", "Reflect", "Bide", "Skull Bash", "Rest", "Substitute"]
hmoves_kabutops = ["Cut", "Surf"]
lmoves_aerodactyl = {'01': ['Wing Attack', 'Agility'], '33': ['Supersonic'], '38': ['Bite'], '45': ['Take Down'], '54': ['Hyper Beam']}
tmoves_aerodactyl = ["Razor Wind", "Whirlwind", "Toxic", "Take Down", "Double-Edge", "Hyper Beam", "Rage", "Dragon Rage", "Mimic", "Double Team", "Reflect", "Bide", "Fire Blast", "Swift", "Sky Attack", "Rest", "Substitute"]
hmoves_aerodactyl = ["Fly"]
lmoves_snorlax = {'01': ['Headbutt', 'Amnesia', 'Rest'], '35': ['Body Slam'], '41': ['Harden'], '48': ['Double-Edge'], '56': ['Hyper Beam']}
tmoves_snorlax = ["Mega Punch", "Mega Kick", "Toxic", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Pay Day", "Submission", "Counter", "Seismic Toss", "Rage", "SolarBeam", "Thunderbolt", "Thunder", "Earthquake", "Fissure", "Mimic", "Double Team", "Reflect", "Bide", "Metronome", "Selfdestruct", "Fire Blast", "Skull Bash", "Rest", "Psywave", "Rock Slide", "Substitute"]
hmoves_snorlax = ["Surf", "Strength"]
lmoves_articuno = {'01': ['Peck', 'Ice Beam'], '51': ['Blizzard'], '55': ['Agility'], '60': ['Mist']}
tmoves_articuno = ["Razor Wind", "Whirlwind", "Toxic", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Rage", "Mimic", "Double Team", "Reflect", "Bide", "Swift", "Sky Attack", "Rest", "Substitute"]
hmoves_articuno = ["Fly"]
lmoves_zapdos = {'01': ['ThunderShock', 'Drill Peck'], '51': ['Thunder'], '55': ['Agility'], '60': ['Light Screen']}
tmoves_zapdos = ["Razor Wind", "Whirlwind", "Toxic", "Take Down", "Double-Edge", "Hyper Beam", "Rage", "Thunderbolt", "Thunder", "Mimic", "Double Team", "Reflect", "Bide", "Swift", "Sky Attack", "Rest", "Thunder Wave", "Substitute"]
hmoves_zapdos = ["Fly", "Flash"]
lmoves_moltres = {'01': ['Peck', 'Fire Spin'], '51': ['Leer'], '55': ['Agility'], '60': ['Sky Attack']}
tmoves_moltres = ["Razor Wind", "Whirlwind", "Toxic", "Take Down", "Double-Edge", "Hyper Beam", "Rage", "Mimic", "Double Team", "Reflect", "Bide", "Fire Blast", "Swift", "Sky Attack", "Rest", "Substitute"]
hmoves_moltres = ["Fly"]
lmoves_dratini = {'01': ['Wrap', 'Leer'], '10': ['Thunder Wave'], '20': ['Agility'], '30': ['Slam'], '40': ['Dragon Rage'], '50': ['Hyper Beam']}
tmoves_dratini = ["Toxic", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Rage", "Dragon Rage", "Thunderbolt", "Thunder", "Mimic", "Double Team", "Reflect", "Bide", "Fire Blast", "Swift", "Skull Bash", "Rest", "Thunder Wave", "Substitute"]
hmoves_dratini = ["Surf"]
lmoves_dragonair = {'01': ['Wrap', 'Leer', 'Thunder Wave'], '10': ['Thunder Wave'], '20': ['Agility'], '35': ['Slam'], '45': ['Dragon Rage'], '55': ['Hyper Beam']}
tmoves_dragonair = ["Toxic", "Horn Drill", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Rage", "Dragon Rage", "Thunderbolt", "Thunder", "Mimic", "Double Team", "Reflect", "Bide", "Fire Blast", "Swift", "Skull Bash", "Rest", "Thunder Wave", "Substitute"]
hmoves_dragonair = ["Surf"]
lmoves_dragonite = {'01': ['Wrap', 'Leer', 'Thunder Wave', 'Agility'], '10': ['Thunder Wave'], '20': ['Agility'], '35': ['Slam'], '45': ['Dragon Rage'], '60': ['Hyper Beam']}
tmoves_dragonite = ["Razor Wind", "Toxic", "Horn Drill", "Body Slam", "Take Down", "Double-Edge", "BubbleBeam", "Water Gun", "Ice Beam", "Blizzard", "Hyper Beam", "Rage", "Dragon Rage", "Thunderbolt", "Thunder", "Mimic", "Double Team", "Reflect", "Bide", "Fire Blast", "Swift", "Skull Bash", "Rest", "Thunder Wave", "Substitute"]
hmoves_dragonite = ["Surf", "Strength"]



# https://bulbapedia.bulbagarden.net/wiki/Weedle_(Pok%C3%A9mon)/Generation_I_learnset#By_leveling_up

bulbasaur = Pokemon("Bulbasaur", 1, "Grass", lmoves_bulbasaur, {16: "Ivysaur", 32: "Venusaur"}, tmoves_bulbasaur,
                    "Poison")
ivysaur = Pokemon("Ivysaur", 2, "Grass", lmoves_ivysaur, {32: "Venusaur"}, tmoves_ivysaur, "Poison")
venusaur = Pokemon("Venusaur", 3, "Grass", lmoves_venusaur, {}, tmoves_venusaur, "Poison")
