from pyboy import PyBoy, WindowEvent
import re

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
                   "Forest Post house",
                   "48",
                   "49",
                   "Forest Pre house",  # 50
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
                   "Mt Moon Pokecenter",
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
move_number = ["",  # No Move 0
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
               "Softboiled",
               "Hi Jump Kick",
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
actions = {}
overworld = False
game_flag = "No_Parcel"
pyboy = PyBoy('Roms/Pokemon Red.gb')
manager = pyboy.botsupport_manager()
parcel_item_slot_1 = 70
item_memory_values = [54046,
                      54048,  # 2
                      54050,
                      54052,  # 4
                      54054,
                      54056,  # 6
                      54058,
                      54060,  # 8
                      54062,
                      54064,  # 10
                      54066,
                      54068,  # 12
                      54070,
                      54072,  # 14
                      54074,
                      54076,  # 16
                      54078,
                      54080,  # 18
                      54082,
                      54084]
item_name_list = ["0",
                  "1",
                  "2",
                  "3",
                  "Pokeball",
                  "5",
                  "6",
                  "7",
                  "8",
                  "9",
                  "Moon Stone"
                  "",  # 10
                  "sa"
                  "Antidote",
                  "Burn_Heal",
                  "13",
                  "Awakening",
                  "Paralyze_Heal",
                  "16",
                  "17",
                  "18",
                  "19",
                  "Potion",  # 20
                  "21",
                  "22",
                  "23",
                  "24",
                  "25",
                  "26",
                  "27",
                  "28",
                  "Escape_Rope",
                  "30",  # 30
                  "31",
                  "32",
                  "33",
                  "34",
                  "HP UP",
                  "36",
                  "37",
                  "38",
                  "39",
                  "Rare Candy",  # 40
                  "Dome Fossil",
                  "Helix Fossil",
                  "43",
                  "44",
                  "45",
                  "46",
                  "47",
                  "48",
                  "49",
                  "50",  # 50
                  "51",
                  "52",
                  "53",
                  "54",
                  "55",
                  "56",
                  "57",
                  "58",
                  "59",
                  "60",  # 60
                  "61",
                  "62",
                  "63",
                  "64",
                  "65",
                  "66",
                  "67",
                  "68",
                  "69",
                  "Oak's_Parcel",  # 70
                  "71",
                  "72",
                  "73",
                  "74",
                  "75",
                  "76",
                  "77",
                  "78",
                  "79",
                  "Ether",  # 80
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
                  "TM01",
                  "202",
                  "203",
                  "TM04",
                  "205",
                  "206",
                  "207",
                  "208",
                  "209",
                  "210",  # 210
                  "211",
                  "TM12",
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
                  "230",  # 230
                  "231",
                  "232",
                  "233",
                  "TM34",
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
                  "Empty Slot"]
Rock_badge = 1
game_over = ["RELEASE_ARROW_RIGHT", "RELEASE_ARROW_DOWN", ]
file = "Quitting.txt"


def tick_pass(number):
    printer_number = number
    if number <= 0:
        return None
    while number > 0:
        pyboy.tick()
        number -= 1
    print("----------------------------", printer_number)


def hold_up(x):
    pyboy.send_input(WindowEvent.PRESS_ARROW_UP)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_ARROW_UP)
    pyboy.tick()
    print("Up--------------------------", x)


def hold_down(x):
    pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_ARROW_DOWN)
    pyboy.tick()
    print("--Down----------------------", x)


def hold_left(x):
    pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
    print("------Left------------------", x)
    pyboy.tick()


def hold_right(x):
    pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
    print("----------Right-------------", x)
    pyboy.tick()


def hold_a(x):
    pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
    print("---------------A------------", x)
    pyboy.tick()


def hold_b(x):
    pyboy.send_input(WindowEvent.PRESS_BUTTON_B)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
    print("----------------B-----------", x)
    pyboy.tick()


def hold_start(x):
    pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)
    print("-----------------Start------", x)
    pyboy.tick()


def hold_select(x):
    pyboy.send_input(WindowEvent.PRESS_BUTTON_SELECT)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_SELECT)
    print("----------------------Select", x)
    pyboy.tick()


def press_up():
    pyboy.send_input(WindowEvent.PRESS_ARROW_UP)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_UP)
    print("Up--------------------------")
    pyboy.tick()


