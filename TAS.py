import struct
import colorama
from colorama import Fore
import random
from pyboy import PyBoy
from pyboy import botsupport
from pyboy import WindowEvent
from pyboy import openai_gym
import pyboy.plugins
appended = ""
started = False
named = False
pathed_to_starters = False
starters = ["Charmander", "Squirtle", "Bulbasaur"]
play_time = 10000


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
    print("Up--------------------------", x)


def hold_down(x):
    pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_ARROW_DOWN)
    print("--Down----------------------", x)


def hold_left(x):
    pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
    print("------Left------------------", x)


def hold_right(x):
    pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
    print("----------Right-------------", x)


def hold_a(x):
    pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
    print("---------------A------------", x)


def hold_b(x):
    pyboy.send_input(WindowEvent.PRESS_BUTTON_B)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
    print("----------------B-----------", x)


def hold_start(x):
    pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)
    print("-----------------Start------", x)


def hold_select(x):
    pyboy.send_input(WindowEvent.PRESS_BUTTON_SELECT)
    tick_pass(x)
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_SELECT)
    print("----------------------Select", x)


def press_up():
    pyboy.send_input(WindowEvent.PRESS_ARROW_UP)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_UP)
    print("Up--------------------------")


def press_down():
    pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_DOWN)
    print("--Down----------------------")


def press_left():
    pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
    print("------Left------------------")


def press_right():
    pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
    print("----------Right-------------")


def press_a():
    pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
    print("---------------A------------")


def press_b():
    pyboy.send_input(WindowEvent.PRESS_BUTTON_B)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
    print("----------------B-----------")


def press_start():
    pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)
    print("-----------------Start------")


def press_select():
    pyboy.send_input(WindowEvent.PRESS_BUTTON_SELECT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_SELECT)
    print("----------------------Select")

# I can implement a spelling function later where I can create a list of a list of letters, then decide how many to the
# right/left and how many up/down the cursor needs to go.


def spell_Jesse():
    xi = 55  #55
    press_down()  # at J
    tick_pass(xi)
    press_a()  # J
    tick_pass(xi)
    press_select()  # Lower case
    tick_pass(xi)
    press_right()  # at k
    tick_pass(xi)
    press_right()  # at l
    tick_pass(xi)
    press_right()  # at m
    tick_pass(xi)
    press_right()  # at n
    tick_pass(xi)
    press_up()  # at e
    tick_pass(xi)
    press_a()  # e
    tick_pass(xi)
    press_down()  # at n
    tick_pass(xi)
    press_down()  # at w
    tick_pass(xi)
    press_left()  # at v
    tick_pass(xi)
    press_left()  # at u
    tick_pass(xi)
    press_left()  # at t
    tick_pass(xi)
    press_left()  # at s
    tick_pass(xi)
    press_a()  # s
    tick_pass(xi)
    press_a()  # s
    tick_pass(xi)
    press_right()  # at t
    tick_pass(xi)
    press_right()  # at u
    tick_pass(xi)
    press_right()  # at v
    tick_pass(xi)
    press_right()  # at w
    tick_pass(xi)
    press_up()  # at n
    tick_pass(xi)
    press_up()  # at e
    tick_pass(xi)
    press_a()  # e
    tick_pass(xi)
    press_start()  # Exit
    tick_pass(xi)


def spell_Rival():
    xi = 55  # 55
    press_right()  # at B
    tick_pass(xi)
    press_a()  # B
    tick_pass(xi)
    press_select()  # Lowercase
    tick_pass(xi)
    press_down()    # at k
    tick_pass(xi)
    press_right()  # at l
    tick_pass(xi)
    press_a()  # l
    tick_pass(xi)
    press_down()  # at u
    tick_pass(xi)
    press_a()  # u
    tick_pass(xi)
    press_up()  # at l
    tick_pass(xi)
    press_up()  # at c
    tick_pass(xi)
    press_right()  # at d
    tick_pass(xi)
    press_right()  # at e
    tick_pass(xi)
    press_a()  # e
    tick_pass(xi)
    press_start()  # Exit
    tick_pass(xi)


def name_starter():
    xi = 55  # 55
    press_right()  # at B
    tick_pass(xi)
    press_right()  # at C
    tick_pass(xi)
    press_right()  # at D
    tick_pass(xi)
    press_right()  # at E
    tick_pass(xi)
    press_right()  # at F
    tick_pass(xi)
    press_right()  # at G
    tick_pass(xi)
    press_a()  # G
    tick_pass(xi)
    press_select()  # Lowercase
    tick_pass(xi)
    press_down()    # at p
    tick_pass(xi)
    press_left()  # at o
    tick_pass(xi)
    press_a()  # o
    tick_pass(xi)
    press_a()  # o
    tick_pass(xi)
    press_left()  # at n
    tick_pass(xi)
    press_left()  # at m
    tick_pass(xi)
    press_up()  # at d
    tick_pass(xi)
    press_a()  # d
    tick_pass(xi)
    press_left()  # at c
    tick_pass(xi)
    press_left()  # at b
    tick_pass(xi)
    press_a()  # b
    tick_pass(xi)
    press_right()  # at c
    tick_pass(xi)
    press_right()  # at d
    tick_pass(xi)
    press_right()  # at e
    tick_pass(xi)
    press_right()  # at f
    tick_pass(xi)
    press_down()  # at o
    tick_pass(xi)
    press_a()  # o
    tick_pass(xi)
    press_down()  # at x
    tick_pass(xi)
    press_right()  # at y
    tick_pass(xi)
    press_a()  # y
    tick_pass(xi)
    press_start()  # Exit
    tick_pass(xi)


def naming(fun_named):
    xi = 120
    xj = 60
    for h in range(25):  # 25
        press_b()
        tick_pass(xj)
    press_a()
    tick_pass(xi)
    spell_Jesse()  # Spell Jesse
    for k in range(11):  # 11
        press_b()
        tick_pass(xj)
    tick_pass(xi)
    press_a()
    tick_pass(xi)
    spell_Rival()  # Spell Rival
    for c in range(12):  # 12
        press_b()
        tick_pass(xj)
    fun_named = True
    return fun_named


def to_starters():
    walk_speed = 21
    transition = 40
    oak_walk = 500
    random_starter = random.randint(0, 2)
    tick_pass(250)
    hold_right(walk_speed * 2)
    hold_up(walk_speed * 4)
    hold_right(walk_speed * 2)
    tick_pass(transition)  # Out of room
    hold_down(walk_speed * 5)
    hold_left(walk_speed * 4)
    hold_down(walk_speed)
    tick_pass(transition)  # Out of house
    hold_right(walk_speed * 5)
    hold_up(walk_speed * 5)
    for i in range(1250):  # In grass
        press_b()
        pyboy.tick()
    # tick_pass(oak_walk)
    hold_down(walk_speed - 5)
    hold_right((walk_speed - 3) * (1 + random_starter))
    hold_up(walk_speed)
    press_a()
    print(starters[random_starter], random_starter)
    for i in range(350):  # Starter selected
        press_a()
        pyboy.tick()
    name_starter()
    for i in range(235):
        press_a()
        pyboy.tick()



pyboy = PyBoy('Roms/Pokemon Red.gb')
increment = 0
for i in range(play_time):
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
        to_starters()
        pathed_to_starters = True
    pyboy.tick()
    check = appended
    appended = ""
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
