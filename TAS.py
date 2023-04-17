import random
from pyboy import PyBoy
from pyboy import botsupport
from pyboy import WindowEvent
from pyboy import openai_gym
import pyboy.plugins
from time import sleep, time, strftime, gmtime

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
counter = 0
bits = 65529
battle_selector = [52444,  # Your move used
                   53202,  # Player's Move ID
                   53429,  # Undocumented
                   53534,  # Undocumented
                   60636,  # Undocumented
                   61394,  # Undocumented
                   61621,  # Undocumented
                   61726]  # Undocumented
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


def tick_pass(number):
    printer_number = number
    if number <= 0:
        return None
    while number > 0:
        pyboy.tick()
        number -= 1
    print("----------------------------", printer_number)


#  A future potential improvement on the code would be to append button presses to show what inputs it's getting.
#  I'm sure I would have to modify each of these functions to tick elsewhere.  This would allow multiple inputs at once.


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


def battle_decision(turns):
    lister = []
    list_of_actions = [hold_a, hold_up, hold_down]
    move1_pp = pyboy.get_memory_value(53293)
    move2_pp = pyboy.get_memory_value(53294)
    move3_pp = pyboy.get_memory_value(53295)
    move4_pp = pyboy.get_memory_value(53296)
    battle_turn = pyboy.get_memory_value(52437)
    move1 = pyboy.get_memory_value(53276)
    move2 = pyboy.get_memory_value(53277)
    move3 = pyboy.get_memory_value(53278)
    move4 = pyboy.get_memory_value(53279)
    move_pool = []
    if move1_pp > 0:
        decided = 0
    elif move2_pp > 0:
        decided = 1
    elif move3_pp > 0:
        decided = 2
    else:
        decided = 3
    moves = [move1, move2, move3, move4]  # List of all moves the pokemon knows 0=blank
    for move in moves:
        if len(move_number[move]) > 0:
            move_pool.append(move)
    # list_of_actions[random.randint(0, len(list_of_actions) - 1)](21)
    for i in range(29781, 29800):
        lister.append(i)


