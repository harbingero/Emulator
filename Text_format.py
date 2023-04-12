import re


def remove_fluff(file):
    no_fluff = []
    count = 0
    for line in file:
        if line.strip() == "<tr>":
            continue
        if line.strip() == "<td>":
            continue
        if line.strip() == "</td>":
            continue
        if line.strip() == "</tr>":
            continue
        line = re.sub("<td>", "", line)
        line = re.sub("</td>", "", line)
        line = re.sub("</tr>", "", line)
        line = re.sub("<a href=\"/wiki/", "", line)
        line = re.sub(
            "<table border=\"1\" class=\"sortable roundy\" style=\"margin:auto; background: #FFF; border:1px solid #ddf; border-collapse:collapse\" width=\"100%\">",
            "", line)
        line = re.sub("<td", "", line)
        line = re.sub("<tbody>", "", line)
        line = re.sub("<tr style=", "", line)
        line = re.sub("\"background: #ddf\">", "", line)
        line = re.sub("<th", "", line)
        line = re.sub("</th>", "", line)
        line = re.sub("%", "", line)
        line = re.sub("style=\"width: [0-9]+px\">", "", line)
        line = re.sub("#", "", line.lstrip())
        line = re.sub("\" title=\"Type\">", "", line)
        line = re.sub("<span", "", line)
        line = re.sub(" style=\"color:000;\">Type</span></a>", "", line)
        line = re.sub("Damage_category\" title=\"", "", line)
        line = re.sub("</span></a>", "", line)
        line = re.sub("\"> style=\"color:000", "", line)
        line = re.sub("\" title=\"[a-z,A-Z]+;\">[a-z,A-Z]+", "", line)
        line = re.sub(";\">[a-z,A-Z]+", "", line)
        line = re.sub("Name", "", line)
        line = re.sub("Damage category", "", line)
        line = re.sub("PP", "", line)
        line = re.sub("Power", "", line)
        line = re.sub("Accuracy", "", line)
        line = re.sub(">Generation", "", line)
        line = re.sub("</a>", "", line)
        line = re.sub("_\(move\)\"", "", line)
        line = re.sub(" \(move\)\"", "", line)
        line = re.sub("title=\"[a-z,A-Z, ,-]+", "", line)
        line = re.sub("\">", "", line)
        line = re.sub(">[a-z,A-Z, ,-]+", "", line)
        line = re.sub("style=\"text-align", "", line)
        line = re.sub(":center; background:", "", line)
        line = re.sub("A8A878", "", line)
        line = re.sub("B8A038", "", line)
        line = re.sub("F85888", "", line)
        line = re.sub("E0C068", "", line)
        line = re.sub("6890F0", "", line)
        line = re.sub("A040A0", "", line)
        line = re.sub("78C850", "", line)
        line = re.sub("A890F0", "", line)
        line = re.sub("A8B820", "", line)
        line = re.sub("C03028", "", line)
        line = re.sub("F08030", "", line)
        line = re.sub("705898", "", line)
        line = re.sub("Type", "", line)
        line = re.sub("_\(type\)\"", "", line)
        line = re.sub(" \(type\)", "", line)
        line = re.sub(" style=\"color:[0-9,A-Z,a-z, ,-]+", "", line)
        line = re.sub("â€”", "None", line)
        line = re.sub("-", "", line)
        if len(line) > 1 and not re.search("align=\"center", line):
            if re.search("166", line):
                return no_fluff
            no_fluff.append(line.rstrip())
            count += 1
    return no_fluff


def combine_inputs(file):
    limiter = 0
    file_line = ""
    existing_map = []
    ending = {}
    pressed = ["Press_LEFT", "Press_RIGHT", "Press_UP", "Press_DOWN", "Press_A", "Press_B"]
    released = ["Release_LEFT", "Release_RIGHT", "Release_UP", "Release_DOWN", "Release_A", "Release_B"]
    for line in file:
        file_line += line
    for map_name in map_number_name:
        if len(map_name) > 3:
            existing_map.append(map_name)
    for maping in existing_map:
        for i in range(0, 6):
            printed = ""
            pressing = maping + "_" + pressed[i] + "[A-Z,a-z,_]+"
            releasing = maping + "_" + released[i] + "[A-Z,a-z,_]+"
            pressing_num = pressing + " = [0-9]+"
            releasing_num = releasing + " = [0-9]+"
            pressed_re = re.findall(pressing_num, file_line)
            released_re = re.findall(releasing_num, file_line)
            for item in pressed_re:
                print(item)
                printed += str(item)
            for item in released_re:
                print(item)
                printed += str(item)  # We now have the ability to check between number and string
    return ending


