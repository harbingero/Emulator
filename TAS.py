import struct
import colorama
from colorama import Fore
from pyboy import PyBoy
from pyboy import botsupport
from pyboy import WindowEvent
from pyboy import openai_gym
import pyboy.plugins
appended = ""
started = False
to_starters = False

def tick_pass(number):
    if number <= 0:
        return None
    while number > 0:
        # print("Tick_Pass")
        pyboy.tick()
        number -= 1
#  A future potential improvement on the code would be to append button presses to show what inputs it's getting.
#  I'm sure I would have to modify each of these functions to tick elsewhere.  This would allow multiple inputs at once.
def press_up():
    print("Up-------------")
    pyboy.send_input(WindowEvent.PRESS_ARROW_UP)
    pyboy.tick()
    pyboy.send_input(WindowEvent.PRESS_ARROW_UP)


def press_down():
    print("--Down---------")
    pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
    pyboy.tick()
    pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)

def press_left():
    print("------Left-----")
    pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)

def press_right():
    print("----------Right")
    pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)

def press_a():
    print(".\t.\t.\tPressed A")
    pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)

def press_b():
    print(".\t.\t.\tPressed B")
    pyboy.send_input(WindowEvent.PRESS_BUTTON_B)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)

def press_start():
    print(".\t.\t.\tPressed Start")
    pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)

def press_select():
    print(".\t.\t.\tPressed Select")
    pyboy.send_input(WindowEvent.PRESS_BUTTON_SELECT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_SELECT)

pyboy = PyBoy('Roms/Pokemon Red.gb')
increment = 0
for i in range(5000):
    manager = pyboy.botsupport_manager()
    sprite0 = manager.sprite(0)
    if manager.sprite(0).on_screen and started is False:
        while started is False and sprite0.on_screen:
            sprite0 = manager.sprite(0)
            press_start()
            tick_pass(110)
        started = True
    if to_starters is False and started is True:
        while not sprite0.on_screen and to_starters is False:
            sprite0 = manager.sprite(0)
            press_b()
            tick_pass(5)
            press_a()
            press_down()
            press_a()
            press_right()
            press_right()
            press_right()
            press_right()
            press_up()
            press_a()
            press_down()
            press_down()
            press_left()
            press_left()
            press_left()
            press_left()
            press_a()
            press_a()
            press_right()
            press_right()
            press_right()
            press_right()
            press_up()
            press_up()
            press_a()
            press_start()
    pyboy.tick()
    check = appended
    appended = ""
    # for j in range(42392, 42402):
    #     appended += str(pyboy.get_memory_value(j)) + ": "
    # if check != appended:
    #     print(check, "\n" + Fore.GREEN + appended + Fore.RESET)
    # else:
    #     print("Same")
    # appended = str(pyboy.get_memory_value(42392))  This section was used to find different memory values at the begining of the game.
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
