import struct
import colorama
from colorama import Fore
from pyboy import PyBoy
from pyboy import WindowEvent
appended = ""

pyboy = PyBoy('Roms/Pokemon Red.gb')
increment = 0
game_start = "Game_Start.png"
new_game = "New_Game.png"

for i in range(2000):
    pyboy.tick()
    check = appended
    appended = ""
    for j in range(16300, 16400):
        appended += str(pyboy.get_memory_value(j)) + ": "
    if check != appended:
        print(check, "\n" + Fore.GREEN + appended + Fore.RESET)
    else:
        print("Same")
    # if i % 50 == 0:
    #     increment += 1
    #     pil_image = pyboy.screen_image()
    #     pil_image.save('screenshot' + str(increment) + '.png')
else:
    # pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
    # pyboy.tick()
    # pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)
    pyboy.stop(save=False)
# while not pyboy.tick():
#     pass
# pyboy.stop(save=False)
#
#