map_number_name = ["Pallet Town",  # 0
                   "Viridian City",
                   "Pewter City",
                   "Cerulean City",
                   "4",
                   "5",
                   "6",
                   "7",
                   "8",
                   "9",
                   "10",  # 10
                   "11",
                   "Route 1",  # Up of Pallet Town
                   "Route 2",  # Up of Viridian city
                   "Route 3",  # Right of Pewter City
                   "Route 4",
                   "16",
                   "17",
                   "18",
                   "19",
                   "20",  # 20
                   "21",
                   "22",
                   "23",
                   "24",
                   "25",
                   "26",
                   "27",
                   "28",
                   "29",
                   "30",  # 30
                   "31",
                   "32",
                   "Route 22",
                   "34",
                   "Golden Bridge",
                   "36",
                   "Mom's Room",
                   "Bedroom",
                   "Gary's House",
                   "Oak's Lab",  # 40
                   "Viridian City Pokecenter",
                   "Viridian City Pokemart",
                   "Viridian City South House",
                   "Viridian City North House",
                   "45",
                   "46",
                   "Forest Post-house",
                   "48",
                   "49",
                   "Forest Pre-house",  # 50
                   "Viridian Forest",
                   "Pewter City Museum Lower",
                   "Pewter City Museum Upper",
                   "Brock's Gym",
                   "Pewter City House East",
                   "Pewter City Pokemart",
                   "Pewter City House West",
                   "Pewter City Pokecenter",
                   "Mt Moon Beginning",
                   "Mt Moon Tunnels",  # 60
                   "Mt Moon Fossil",
                   "62",
                   "Cerulean City House",
                   "Cerulean City Pokecenter",
                   "Cerulean City Gym",
                   "Bike Shop",
                   "Cerulean City Pokemart",
                   "68",
                   "69",
                   "70",  # 70
                   "71",
                   "72",
                   "73",
                   "74",
                   "75",
                   "76",
                   "77",
                   "78",
                   "79",
                   "80",  # 80
                   "81",
                   "82",
                   "83",
                   "84",
                   "85",
                   "86",
                   "87",
                   "88",
                   "89",
                   "90",  # 90
                   "91",
                   "92",
                   "93",
                   "94",
                   "95",
                   "96",
                   "97",
                   "98",
                   "99",
                   "100",  # 100
                   "101",
                   "102",
                   "103",
                   "104",
                   "105",
                   "106",
                   "107",
                   "108",
                   "109",
                   "110",  # 110
                   "111",
                   "112",
                   "113",
                   "114",
                   "115",
                   "116",
                   "117",
                   "118",
                   "119",
                   "120",  # 120
                   "121",
                   "122",
                   "123",
                   "124",
                   "125",
                   "126",
                   "127",
                   "128",
                   "129",
                   "130",  # 130
                   "131",
                   "132",
                   "133",
                   "134",
                   "135",
                   "136",
                   "137",
                   "138",
                   "139",
                   "140",  # 140
                   "141",
                   "142",
                   "143",
                   "144",
                   "145",
                   "146",
                   "147",
                   "148",
                   "149",
                   "150",  # 150
                   "151",
                   "152",
                   "153",
                   "154",
                   "155",
                   "156",
                   "157",
                   "158",
                   "159",
                   "160",  # 160
                   "161",
                   "162",
                   "163",
                   "164",
                   "165",
                   "166",
                   "167",
                   "168",
                   "169",
                   "170",  # 170
                   "171",
                   "172",
                   "173",
                   "174",
                   "175",
                   "176",
                   "177",
                   "178",
                   "179",
                   "180",  # 180
                   "181",
                   "182",
                   "183",
                   "184",
                   "185",
                   "186",
                   "187",
                   "188",
                   "189",
                   "190",  # 190
                   "191",
                   "192",
                   "193",
                   "194",
                   "195",
                   "196",
                   "197",
                   "198",
                   "199",
                   "200",  # 200
                   "201",
                   "202",
                   "203",
                   "204",
                   "205",
                   "206",
                   "207",
                   "208",
                   "209",
                   "210",  # 210
                   "211",
                   "212",
                   "213",
                   "214",
                   "215",
                   "216",
                   "217",
                   "218",
                   "219",
                   "220",  # 220
                   "221",
                   "222",
                   "223",
                   "224",
                   "225",
                   "226",
                   "227",
                   "228",
                   "229",
                   "Cerulean City Backdoor House",  # 230
                   "231",
                   "232",
                   "233",
                   "234",
                   "235",
                   "236",
                   "237",
                   "238",
                   "239",
                   "240",  # 240
                   "241",
                   "242",
                   "243",
                   "244",
                   "245",
                   "246",
                   "247",
                   "248",
                   "249",
                   "250",  # 250
                   "251",
                   "252",
                   "253",
                   "254",
                   "255"]
