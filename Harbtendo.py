# TO DO:
# create a list of all map location numbers
# create battle decision function
# flesh out battle values function
# determine if I need to go back and heal after battle (Poison, low HP, etc.)
# figure out if after a level up, if a Pokémon is learning a new move
import struct
import colorama
from colorama import Fore
import random
from pyboy import PyBoy
from pyboy import botsupport
from pyboy import WindowEvent
from pyboy import openai_gym
import pyboy.plugins

turn_counter = []
appended = ""
started = False
named = False
pathed_to_starters = False
starters = ["Charmander", "Squirtle", "Bulbasaur"]
play_time = 5000000
regain_control = False
overwrite = True
controlled_ticks = 0
letter_axis = {"a": "00",
               "b": "10",
               "c": "20",
               "d": "30",
               "e": "40",
               "f": "50",
               "g": "60",
               "h": "70",
               "i": "80",
               "j": "01",
               "k": "11",
               "l": "21",
               "m": "31",
               "n": "41",
               "o": "51",
               "p": "61",
               "q": "71",
               "r": "81",
               "s": "02",
               "t": "12",
               "u": "22",
               "v": "32",
               "w": "42",
               "x": "52",
               "y": "62",
               "z": "72",
               " ": "82",
               "*": "03",
               "(": "13",
               ")": "23",
               ":": "33",
               ";": "43",
               "[": "53",
               "]": "63",
               "#": "73",  # pk
               "$": "83",  # mn
               "-": "04",
               "?": "14",
               "!": "24",
               "^": "34",  # ♂
               "%": "44",  # ♀
               "/": "54",
               ".": "64",
               ",": "74",
               "&": "84"}  # (*)=x,  (#)=pk, ($)=mn, (^)=♂, (%)=♀, (&)=End
player_name = ["Jesse", "Josh", "Sam", "Dakota", "Ash", "Smant"]
rival_name = ["Blue", "Gio", "Trash", "Oak", "Gary", "Logan"]
pokemon_name = ["Good Boy", "Puppy", "Slave", "Legend"]

map_number_name = ["Pallet Town",
                   "Viridian City",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "Route 1",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "Mom's Room",
                   "Bedroom",
                   "Gary's House",
                   "Oak's Lab",
                   "Viridian City Pokecenter",
                   "Viridian City Pokemart",
                   "Viridian City South House",
                   "Viridian City North House",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""]
map_no_paths = {"Bedroom": ["00", "05", "06", "33", "34", "65", "66"],
                "Mom's Room": ["00", "01", "30", "33", "34", "43", "44", "53"]}
map_destinations = {"Bedroom": ["70"],
                    "Mom's Room": ["27", "37", "70"]}
move_number = ["",  # No Move 0
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "Scratch",  # 10
               "",
               "",
               "",
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
               "Tackle",
               "",
               "",
               "",
               "",
               "",
               "Tail Whip",
               "",  # 40
               "",
               "",
               "",
               "",
               "Growl",  # 45
               "",
               "",
               "",
               "",
               "",  # 50
               "",
               "Ember",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",  # 60
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",  # 70
               "",
               "",
               "Leech Seed",
               "",
               "",
               "",
               "",
               "",
               "",
               "",  # 80
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",  # 90
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",  # 100
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",  # 110
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",  # 120
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",  # 130
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",  # 140
               "",
               "",
               "",
               "",
               "Bubble",
               "",
               "",
               "",
               "",
               "",  # 150
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",  # 160
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",
               "",  # 170
               ""]
status_move = ["Growl",
               "Tail Whip"]
damage_move = ["Scratch",
               "Tackle",
               "Ember"]

#  0 Pallet Town
#  1 Viridian City
#  12 Route 1
#  33 Left of Viridian City
#  37 Downstairs home
#  38 Bedroom
#  39 Gary's house
#  40 Oak's lab
#  41 Viridian City Pokemon Center
#  42 Viridian City Pokemart
#  43 Viridian City House
#  44 Viridian City House

if overwrite:
    with open("debug.txt", "w") as f1:
        f1.write("")


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
    pyboy.tick()
    print("------Left------------------", x)


def hold_right(x):
    pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
    pyboy.tick()
    print("----------Right-------------", x)


def hold_a(x):
    pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
    pyboy.tick()
    print("---------------A------------", x)


def hold_b(x):
    pyboy.send_input(WindowEvent.PRESS_BUTTON_B)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
    pyboy.tick()
    print("----------------B-----------", x)