def press_down():
    pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_DOWN)
    print("--Down----------------------")
    pyboy.tick()


def press_left():
    pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
    print("------Left------------------")
    pyboy.tick()


def press_right():
    pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
    print("----------Right-------------")
    pyboy.tick()


def press_a():
    pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
    pyboy.tick()
    print("---------------A------------")


def press_b():
    pyboy.send_input(WindowEvent.PRESS_BUTTON_B)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
    print("----------------B-----------")
    pyboy.tick()


def press_start():
    pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)
    print("-----------------Start------")
    pyboy.tick()


def press_select():
    pyboy.send_input(WindowEvent.PRESS_BUTTON_SELECT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_SELECT)
    print("----------------------Select")
    pyboy.tick()


with open(file, "w") as f1:
    f1.write("")


def battle_decisions(turns):
    counter = 0
    decision = None
    move1 = pyboy.get_memory_value(53276)
    move2 = pyboy.get_memory_value(53277)
    move3 = pyboy.get_memory_value(53278)
    move4 = pyboy.get_memory_value(53279)
    move1_pp = pyboy.get_memory_value(53293)
    move2_pp = pyboy.get_memory_value(53294)
    move3_pp = pyboy.get_memory_value(53295)
    move4_pp = pyboy.get_memory_value(53296)
    battle_turn = pyboy.get_memory_value(52437)
    move_list = [move1, move2, move3, move4]
    pp_list = [move1_pp, move2_pp, move3_pp, move4_pp]
    move_selector = pyboy.get_memory_value(53202)
    while decision == None:
        if battle_turn not in turns:
            decision = input("Move?")
            pyboy.tick()
            while decision not in move_number:
                decision = input("Move?")
                pyboy.tick()
        if move_number[move_selector] == decision:
            print(move_number[move_selector], decision)
            press_a()
        if battle_turn not in turns:
            turns.append(battle_turn)
        pyboy.tick()
    return(turns)


while not pyboy.tick():
    turns = []
    parcel_bit = pyboy.get_memory_value(54797)
    back_pack_numbers = []
    back_pack_names = []
    for i in item_memory_values:
        back_pack_numbers.append(pyboy.get_memory_value(i))
    for i in back_pack_numbers:
        back_pack_names.append(item_name_list[i])
    print(back_pack_numbers)
    print(back_pack_names)
    map_number = pyboy.get_memory_value(54110)
    map_name = map_number_name[map_number]
    while pyboy.get_memory_value(53335):
        turns = battle_decisions(turns)
        map_name = "In Battle"
        pyboy.tick()
    sprite0 = manager.sprite(0).on_screen
    parcel = pyboy.get_memory_value(54797)
    badges = pyboy.get_memory_value(54102)
    if game_flag == "Pokedex" and badges > 0:
        game_flag = "Brock"
    if game_flag == "Parcel" and parcel_bit == 2 and parcel_item_slot_1 not in back_pack_numbers:
        game_flag = "Pokedex"
    if game_flag == "No_Parcel" and parcel:
        game_flag = "Parcel"
    print(map_name, badges)
    if map_number > 0 and sprite0:
        overworld = True
    if len(pyboy.get_input()) > 0 and overworld and sprite0:
        for i in pyboy.get_input():
            i = re.sub("RELEASE_BUTTON", "Release", str(i))
            i = re.sub("PRESS_BUTTON", "Press", str(i))
            i = re.sub("PRESS_ARROW", "Press", str(i))
            i = re.sub("RELEASE_ARROW", "Release", str(i))
            i = re.sub("WINDOW_UNFOCUS", "", str(i))
            i = re.sub("WINDOW_FOCUS", "", str(i))
            i = re.sub("PRESS_SPEED_UP", "", str(i))
            i = re.sub("RELEASE_SPEED_UP", "", str(i))
            stringer = map_number_name[map_number] + "_" + str(i) + "_" + game_flag
            if len(i) == 0:
                break
            if stringer not in actions:
                actions[stringer] = 1
            else:
                actions[stringer] += 1
    print("len: ", len(pyboy.get_input()))
    with open(file, "r") as f1:
        file_len = ""
        for line in f1:
            file_len += line
        if len(file_len) > 0:
            pyboy.stop()
            for action in actions:
                print(action, "=", actions[action])
            print(game_flag)
    pass
pyboy.stop()