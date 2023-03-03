import random
from pyboy import PyBoy
from pyboy import botsupport
from pyboy import WindowEvent
from pyboy import openai_gym
import pyboy.plugins

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
               "",
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
               "",
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
               "",
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
    print(move_number[move1], "PP: ", move1_pp, "|", move_number[move2], "PP: ", move2_pp, "|",
          move_number[move3], "PP: ", move3_pp, "|", move_number[move4], "PP: ", move4_pp)
    moves = [move1, move2, move3, move4]  # List of all moves the pokemon knows 0=blank
    for move in moves:
        if len(move_number[move]) > 0:
            move_pool.append(move)
    list_of_actions[random.randint(0, len(list_of_actions) - 1)](21)


def overworld_move():
    parcel = pyboy.get_memory_value(54797)
    map_number = pyboy.get_memory_value(54110)
    map_name = map_number_name[map_number]
    print(parcel)
    list_of_actions = [hold_a, hold_up, hold_down, hold_left, hold_right, hold_b]
    if map_name is "Pallet Town" and not parcel:
        list_of_actions.append(hold_up)
        list_of_actions.append(hold_up)
    if not parcel and map_name is "Oak's Lab" or "Mom's Room" or "Gary's House":
        list_of_actions.append(hold_down)
        list_of_actions.append(hold_down)
    if map_name is "Route 1" and not parcel:
        list_of_actions = [hold_a, hold_up, hold_left, hold_right, hold_b]
    if map_name is "Bedroom":
        list_of_actions = [hold_right, hold_up]
    list_of_actions[random.randint(0, len(list_of_actions) - 1)](21)


pyboy = PyBoy('Roms/Pokemon Red.gb')


def main(argv):
    list_of_actions = [hold_a, hold_up, hold_down, hold_left, hold_right, hold_b]
    while not pyboy.tick():
        move1 = pyboy.get_memory_value(53276)
        move2 = pyboy.get_memory_value(53277)
        move3 = pyboy.get_memory_value(53278)
        move4 = pyboy.get_memory_value(53279)
        turn_count = []
        in_battle = pyboy.get_memory_value(53335)
        while in_battle:
            print("Moves:  ", move1, move2, move3, move4)
            if pyboy.get_memory_value(53293) > 0 and pyboy.get_memory_value(53276) != 0:
                press_a()
            else:
                press_down()
            press_a()
            battle_decision(turn_count)
            in_battle = pyboy.get_memory_value(53335)
        overworld_move()
    pyboy.stop()


main(None)