def hold_start(x):
    pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)
    pyboy.tick()
    print("-----------------Start------", x)


def hold_select(x):
    pyboy.send_input(WindowEvent.PRESS_BUTTON_SELECT)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_SELECT)
    pyboy.tick()
    print("----------------------Select", x)


def press_up():
    pyboy.send_input(WindowEvent.PRESS_ARROW_UP)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_UP)
    pyboy.tick()
    print("Up--------------------------")


def press_down():
    pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_DOWN)
    pyboy.tick()
    print("--Down----------------------")


def press_left():
    pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
    pyboy.tick()
    print("------Left------------------")


def press_right():
    pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
    pyboy.tick()
    print("----------Right-------------")


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
    pyboy.tick()
    print("----------------B-----------")


def press_start():
    pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)
    pyboy.tick()
    print("-----------------Start------")


def press_select():
    pyboy.send_input(WindowEvent.PRESS_BUTTON_SELECT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_SELECT)
    pyboy.tick()
    print("----------------------Select")


def spell_name(name):
    xi = 55
    for i in range(1):
        press_b()
        tick_pass(xi)
    x = 0
    y = 0
    caps = True
    for letter in name:
        x_true = False
        y_true = False
        while x_true is False and y_true is False:
            destination = letter_axis[letter.lower()]
            delta_x = int(destination[0]) - x
            delta_y = int(destination[1]) - y
            if delta_x == 0:
                x_true = True
            if delta_y == 0:
                y_true = True
            if delta_x > 0:
                for i in range(delta_x):
                    press_right()
                    tick_pass(xi)
                    x = x + 1
            if delta_x < 0:
                delta_x = delta_x * (-1)
                for i in range(delta_x):
                    press_left()
                    tick_pass(xi)
                    x = x - 1
            if delta_y > 0:
                for i in range(delta_y):
                    press_down()
                    tick_pass(xi)
                    y = y + 1
            if delta_y < 0:
                delta_y = delta_y * (-1)
                for i in range(delta_y):
                    press_up()
                    tick_pass(xi)
                    y = y - 1
        press_a()
        tick_pass(xi)
        if caps:
            press_select()
            tick_pass(xi)
            caps = False
        if letter == " ":
            press_select()
            tick_pass(xi)
            caps = True
    press_start()
    tick_pass(xi)


def naming(fun_named):
    xi = 120
    xj = 60
    for h in range(25):  # 25
        press_b()
        tick_pass(xj)
    press_a()
    tick_pass(xi)
    spell_name(player_name[random.randint(0, len(player_name) - 1)])
    for k in range(11):  # 11
        press_b()
        tick_pass(xj)
    tick_pass(xi)
    press_a()
    tick_pass(xi)
    spell_name(rival_name[random.randint(0, len(rival_name) - 1)])
    for c in range(12):  # 12
        press_b()
        tick_pass(xj)
    fun_named = True
    return fun_named


def overworld_move():
    test_move = False
    random_moves = random.randint(0, 8)
    parcel_maps = ["Oak's Lab", "Mom's Room", "Gary's House"]
    parcel = pyboy.get_memory_value(54797)
    map_number = pyboy.get_memory_value(54110)
    map_name = map_number_name[map_number]
    print(parcel)
    list_of_actions = [hold_a, hold_up, hold_down, hold_left, hold_right, hold_b]
    if map_name == "Pallet Town" and not parcel:
        list_of_actions.append(hold_up)
        list_of_actions.append(hold_up)
    if not parcel and map_name in parcel_maps:
        list_of_actions.append(hold_down)
        list_of_actions.append(hold_down)
    if map_name == "Route 1" and not parcel:
        list_of_actions = [hold_a, hold_up, hold_left, hold_right, hold_b]
    if map_name == "Bedroom":
        list_of_actions = [hold_right, hold_up]
    if not test_move:
        list_of_actions[random.randint(0, len(list_of_actions) - 1)](21 * random_moves)