file = "Actions_Big.txt"
moves_site = "https://bulbapedia.bulbagarden.net/wiki/List_of_moves"
pokedex = ["Bulbasaur",
           "Ivysaur",
           "Venusaur",
           "Charmander",
           "Charmeleon",
           "Charizard",
           "Squirtle",
           "Wartortle",
           "Blastoise",
           "Caterpie",
           "Metapod",
           "Butterfree",
           "Weedle",
           "Kakuna",
           "Beedrill",
           "Pidgey",
           "Pidgeotto",
           "Pidgeot",
           "Rattata",
           "Raticate",
           "Spearow",
           "Fearow",
           "Ekans",
           "Arbok",
           "Pikachu",
           "Raichu",
           "Sandshrew",
           "Sandslash",
           "Nidoran_f",
           "Nidorina",
           "Nidoqueen",
           "Nidoran_m",
           "Nidorino",
           "Nidoking",
           "Clefairy",
           "Clefable",
           "Vulpix",
           "Ninetales",
           "Jigglypuff",
           "Wigglytuff",
           "Zubat",
           "Golbat",
           "Oddish",
           "Gloom",
           "Vileplume",
           "Paras",
           "Parasect",
           "Venonat",
           "Venomoth",
           "Diglett",
           "Dugtrio",
           "Meowth",
           "Persian",
           "Psyduck",
           "Golduck",
           "Mankey",
           "Primeape",
           "Growlithe",
           "Arcanine",
           "Poliwag",
           "Poliwhirl",
           "Poliwrath",
           "Abra",
           "Kadabra",
           "Alakazam",
           "Machop",
           "Machoke",
           "Machamp",
           "Bellsprout",
           "Weepinbell",
           "Victreebel",
           "Tentacool",
           "Tentacruel",
           "Geodude",
           "Graveler",
           "Golem",
           "Ponyta",
           "Rapidash",
           "Slowpoke",
           "Slowbro",
           "Magnemite",
           "Magneton",
           "Farfetchd",
           "Doduo",
           "Dodrio",
           "Seel",
           "Dewgong",
           "Grimer",
           "Muk",
           "Shellder",
           "Cloyster",
           "Gastly",
           "Haunter",
           "Gengar",
           "Onix",
           "Drowzee",
           "Hypno",
           "Krabby",
           "Kingler",
           "Voltorb",
           "Electrode",
           "Exeggcute",
           "Exeggutor",
           "Cubone",
           "Marowak",
           "Hitmonlee",
           "Hitmonchan",
           "Lickitung",
           "Koffing",
           "Weezing",
           "Rhyhorn",
           "Rhydon",
           "Chansey",
           "Tangela",
           "Kangaskhan",
           "Horsea",
           "Seadra",
           "Goldeen",
           "Seaking",
           "Staryu",
           "Starmie",
           "Mrmime",
           "Scyther",
           "Jynx",
           "Electabuzz",
           "Magmar",
           "Pinsir",
           "Tauros",
           "Magikarp",
           "Gyarados",
           "Lapras",
           "Ditto",
           "Eevee",
           "Vaporeon",
           "Jolteon",
           "Flareon",
           "Porygon",
           "Omanyte",
           "Omastar",
           "Kabuto",
           "Kabutops",
           "Aerodactyl",
           "Snorlax",
           "Articuno",
           "Zapdos",
           "Moltres",
           "Dratini",
           "Dragonair",
           "Dragonite",
           "Mewtwo",
           "Mew"]
removal = ["Rock",
           "Electric",
           "Ice",
           "Grass",
           "Fire",
           "Water",
           "Ghost",
           "Dragon",
           "Normal",
           "Psychic",
           "Dark",
           "Flying",
           "Fighting",
           "Bug",
           "Fairy",
           "Ground",
           "Poison",
           "Steel"]
appended = []
counter = 1
no_scratch = False
x = []
y = []
result = []
result1 = []
bit_values = [52444,
              53202,
              53429,
              53534,
              60636,
              61394,
              61621,
              61726]
second_bit_values = [52444,
                     53202,
                     53429,
                     53534,
                     60636,
                     61394,
                     61621,
                     61726,
                     49335,
                     57527]