def overworld_move():
    printer = False
    reduced_move = None
    reduced_amount = None
    parcel_item_slot_1 = 70
    manager = pyboy.botsupport_manager()
    parcel = pyboy.get_memory_value(54797)
    back_pack_numbers = []
    back_pack_names = []
    badges = pyboy.get_memory_value(54102)
    for item in item_memory_values:
        back_pack_numbers.append(pyboy.get_memory_value(item))
        back_pack_names.append(item_name_list[pyboy.get_memory_value(item)])
    map_number = pyboy.get_memory_value(54110)
    map_name = map_number_name[map_number]
    random_spaces = random.randint(1, 7)
    list_of_actions = [hold_a, hold_b, hold_up, hold_down, hold_left, hold_right]
    if badges == 1:
        print(badges)
        if map_name == "Route 4":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 2
            bb = 1
            down = 12
            left = 14
            right = 31
            up = 40
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Cerulean City Backdoor House":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 3
            bb = 3
            down = 21
            left = 26
            right = 21
            up = 26
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Cerulean City":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 13
            bb = 13
            down = 8
            left = 23
            right = 23
            up = 20
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Golden Bridge":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 10
            bb = 10
            down = 10
            left = 20
            right = 20
            up = 30
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Mt Moon Beginning":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 14
            bb = 24
            down = 8
            left = 20
            right = 14
            up = 19
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Mt Moon Tunnels":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 1
            bb = 20
            down = 23
            left = 8
            right = 47
            up = 7
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Mt Moon Fassil":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 12
            bb = 29
            down = 10
            left = 20
            right = 13
            up = 15
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Cerulean City House":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 2
            bb = 2
            down = 28
            left = 24
            right = 24
            up = 21
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Cerulean City Pokecenter":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 16
            bb = 27
            down = 19
            left = 13
            right = 8
            up = 17
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Cerulean City Gym":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 35
            left = 12
            right = 12
            up = 39
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Forest Post House":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 18
            left = 23
            right = 21
            up = 36
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Forest Pre House":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 2
            bb = 2
            down = 15
            left = 35
            right = 23
            up = 23
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Gary's House":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 2
            bb = 2
            down = 30
            left = 25
            right = 15
            up = 25
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Mom's Room":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 2
            bb = 2
            down = 29
            left = 29
            right = 14
            up = 24
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Oak's Lab":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 27
            left = 24
            right = 27
            up = 19
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pallet Town":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 19
            left = 25
            right = 25
            up = 29
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pewter City House East":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 3
            bb = 3
            down = 40
            left = 27
            right = 13
            up = 13
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pewter City House West":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 6
            bb = 6
            down = 42
            left = 13
            right = 13
            up = 20
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pewter City Museum Lower":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 3
            bb = 26
            down = 26
            left = 19
            right = 19
            up = 6
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pewter City Museum Upper":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 10
            bb = 15
            down = 20
            left = 18
            right = 18
            up = 20
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pewter City Pokecenter":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 20
            bb = 16
            down = 16
            left = 16
            right = 16
            up = 16
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pewter City Pokemart":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 18
            bb = 18
            down = 16
            left = 16
            right = 16
            up = 16
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pewter City":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 20
            left = 19
            right = 36
            up = 23
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Route 1":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 3
            bb = 10
            down = 21
            left = 16
            right = 24
            up = 26
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Route 2":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 26
            left = 24
            right = 21
            up = 26
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Route 22":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 7
            bb = 7
            down = 8
            left = 7
            right = 63
            up = 8
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Route 3":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 21
            bb = 23
            down = 7
            left = 5
            right = 42
            up = 11
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City North House":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 2
            bb = 2
            down = 26
            left = 15
            right = 22
            up = 33
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City Pokecenter":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 3
            bb = 3
            down = 30
            left = 30
            right = 18
            up = 18
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City Pokecenter":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 22
            bb = 10
            down = 17
            left = 17
            right = 17
            up = 17
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City Pokemart":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 5
            bb = 5
            down = 35
            left = 20
            right = 20
            up = 18
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City South House":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 6
            bb = 6
            down = 38
            left = 13
            right = 25
            up = 13
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 17
            left = 30
            right = 17
            up = 34
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian Forest":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 4
            bb = 3
            down = 35
            left = 12
            right = 8
            up = 37
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
    if parcel and "Oak's_Parcel" not in back_pack_names:
        if map_name == "Bedroom":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 3
            bb = 3
            down = 30
            left = 30
            right = 18
            up = 18
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Brock's Gym":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 24
            bb = 16
            down = 9
            left = 13
            right = 1
            up = 37
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Forest Post House":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 10
            left = 14
            right = 12
            up = 63
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Forest Pre House":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 7
            left = 17
            right = 23
            up = 51
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Gary's House":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 2
            bb = 2
            down = 54
            left = 14
            right = 14
            up = 14
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Mom's Room":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 2
            bb = 2
            down = 26
            left = 26
            right = 22
            up = 22
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Oak's Lab":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 8
            bb = 68
            down = 11
            left = 4
            right = 5
            up = 4
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pallet Town":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 19
            left = 27
            right = 13
            up = 40
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pewter City House East":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 2
            bb = 2
            down = 33
            left = 29
            right = 14
            up = 19
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pewter City House West":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 2
            bb = 2
            down = 24
            left = 38
            right = 17
            up = 17
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pewter City Museum Lower":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 4
            bb = 8
            down = 27
            left = 22
            right = 22
            up = 17
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pewter City Museum Upper":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 14
            bb = 7
            down = 27
            left = 20
            right = 18
            up = 14
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pewter City Pokecenter":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 14
            bb = 19
            down = 24
            left = 9
            right = 4
            up = 30
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pewter City Pokemart":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 14
            bb = 19
            down = 24
            left = 19
            right = 14
            up = 10
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pewter City":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 18
            left = 21
            right = 23
            up = 35
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Route 1":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 19
            bb = 7
            down = 1
            left = 13
            right = 9
            up = 50
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Route 2":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 6
            bb = 1
            down = 10
            left = 22
            right = 18
            up = 43
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Route 22":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 4
            bb = 4
            down = 8
            left = 8
            right = 68
            up = 8
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City North House":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 3
            bb = 3
            down = 33
            left = 17
            right = 17
            up = 28
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City Pokecenter":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 20
            bb = 20
            down = 24
            left = 8
            right = 8
            up = 20
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City Pokemart":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 2
            bb = 2
            down = 40
            left = 23
            right = 20
            up = 13
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City South House":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 2
            bb = 2
            down = 23
            left = 32
            right = 18
            up = 23
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 5
            left = 15
            right = 37
            up = 42
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian Forest":
            print(map_name, "Pokedex")
            list_of_actions = []
            ab = 17
            bb = 12
            down = 21
            left = 10
            right = 7
            up = 32
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Cerulean City Pokemart":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 2
            bb = 2
            down = 50
            left = 20
            right = 13
            up = 13
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Bedroom":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 4
            bb = 4
            down = 34
            left = 25
            right = 17
            up = 17
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Brock's Gym":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 0
            bb = 0
            down = 100
            left = 0
            right = 0
            up = 0
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Forest Post-House":
            print(map_name, "Brock")
            list_of_actions = []
            ab = 3
            bb = 3
            down = 30
            left = 30
            right = 18
            up = 18
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
    if parcel and "Oak's_Parcel" in back_pack_names:
        if map_name == "Bedroom":
            print(map_name, "parcel")
            list_of_actions = []
            ab = 3
            bb = 3
            down = 22
            left = 29
            right = 22
            up = 22
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Gary's House":
            print(map_name, "parcel")
            list_of_actions = []
            ab = 3
            bb = 3
            down = 69
            left = 9
            right = 4
            up = 12
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Mom's Room":
            print(map_name, "parcel")
            list_of_actions = []
            ab = 3
            bb = 3
            down = 27
            left = 20
            right = 20
            up = 27
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Oak's Lab":
            print(map_name, "parcel")
            list_of_actions = []
            ab = 24
            bb = 3
            down = 3
            left = 3
            right = 3
            up = 64
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pallet Town":
            print(map_name, "parcel")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 55
            left = 16
            right = 15
            up = 13
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
            reduced_move = [hold_up]
            reduced_amount = 5
        if map_name == "Route 1":
            print(map_name, "parcel")
            list_of_actions = []
            ab = 2
            bb = 1
            down = 48
            left = 18
            right = 30
            up = 1
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Route 22":
            print(map_name, "parcel")
            list_of_actions = []
            ab = 4
            bb = 5
            down = 7
            left = 5
            right = 67
            up = 12
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City North House":
            print(map_name, "parcel")
            list_of_actions = []
            ab = 5
            bb = 5
            down = 81
            left = 3
            right = 3
            up = 3
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City Pokecenter":
            print(map_name, "parcel")
            list_of_actions = []
            ab = 22
            bb = 9
            down = 30
            left = 2
            right = 2
            up = 35
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City Pokemart":
            print(map_name, "parcel")
            list_of_actions = []
            ab = 8
            bb = 46
            down = 16
            left = 5
            right = 20
            up = 5
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City South House":
            print(map_name, "parcel")
            list_of_actions = []
            ab = 3
            bb = 3
            down = 48
            left = 15
            right = 15
            up = 15
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City":
            print(map_name, "parcel")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 47
            left = 28
            right = 17
            up = 6
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
    if parcel == 0:
        if map_name == "Bedroom":
            print(map_name, "parcelless")
            list_of_actions = []
            up = 30
            right = 27
            left = 19
            down = 11
            ab = 2
            bb = 11
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Gary's House":
            print(map_name, "parcelless")
            list_of_actions = []
            up = 1
            right = 1
            left = 1
            down = 95
            ab = 1
            bb = 1
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Mom's Room":
            print(map_name, "parcelless")
            list_of_actions = []
            up = 2
            right = 14
            left = 21
            down = 62
            ab = 1
            bb = 1
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Oak's Lab":
            print(map_name, "parcelless")
            list_of_actions = []
            up = 13
            right = 17
            left = 17
            down = 25
            ab = 18
            bb = 10
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Pallet Town":
            print(map_name, "parcelless")
            list_of_actions = []
            up = 29
            right = 21
            left = 21
            down = 5
            ab = 12
            bb = 12
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
            reduced_move = [hold_down]
            reduced_amount = 2
        if map_name == "Route 1":
            print(map_name, "parcelless")
            list_of_actions = []
            up = 54
            right = 12
            left = 10
            down = 1
            ab = 14
            bb = 9
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
            reduced_move = [hold_down]
            reduced_amount = 1
        if map_name == "Route 22":
            print(map_name, "parcelless")
            list_of_actions = []
            ab = 8
            bb = 8
            down = 21
            left = 1
            right = 41
            up = 21
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
            reduced_move = [hold_left]
        if map_name == "Viridian City North House":
            print(map_name, "parcelless")
            list_of_actions = []
            ab = 4
            bb = 4
            down = 58
            left = 18
            right = 8
            up = 8
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City Pokecenter":
            print(map_name, "parcelless")
            list_of_actions = []
            ab = 31
            bb = 7
            down = 13
            left = 7
            right = 5
            up = 37
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City Pokemart":
            print(map_name, "parcelless")
            list_of_actions = []
            ab = 48
            bb = 48
            down = 1
            left = 1
            right = 1
            up = 1
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
        if map_name == "Viridian City":
            print(map_name, "parcelless")
            list_of_actions = []
            ab = 1
            bb = 1
            down = 12
            left = 28
            right = 32
            up = 27
            for u in range(0, up):
                list_of_actions.append(hold_up)
            for r in range(0, right):
                list_of_actions.append(hold_right)
            for l in range(0, left):
                list_of_actions.append(hold_left)
            for d in range(0, down):
                list_of_actions.append(hold_down)
            for a in range(0, ab):
                list_of_actions.append(hold_a)
            for b in range(0, bb):
                list_of_actions.append(hold_b)
            reduced_move = [hold_down]
            reduced_amount = 4
    decision = random.randint(0, len(list_of_actions) - 1)
    print("List of actions: ", len(list_of_actions))
    if list_of_actions[decision] == hold_a or list_of_actions[decision] == hold_b:  # hold a or b only one frame
        list_of_actions[decision](16)
    else:  # Not hold a or b
        if reduced_move is not None:
            if list_of_actions[decision] in reduced_move:
                random_spaces = random.randint(1, reduced_amount)
        for space in range(random_spaces):
            map_position = manager.screen().tilemap_position()[0]
            list_of_actions[decision](16)
            check_map = pyboy.get_memory_value(54110)
            if check_map != map_number:
                break
            check_move = manager.screen().tilemap_position()[0]
            if map_position == check_move:
                break