#     print(map_number)
#     map_name = map_number_name[map_number]
#     no_paths = map_no_paths[map_name]
#     if len(map_destinations[map_name]) < 2:
#         random_destination = random.randint(0, len(map_destinations[map_name]) - 1)
#     else:
#         random_destination = 0
#     destination = map_destinations[map_name][random_destination]
#     print(destination)
#     print(no_paths)
#     while x != int(destination[0]) and y != int(destination[1]):
#         try_left = True
#         try_right = True
#         try_up = True
#         try_down = True
#         print(destination[0], destination[1])
#         delta_x = int(destination[0]) - x
#         delta_y = int(destination[1]) - y
#         if delta_x > 0:  # Try right
#             trying = str(int(x+1)) + y
#             for position in no_paths:
#                 if trying in position:
#                     try_right = False
#         if delta_x < 0:  # Try left
#             trying = str(int(x-1)) + y
#             for position in no_paths:
#                 if trying in position:
#                     try_left = False
#         if delta_y > 0:  # Try down
#             trying = x + str(int(y+1))
#             for position in no_paths:
#                 if trying in position:
#                     try_down = False
#         if delta_y < 0:  # Try up
#             trying = x + str(int(y-1))
#             for position in no_paths:
#                 if trying in position:
#                     try_up = False
#         print("UP: ", try_up, "\nDOWN: ", try_down, "\nLEFT: ", try_left, "\nRIGHT: ", try_right)
#         vert_or_hori = random.randint(0, 1)   #  0=vertical 1=horizontal
#         if vert_or_hori == 0
#         riup_or_ledo = random.randint(0, 4)  # 0,1,2=towards direction 3=opposite direction
#               #  To continue I need to go left/right and determine if I can go into the next square
#     return x, y  #  Once this function is done, I need to delete the while loop under where this is being implimented in to_starters and impliment this in Mom's room as well.xi = 55


def to_starters(name):
    walk_speed = 21
    transition = 40
    oak_walk = 500
    random_starter = random.randint(0, 2)
    x = 3
    y = 5
    tick_pass(250)
    # x, y = overworld_move(pyboy.get_memory_value(54110), x, y)
    while pyboy.get_memory_value(54110) == 38:
        hold_right(walk_speed * 1)
        hold_up(walk_speed * 1)
    tick_pass(transition)  # Out of room
    hold_down(walk_speed * 5)
    hold_left(walk_speed * 4)
    hold_down(walk_speed)
    tick_pass(transition)  # Out of house
    hold_right(walk_speed * 5)
    hold_up(walk_speed * 5)
    for i in range(1000):  # 1250 In grass
        press_b()
        pyboy.tick()
    # tick_pass(oak_walk)
    hold_down(walk_speed - 5)
    hold_right((walk_speed - 5) * (1 + random_starter))
    hold_up(walk_speed)
    press_a()
    for i in range(270):  # 350/270 Starter selected
        press_a()
        pyboy.tick()
    for i in range(20):
        press_b()
        pyboy.tick()
    spell_name(name)
    for i in range(280):  # 280
        press_a()
        pyboy.tick()


def to_rival_battle1():
    pass  # Finish the path from starter to challenge the rival