final_bit_value = [52444,
                   53202,
                   53429,
                   53534,
                   60636,
                   61394,
                   61621,
                   61726,
                   65492,
                   65284]
moves = ["",  # No Move 0
         "Pound",
         "Karate Chop",
         "Double Slap",
         "Comet Punch",
         "Mega Punch",
         "Pay Day",
         "Fire Punch",
         "Ice Punch",
         "Thunder Punch",
         "Scratch",  # 10
         "ViceGrip",
         "Guillotine",
         "Razor Wind",
         "Swords Dance",
         "Cut",
         "Gust",
         "Wing Attack",
         "Whirlwind",
         "Fly",
         "Bind",  # 20
         "Slam",
         "Vine Whip",
         "Stomp",
         "Double Kick",
         "Mega Kick",
         "Jump Kick",
         "Rolling Kick",
         "Sand-Attack",
         "Headbutt",
         "Horn Attack",  # 30
         "Fury Attack",
         "Horn Drill",
         "Tackle",
         "Body Slam",
         "Wrap",
         "Take Down",
         "Thrash",
         "Double-Edge",
         "Tail Whip",
         "Poison Sting",  # 40
         "Twineedle",
         "Pin Missile",
         "Leer",
         "Bite",
         "Growl",  # 45
         "Roar",
         "Sing",
         "Supersonic",
         "SonicBoom",
         "Disable",  # 50
         "Acid",
         "Ember",
         "Flamethrower",
         "Mist",
         "Water Gun",
         "Hydro Pump",
         "Surf",
         "Ice Beam",
         "Blizzard",
         "Psybeam",  # 60
         "BubbleBeam",
         "Aurora Beam",
         "Hyper Beam",
         "Peck",
         "Drill Peck",
         "Submission",
         "Low Kick",
         "Counter",
         "Seismic Toss",
         "Strength",  # 70
         "Absorb",
         "Mega Drain",
         "Leech Seed",
         "Growth",
         "Razor Leaf",
         "SolarBeam",
         "PoisonPowder",
         "Stun Spore",
         "Sleep Powder",
         "Petal Dance",  # 80
         "String Shot",
         "Dragon Rage",
         "Fire Spin",
         "ThunderShock",
         "Thunderbolt",
         "Thunder Wave",
         "Thunder",
         "Rock Throw",
         "Earthquake",
         "Fissure",  # 90
         "Dig",
         "Toxic",
         "Confusion",
         "Psychic",
         "Hypnosis",
         "Meditate",
         "Agility",
         "Quick Attack",
         "Rage",
         "Teleport",  # 100
         "Night Shade",
         "Mimic",
         "Screech",
         "Double Team",
         "Recover",
         "Harden",
         "Minimize",
         "Smokescreen",
         "Confuse Ray",
         "Withdraw",  # 110
         "Defense Curl",
         "Barrier",
         "Light Screen",
         "Haze",
         "Reflect",
         "Focus Energy",
         "Bide",
         "Metronome",
         "Mirror Move",
         "Selfdestruct",  # 120
         "Egg Bomb",
         "Lick",
         "Smog",
         "Sludge",
         "Bone Club",
         "Fire Blast",
         "Waterfall",
         "Clamp",
         "Swift",
         "Skull Bash",  # 130
         "Spike Cannon",
         "Constrict",
         "Amnesia",
         "Kinesis",
         "SoftBoiled",
         "High Jump Kick",
         "Glare",
         "Dream Eater",
         "Poison Gas",
         "Barrage",  # 140
         "Leech Life",
         "Lovely Kiss",
         "Sky Attack",
         "Transform",
         "Bubble",
         "Dizzy Punch",
         "Spore",
         "Flash",
         "Psywave",
         "Splash",  # 150
         "Acid Armor",
         "Crabhammer",
         "Explosion",
         "Fury Swipes",
         "Bonemerang",
         "Rest",
         "Rock Slide",
         "Hyper Fang",
         "Sharpen",
         "Conversion",  # 160
         "Tri Attack",
         "Super Fang",
         "Slash",
         "Substitute",
         "Struggle"]
types = ["Normal",
         "Fighting",
         "Flying",
         "Ground",
         "Rock",
         "Bug",
         "Ghost",
         "Poison",
         "Steel",
         "Water",
         "Grass",
         "Fire",
         "Ice",
         "Electric",
         "Psychic",
         "Dragon",
         "Dark"]
physical = ["Normal",
            "Fighting",
            "Flyging",
            "Ground",
            "Rock",
            "Bug",
            "Ghost",
            "Poison",
            "Steel"]