pyboy = PyBoy('Roms/Pokemon Red.gb')


def main(counter):
    parcel_get = False
    pokedex_get = False
    parcel_time = 0
    pokedex_time = 0
    item_memory_values = [54046, 54058, 54060, 54062]
    start_time = time()
    while not pyboy.tick():
        back_pack_numbers = []
        for item in item_memory_values:
            back_pack_numbers.append(pyboy.get_memory_value(item))
        list_of_actions = [hold_a, hold_b, hold_up, hold_down, hold_left, hold_right]
        manager = pyboy.botsupport_manager()
        counted = False
        move1 = pyboy.get_memory_value(53276)
        move2 = pyboy.get_memory_value(53277)
        move3 = pyboy.get_memory_value(53278)
        move4 = pyboy.get_memory_value(53279)
        turn_count = []
        in_battle = pyboy.get_memory_value(53335)
        while not manager.sprite(0).on_screen and not in_battle:
            list_of_actions = [hold_a, hold_up, hold_down, hold_left, hold_right, hold_a, hold_b, hold_up, hold_down,
                               hold_left, hold_right]
            list_of_actions[random.randint(0, len(list_of_actions) - 1)](16)
        while in_battle:
            scratch_appender = []  # scratch is move 10.  tackle is 33. growl is 45
            list_in_battle = [hold_a, hold_down, hold_up]
            if pyboy.get_memory_value(53293) > 0 and pyboy.get_memory_value(53276) != 0:
                for i in range(0, 5):
                    list_in_battle.append(hold_a)
                list_in_battle[random.randint(0, len(list_in_battle) - 1)](21)
            else:
                list_of_actions = [hold_a, hold_up, hold_down, hold_a, hold_a]
                list_of_actions[random.randint(0, len(list_of_actions) - 1)](21)
            battle_decision(turn_count)
            pyboy.tick()
            tester = pyboy.get_memory_value(bits)
            in_battle = pyboy.get_memory_value(53335)
            counter += 1
        if not counted:
            counter += 1
        print(counter)
        while pyboy.get_memory_value(54110) == 40 and not manager.sprite(
                0).on_screen and not in_battle:  # This fixes a bug where if you attempt to leave Oak's lab without a pokemon too much, your sprite is no longer on the screen for some reason.  And pressing start and backing out fixes this.
            tick_pass(40)
            press_start()
            tick_pass(40)
            press_b()
            tick_pass(40)
        if pyboy.get_memory_value(54797) and not parcel_get:
            parcel_get = True
            parcel_time = counter
        if parcel_get and not pokedex_get and 70 not in back_pack_numbers and (parcel_time + 500) < counter:
            print(back_pack_numbers)
            pokedex_get = True
            pokedex_time = counter
        if pyboy.get_memory_value(54797):
            print("Ticks to Parcel: ", parcel_time)
        if pokedex_get:
            print("Ticks to Pokedex: ", pokedex_time)
        overworld_move()
        list_of_actions = [hold_a, hold_b, hold_up, hold_down, hold_left, hold_right]
    pyboy.stop()


main(counter)