def save_values(tick_number):
    with open("debug.txt", "a") as f:
        testing = True
        add_test = False
        other_battle_type = pyboy.get_memory_value(53335)
        battle_type = pyboy.get_memory_value(53338)
        direction = pyboy.get_memory_value(49417)
        grass = pyboy.get_memory_value(49671)
        badges = pyboy.get_memory_value(54102)
        map_number = pyboy.get_memory_value(54110)
        sprite_walk = pyboy.get_memory_value(49664)
        secondY = pyboy.get_memory_value(9741)
        secondX = pyboy.get_memory_value(9742)
        second_delta_X = pyboy.get_memory_value(9744)
        second_delta_Y = pyboy.get_memory_value(9743)
        sprite_x_pos = pyboy.get_memory_value(49414)
        sprite_x_pos_delta = pyboy.get_memory_value(49413)
        sprite_y_pos = pyboy.get_memory_value(49412)
        sprite_y_pos_delta = pyboy.get_memory_value(49411)
        sprite_move_check = pyboy.get_memory_value(49672)
        move_status = pyboy.get_memory_value(49409)
        image_index = pyboy.get_memory_value(49410)
        animation_frame_counter = pyboy.get_memory_value(49416)
        have_map = pyboy.get_memory_value(54771)
        have_parcel = pyboy.get_memory_value(54797)
        gio_fight = pyboy.get_memory_value(55121)
        brock_fight = pyboy.get_memory_value(55125)
        misty_fight = pyboy.get_memory_value(55134)
        surge_fight = pyboy.get_memory_value(55155)
        erika_fight = pyboy.get_memory_value(55164)
        koga_fight = pyboy.get_memory_value(55186)
        blaine_fight = pyboy.get_memory_value(55194)
        sabrina_fight = pyboy.get_memory_value(55219)
        v_snorlax_fight = pyboy.get_memory_value(55256)
        c_snorlax_fight = pyboy.get_memory_value(55264)
        map_height = pyboy.get_memory_value(9748)
        map_width = pyboy.get_memory_value(9749)
        walking = pyboy.get_memory_value(10668)
        # map_script = pyboy.get_memory_value(11493)
        undocumented = []
        if direction == 0:
            word_direction = "Down"
        elif direction == 4:
            word_direction = "Up"
        elif direction == 8:
            word_direction = "Left"
        elif direction == 12:
            word_direction = "Right"
        for i in range(49418, 49423):
            undocumented.append(i)
        undocumented_appended = []
        for i in undocumented:
            undocumented_appended.append(pyboy.get_memory_value(i))

        player_input = []
        if len(pyboy.get_input()) > 0:
            for i in range(len(pyboy.get_input())):
                player_input.append(str(pyboy.get_input()[i]))
        print("Grass: ", grass, "128 while in, 0 while not")
        print(Fore.BLUE + "Move status: ", move_status)
        print("Image index: ", image_index)
        print("Animation Frame Counter: ", animation_frame_counter)
        print("Undocumented values: ", undocumented_appended)
        print("X =", sprite_x_pos, "\nY =", sprite_y_pos, "\nDeltaX =",
              sprite_x_pos_delta, "\nDeltaY =", sprite_y_pos_delta)
        print(Fore.GREEN + "Map number:  ", str(map_number) + "\t" + str(map_number_name[map_number]) + Fore.RESET)
        if testing:
            f.write("Map value\t\t" + str(map_number) + " " + str(map_number_name[map_number]))
            f.write("\nMove Status:\t\t" + str(move_status))
            f.write("\nImage index:\t\t" + str(image_index))
            f.write("\nAnimation Frame Counter:" + str(animation_frame_counter))
            f.write("\nUndocumented Valuse:\t" + str(undocumented_appended))
            if add_test:
                for i in range(49408, 49470):
                    if i % 10 == 0:
                        print(Fore.LIGHTGREEN_EX + str(i) + "=", pyboy.get_memory_value(i))
                    else:
                        print(Fore.LIGHTGREEN_EX + str(i) + "=", pyboy.get_memory_value(i), end=", ")
                    f.write("\n" + str(i) + "\n" + str(pyboy.get_memory_value(i)))
        print(Fore.RESET)
        print("_________________________"
              "Number of ticks in over world in control " + str(tick_number) +
              "_________________________")
        f.write("\nDirection: " + word_direction + " " + str(direction) +
                "\t\t| 0: down, 4: up, 8: left, 12: right\nPlayer input: " + str(player_input))
        f.write("\nReady to move:  " + str(sprite_move_check) + "\t| 0=ready to move")
        f.write("\nMovement:  " + str(sprite_walk) + "\t\t| Countdown")
        f.write("\n\nPossition X:  " + str(sprite_x_pos) + "\nDelta X:  " + str(sprite_x_pos_delta) +
                "\nPossition Y:  " + str(sprite_y_pos) + "\nDelta Y:  " + str(sprite_y_pos_delta))
        f.write("\nHeight:  " + str(map_height) +
                "\nWidth:  " + str(map_width))
        f.write("\nSecond X:  " + str(secondX) + "\nDelta X:  " + str(second_delta_X) +
                "\nSecond Y:  " + str(secondY) + "\nDelta Y:  " + str(second_delta_Y))
        f.write("\nPlayer in grass: " + str(grass) + "\t| 128 while in, 0 while not\n")
        f.write("Have the map:\t" + str(have_map))
        f.write("\nHave parcel:\t" + str(have_parcel))
        f.write("\nBadges:  " + str(badges) + "\t\t| Binary values\n")
        # f.write("Battle Type:  " + str(other_battle_type) + "\t\t| 0 not in battle, 1 wild PKMN, 2 Trainer\n")
        f.write("\n_________________________"
                "^Number of ticks in over world in control " + str(tick_number) +
                "^_________________________\n\n")


