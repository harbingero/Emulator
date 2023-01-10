import struct
from pyboy import PyBoy
from pyboy import WindowEvent
appended = ""

pyboy = PyBoy('Roms/Pokemon Red.gb')

for i in range(2000):
    pyboy.tick()
    check = appended
    appended = ""
    for j in range(10000):
        appended += str(pyboy.get_memory_value(j)) + ": "
    if check != appended:
        print(check, "\n" + appended)
    else:
        print("Same")
else:
    # pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
    # pyboy.tick()
    # pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)
    #
    # pil_image = pyboy.screen_image()
    # pil_image.save('screenshot.png')
    pyboy.stop(save=False)
# while not pyboy.tick():
#     pass
# pyboy.stop(save=False)
#
#
