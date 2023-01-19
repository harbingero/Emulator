import struct
import colorama
from colorama import Fore
from pyboy import PyBoy
from pyboy import botsupport
from pyboy import WindowEvent
from pyboy import openai_gym
import pyboy.plugins
appended = ""

pyboy = PyBoy('Roms/Pokemon Red.gb')
increment = 0
game_start = "Game_Start.png"
new_game = "New_Game.png"
for i in range(5000):
    pyboy.tick()
    check = appended
    appended = ""
    manager = pyboy.botsupport_manager()
    print(manager.sprite(0))
    for j in range(42392, 42402):
        appended += str(pyboy.get_memory_value(j)) + ": "
    if check != appended:
        print(check, "\n" + Fore.GREEN + appended + Fore.RESET)
    else:
        print("Same")
    # appended = str(pyboy.get_memory_value(42392))  This section was used to find different memory values at the begining of the game.
    # for j in range(16384, 17000):
    #     appended += str(pyboy.get_memory_value(j)) + ": "
    # if i % 50 == 0:
    #     increment += 1
    #     pil_image = pyboy.screen_image()
    #     pil_image.save('screenshot' + str(increment) + '.png')
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