#     49408: picture ID (fixed, loaded at map init)
#     49409: movement status (0: uninitialized, 1: ready, 2: delayed, 3: moving)
#     49410: sprite image index (changed on update, $ff if off screen, includes facing direction,
#           progress in walking animation and a sprite-specific offset)
#     49411: Y screen position delta (-1,0 or 1; added to 49412 on each walking animation update)
#     49412: Y screen position (in pixels, always 4 pixels above grid which makes sprites
#           appear to be in the center of a tile)
#     49413: X screen position delta (-1,0 or 1; added to 49414 on each walking animation update)
#     49414: X screen position (in pixels, snaps to grid if not currently walking)
#     49415: intra-animation-frame counter (counting upwards to 4 until 49416 is incremented)
#     49416: animation frame counter (increased every 4 updates, hold four states (totalling to 16 walking frames)
#     49417: facing direction (0: down, 4: up, 8: left, $c: right)
#     49418 to 49423 are unudocumented (if used)


def battle_values():
    with open("debug.txt", "a") as f0:
        other_battle_type = pyboy.get_memory_value(53335)
        battle_type = pyboy.get_memory_value(53338)
        battle_turn = pyboy.get_memory_value(52437)
        party_quantity = pyboy.get_memory_value(53603)
        move1 = pyboy.get_memory_value(53276)
        move2 = pyboy.get_memory_value(53277)
        move3 = pyboy.get_memory_value(53278)
        move4 = pyboy.get_memory_value(53279)
        party1 = pyboy.get_memory_value(53603)
        party2 = pyboy.get_memory_value(53603)
        party3 = pyboy.get_memory_value(53603)
        party4 = pyboy.get_memory_value(53603)
        party5 = pyboy.get_memory_value(53603)
        party6 = pyboy.get_memory_value(53603)
        player_input = []
        print("Battle type: ", other_battle_type)
        if len(pyboy.get_input()) > 0:
            for i in range(len(pyboy.get_input())):
                player_input.append(str(pyboy.get_input()[i]))
        f0.write("Battle turn #:  " + str(battle_turn))
        f0.write("\nParty quantity:  " + str(party_quantity))
        f0.write("\nLead Pokemon:  " + str(party1) +
                 "\nMove 1:  " + str(move1) +
                 "\nMove 2:  " + str(move2) +
                 "\nMove 3:  " + str(move3) +
                 "\nMove 4:  " + str(move4))
        f0.write("\nParty 2:  " + str(party2))
        f0.write("\nParty 3:  " + str(party3))
        f0.write("\nParty 4:  " + str(party4))
        f0.write("\nParty 5:  " + str(party5))
        f0.write("\nParty 6:  " + str(party6))
        f0.write("\n_________________________^Number of turns in battle under your control " + str(battle_turn) +
                 "^_________________________\n\n")


def battle_decision(turns):
    test_battle = False
    lister = []
    list_of_actions = [hold_a, hold_a, hold_a, hold_up, hold_down]
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
    print(move_number[move1], "PP: ", move1_pp, "\t|", move_number[move2], "PP: ", move2_pp, "\t|",
          move_number[move3], "PP: ", move3_pp, "\t|", move_number[move4], "PP: ", move4_pp)
    moves = [move1, move2, move3, move4]  # List of all moves the pokemon knows 0=blank
    for move in moves:
        if len(move_number[move]) > 0:
            move_pool.append(move)
    if not test_battle:
        list_of_actions[random.randint(0, len(list_of_actions) - 1)](21)
    for i in range(29781, 29800):
        lister.append(pyboy.get_memory_value(i))
    print("Battle?: ", lister)
    xi = 100
    xj = 1
    xk = 1
    print(moves)
    pyboy.tick()
    # if len(move_pool) > 0:
    #     for i in range(0, xj):
    #         print("First\n", i)
    #         press_a()
    #         tick_pass(xi)
    #     for i in range(0, decided * xj):
    #         print("Second\n", i, decided)
    #         press_down()
    #         tick_pass(xi)
    #     for i in range(0, xk):
    #         print("Third\n", i)
    #         press_a()
    #         tick_pass(xi)
    # else:
    #     press_a()


    # if pyboy.get_memory_value(53293) > 0 and pyboy.get_memory_value(53276) != 0:
    #     press_a()
    # else:
    #     press_down()
    # press_a()


    # move_type = [0, 0]  # 0=status, 1=damage                      Replace a 0 with a 1
    # for i in range(0, battle_turn):  # Add weighted values for later in battle to not set up as much
    #     move_type.append(0)                                     # Replace a 0 with a 1
    # type_decided = move_type[random.randint(0, len(move_type) - 1)]  # Decide status/damage
    # damage_pool = []
    # status_pool = []
    # move_position = 0  # Used to determine where in the list of moves the move is
    # moves = []  # Appended moves position in line 0=top 1=second 2=third 3=fourth
    # d_moves = []
    # s_moves = []
    # if battle_turn not in turns:  # Attempt anything below this line in this function at your own risk
    #     for move in move_pool:
    #         if len(move_number[move]) < 1:
    #             break
    #         elif move_number[move] in damage_move:  # and len(move_number[move]) > 0
    #             print("Damage move: ", move, move_number[move])
    #             damage_pool.append(move)
    #             d_moves.append(move_position)
    #         elif move_number[move] in status_move:  # and len(move_number[move]) > 0
    #             print("Status move: ", move, move_number[move])
    #             status_pool.append(move)
    #             s_moves.append(move_position)
    #         print(move_position)
    #         move_position += 1
    #     if type_decided and len(damage_pool) > 0:  # if damage
    #         decision = random.randint(0, len(damage_pool) - 1)
    #         tell = 0
    #         for mov in d_moves:
    #             if decision == tell:
    #                 decided = mov
    #                 moves.append(move_pool[mov])
    #     if type_decided == 0 and len(status_pool) > 0:
    #         decision = random.randint(0, len(status_pool) - 1)
    #         tell = 0
    #         for mov in s_moves:
    #             if decision == tell:
    #                 decided = mov
    #                 moves.append(move_pool[mov])
    #     turns.append(battle_turn)
    #     print("Turns: ", turns, "Decided: ", decided)