special = ["Water",
           "Grass",
           "Fire",
           "Ice",
           "Electric",
           "Psychic",
           "Dragon",
           "Dark"]
concat = ""
tms = ["Mega Punch",
       "Razor Wind",
       "Swords Dance",
       "Whirlwind",
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
       "Mega Drain",
       "SolarBeam",
       "Dragon Rage",
       "Thunderbolt",
       "Thunder",
       "Earthquake",
       "Fissure",
       "Dig",
       "Psychic",
       "Teleport",
       "Mimic",
       "Double Team",
       "Reflect",
       "Bide",
       "Metronome",
       "Selfdestruct",
       "Egg Bomb",
       "Fire Blast",
       "Swift",
       "Skull Bash",
       "Softboiled",
       "Dream Eater",
       "Sky Attack",
       "Rest",
       "Thunder Wave",
       "Psywave",
       "Explosion",
       "Rock Slide",
       "Tri Attack",
       "Substitute"]

with open(file, "r") as f1:
    combined_inputs = combine_inputs(f1)
    # defluffed = remove_fluff(f1)
this_equals = ""
split = True
the_type = ""
bit_number = ""
pp = ""
damage = ""
accuracy = ""
tm = False

# for i in range(80, 256):
#     if i % 10 == 0:
#         print("\"" + str(i) + "\",  #" + str(i))
#     else:
#         print("\"" + str(i) + "\",")
for i in combined_inputs:
    print(i)

# for line in defluffed:
#     spaced = re.sub("_", " ", line)
#     # print(line)
#     # print("Spaced: ", spaced)
#     if spaced in moves and len(this_equals) == 0:
#         this_equals = line
#         if spaced in tms:
#             tm = True
#     if line in types and len(the_type) == 0:
#         the_type = line
#     if len(the_type) > 0 and the_type in special:
#         split = False
#     if str(line) == str(counter) and len(bit_number) == 0:
#         bit_number = str(line)
#     appended.append(line)
#     if line == "I":
#         # print(appended)
#         concat = this_equals.lower() + " = Move(\"" + the_type + "\",\n" + str(split) + ",\n" + appended[3] + ",\n" + appended[4] + ",\n" + appended[5] + ",\n" + str(tm) + ",\n" + bit_number + ")"
#         concat = re.sub("\'", "", concat)
#         print(concat)
#         concat = ""
#         counter += 1
#         this_equals = ""
#         split = True
#         the_type = ""
#         bit_number = ""
#         pp = ""
#         damage = ""
#         accuracy = ""
#         appended = []
#         tm = False


# for i in moves:
#     variable_name = re.sub(" ", "_", i)
#     print(variable_name + " = Move(Type,\nTrue,\n0,\n0,\n0,\nFalse,\n" + str(counter) + ")")
#     counter += 1

# for i in bit_values:
#     if i not in final_bit_value:
#         if i not in second_bit_values:
#             if i not in result:
#                 result.append(i)
#
# for i in second_bit_values:
#     if i not in final_bit_value:
#         if i not in result1:
#             result1.append(i)
# print(result)
# print(result1)

# with open(file, "r") as f1:
#     for line in f1:
#         if line[0] == "_":
#             no_scratch = True
#         if not no_scratch:
#             for i in line.split():
#                 if i not in x and len(i) > 0:
#                     x.append(i)
#         if no_scratch and line[0] != "_":
#             for i in line.split():
#                 if i not in y:
#                     y.append(i)
# print(x)
# print(y)
# for i in x:
#     if i not in y:
#         result.append(int(i))
# print(result)


# with open(file, "r") as f1:
#     for line in f1:
#         items = line.split()
#         for item in items:
#             if re.search("^#", item):
#                 print("passed ^#: ", item)
#                 continue
#             if item in removal:
#                 print("In removal: ", item)
#                 continue
#             if item in appended:
#                 continue
#             appended.append(item)
# for pokemon in pokedex:
#     plus1 = counter + 1
#     appended.append(pokemon.lower() + " = Pokemon(pokedex[" + str(counter) + "],"
#                     "\n\t\t" + str(plus1) +
#                     ",\n\t\t\"type1\""
#                     ",\n\t\tlmoves_" + pokemon.lower() +
#                     ",\n\t\t{}"
#                     ",\n\t\ttmoves_" + pokemon.lower() +
#                     ",\n\t\thmoves_" + pokemon.lower() +
#                     ",\n\t\t\"\")")
#     counter = plus1
# for item in appended:
#     print(item)
# print(appended)
