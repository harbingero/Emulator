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
# FIELDS_Commented = [
#   (None, "="), # "Native" endian.
#   (None, 'xxxx'), # 0x100-0x103 (entrypoint)
#   (None, '48x'), # 0x104-0x133 (nintendo logo)
#   ("title", '15s'), # 0x134-0x142 (cartridge title) (0x143 is shared with the cgb flag)
#   ("cgb", 'B'), # 0x143 (cgb flag)
#   ("new_licensee_code", 'H'), # 0x144-0x145 (new licensee code)
#   ("sgb", 'B'), # 0x146 (sgb `flag)
#   ("cartridge_type", 'B'), # 0x147 (cartridge type)
#   ("rom_size", 'B'), # 0x148 (ROM size)
#   ("ram_size", 'B'), # 0x149 (RAM size)
#   ("destination_code", 'B'), # 0x14A (destination code)
#   ("old_licensee_code", 'B'), # 0x14B (old licensee code)
#   ("mask_rom_version", 'B'), # 0x14C (mask rom version)
#   ("header_checksum", 'B'), # 0x14D (header checksum)
#   ("global_checksum", 'H'), # 0x14E-0x14F (global checksum)
# ]
# FIELDS = [
#   (None, "="),
#   (None, 'xxxx'),
#   (None, '48x'),
#   ("title", '15s'),
#   ("cgb", 'B'),
#   ("new_licensee_code", 'H'),
#   ("sgb", 'B'),
#   ("cartridge_type", 'B'),
#   ("rom_size", 'B'),
#   ("ram_size", 'B'),
#   ("destination_code", 'B'),
#   ("old_licensee_code", 'B'),
#   ("mask_rom_version", 'B'),
#   ("header_checksum", 'B'),
#   ("global_checksum", 'H'),
# ]