# I can create a function that checks the map number value compared to the previous map number value you leave from
# and determine delta x and delta y between entrance x and y to destination x and y.
# Other finessing potential is checking if there is a direction you can go vs cannot


pyboy = PyBoy('Roms/Pokemon Red.gb')
increment = 0
for i in range(play_time):
    turn_count = []
    in_battle = pyboy.get_memory_value(53335)
    move1 = pyboy.get_memory_value(53276)
    move2 = pyboy.get_memory_value(53277)
    move3 = pyboy.get_memory_value(53278)
    move4 = pyboy.get_memory_value(53279)
    manager = pyboy.botsupport_manager()
    sprite0 = manager.sprite(0)
    if manager.sprite(0).on_screen and started is False:
        while started is False and sprite0.on_screen:
            sprite0 = manager.sprite(0)
            press_start()
            tick_pass(110)
        started = True
    if named is False and started:
        named = naming(named)
    if named and started and pathed_to_starters is False:
        starter_name = pokemon_name[random.randint(0, len(pokemon_name) - 1)]
        to_starters(starter_name)
        pathed_to_starters = True
    if named and started and pathed_to_starters:
        regain_control = True
    if regain_control and not in_battle:
        turns = []
        # save_values(controlled_ticks)
        overworld_move()
    while in_battle:
        battle_decision(turn_count)
        in_battle = pyboy.get_memory_value(53335)
    # if regain_control and in_battle:
    #     # battle_decision(turn_counter)
    #     if pyboy.get_memory_value(53293) > 0:
    #         print("Moves:  ", move1, move2, move3, move4)
    #         battle_values()
    #         press_a()
    #     else:
    #         battle_decision(turn_counter)
    pyboy.tick()
    check = appended
    appended = ""
    if regain_control:
        controlled_ticks += 1
    # for j in range(42392, 42402):
    #     appended += str(pyboy.get_memory_value(j)) + ": "
    # if check != appended:
    #     print(check, "\n" + Fore.GREEN + appended + Fore.RESET)
    # else:
    #     print("Same")
    # appended = str(pyboy.get_memory_value(42392))  This section was used to find different
    # memory values at the beginning of the game.
    # for j in range(16384, 17000):
    #     appended += str(pyboy.get_memory_value(j)) + ": "
    # if i % 50 == 0:
    #     increment += 1
    #     pil_image = pyboy.screen_image()
    #     pil_image.save('screenshot' + str(increment) + '.png')
    # print(str(i) + "\n", manager.tilemap_window())
    # print(manager.tilemap_background())
    # for j in range(24):
    #     print(manager.sprite(j), "\n", manager.sprite(j).tiles)
else:
    pyboy.stop(save=False)
    # pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
    # pyboy.tick()
    # pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)
# while not pyboy.tick():
#     pass
# pyboy.stop(save=False)
#
#