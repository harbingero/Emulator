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
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",  # 10
                   "",
                   "Route 1",
                   "Route 2",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",  # 20
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",  # 30
                   "",
                   "",
                   "Route 22",
                   "",
                   "",
                   "",
                   "Mom's Room",
                   "Bedroom",
                   "Gary's House",
                   "Oak's Lab",  # 40
                   "Viridian City Pokecenter",
                   "Viridian City Pokemart",
                   "Viridian City South House",
                   "Viridian City North House",
                   "",
                   "",
                   "Forest Post-house",
                   "",
                   "",
                   "Forest Pre-house",  # 50
                   "Viridian Forest",
                   "",
                   "",
                   "Brock's Gym",
                   "",
                   "Pewter City Pokemart",
                   "",
                   "Pewter City Pokecenter",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""]
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
    item_1 = []
    for item in item_memory_values:
        item_1.append(pyboy.get_memory_value(item))
    map_number = pyboy.get_memory_value(54110)
    map_name = map_number_name[map_number]
    random_spaces = random.randint(1, 7)
    list_of_actions = [hold_a, hold_b, hold_up, hold_down, hold_left, hold_right]
    if "Pallet Town" == map_name and not parcel:
        if printer:
            print("Pallet Town: without parcel.")
        list_of_actions.append(hold_up)
        list_of_actions.append(hold_up)
        list_of_actions.append(hold_a)
        list_of_actions.append(hold_b)
        list_of_actions.append(hold_up)
        list_of_actions.append(hold_left)
        list_of_actions.append(hold_right)
    if "Pallet Town" == map_name and parcel and parcel_item_slot_1 in item_1:
        if printer:
            print("Pallet Town: with parcel but no pokedex.")
        list_of_actions = [hold_up, hold_down, hold_left, hold_right]
        reduced_move = [hold_up]
        reduced_amount = 5
    if "Pallet Town" == map_name and parcel and parcel_item_slot_1 not in item_1:
        if printer:
            print("Pallet Town: with parcel and pokedex.")
        list_of_actions.append(hold_up)
        list_of_actions.append(hold_up)
        list_of_actions.append(hold_a)
        list_of_actions.append(hold_b)
        list_of_actions.append(hold_up)
        list_of_actions.append(hold_left)
        list_of_actions.append(hold_right)
    if "Mom's Room" == map_name and not parcel or "Gary's House" == map_name:
        if printer:
            print(map_name + ": without parcel.")
        list_of_actions.append(hold_down)
        list_of_actions.append(hold_down)
        list_of_actions.append(hold_a)
        list_of_actions.append(hold_a)
        list_of_actions.append(hold_down)
        list_of_actions.append(hold_left)
        list_of_actions.append(hold_right)
    if "Oak's Lab" == map_name and not parcel:
        if printer:
            print("Oak's Lab: without parcel.")
        list_of_actions.append(hold_down)
        list_of_actions.append(hold_down)
        list_of_actions.append(hold_a)
        list_of_actions.append(hold_a)
        list_of_actions.append(hold_down)
        list_of_actions.append(hold_left)
        list_of_actions.append(hold_right)
        reduced_move = [hold_down]
        reduced_amount = 2
    if "Oak's Lab" == map_name and parcel and parcel_item_slot_1 in item_1:
        if printer:
            print("Oak's Lab: with parcel but no pokedex.")
        list_of_actions.append(hold_up)
        list_of_actions.append(hold_up)
        list_of_actions.append(hold_a)
        list_of_actions.append(hold_a)
    if "Oak's Lab" == map_name and parcel and parcel_item_slot_1 not in item_1:
        if printer:
            print("Oak's Lab:  with parcel and pokedex.")
        list_of_actions.append(hold_down)
        list_of_actions.append(hold_down)
    if "Route 1" == map_name and not parcel:
        if printer:
            print("Route 1: without parcel.")
        reduced_move = [hold_down]
        reduced_amount = 1
        list_of_actions = [hold_a, hold_b, hold_up, hold_left, hold_right, hold_up,
                           hold_down, hold_left, hold_right, hold_up, hold_up]
    if "Route 1" == map_name and parcel and parcel_item_slot_1 not in item_1:
        if printer:
            print("Route 1: with parcel but no pokedex.")
        reduced_move = [hold_down]
        reduced_amount = 1
        list_of_actions = [hold_a, hold_b, hold_up, hold_left, hold_right, hold_up,
                           hold_down, hold_left, hold_right, hold_up, hold_up]
    if "Bedroom" == map_name and pyboy.botsupport_manager().sprite(0).on_screen:
        if printer:
            print("Bedroom.")
        reduced_move = [hold_down, hold_left]
        reduced_amount = 1
    if "Route 22" == map_name:
        if printer:
            print("Route 22.")
        reduced_move = [hold_left]
        reduced_amount = 1
        list_of_actions = [hold_a, hold_b, hold_up, hold_right, hold_right, hold_right,
                           hold_down, hold_left, hold_right, hold_right]
    if "Viridian City" == map_name and not parcel:
        if printer:
            print("Viridian City: without parcel.")
        reduced_move = [hold_down]
        reduced_amount = 3
        list_of_actions.append(hold_right)
        list_of_actions.append(hold_up)
        list_of_actions.append(hold_right)
        list_of_actions.append(hold_up)
    if "Viridian City" == map_name and parcel and parcel_item_slot_1 not in item_1:
        if printer:
            print("Viridian City: with parcel and pokedex")
        reduced_move = [hold_down]
        reduced_amount = 3
    if "Viridian City" == map_name and parcel and parcel_item_slot_1 in item_1:
        if printer:
            print("Viridian City: with parcel no pokedex")
        reduced_move = [hold_up]
        reduced_amount = 3
        list_of_actions.append(hold_down)
        list_of_actions.append(hold_down)
    decision = random.randint(0, len(list_of_actions) - 1)
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
        item_1 = []
        for item in item_memory_values:
            item_1.append(pyboy.get_memory_value(item))
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
        if parcel_get and not pokedex_get and 70 not in item_1 and (parcel_time + 500) < counter:
            print(item_1)
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