import struct
from pyboy import PyBoy
from pyboy import WindowEvent

pyboy = PyBoy('Roms/Pokemon Red.gb')

for i in range(2000):
    pyboy.tick()
else:
    pyboy.stop(save=False)
# while not pyboy.tick():
#     pass
# pyboy.stop(save=False)
#
#
# pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
# pyboy.tick()
# pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)
#
# pil_image = pyboy.screen_image()
# pil_image.save('screenshot.png')