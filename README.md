# Emulator
Building an emulator in python to do other python-ey things.


[https://www.inspiredpython.com/course/game-boy-emulator/game-boy-emulator-writing-the-z80-disassembler](https://www.inspiredpython.com/course/game-boy-emulator/let-s-write-a-game-boy-emulator-in-python)
https://hackaday.io/project/176113-picarts-gpio-rom-carts/log/186621-controlling-emulators-with-python
https://stackoverflow.com/questions/32064844/python-interact-with-dolphin-emulator
https://gbdev.io/pandocs/The_Cartridge_Header.html
https://www.inspiredpython.com/course/testing-with-hypothesis/testing-your-python-code-with-hypothesis

Sites to give help:

I have ended up using https://github.com/Baekalfen/PyBoy/blob/master/README.md pyboy program.  This can allow me to make checks when I want.  And read states in the game.

Using https://datacrystal.romhacking.net/wiki/Pok%C3%A9mon_Red/Blue:RAM_map, this will help finding values in memory.  There'll be a section about half way down that will be useful to checking where we are in the run called Event Flags.  I can use this to tell it which set of instructions to give it.  This site, https://glitchcity.wiki/The_Big_HEX_List, will give me hex values for specific pokemon and trainers.

Maps can be downloaded in the furture from https://tcrf.net/Development:Pok%C3%A9mon_Red_and_Blue/Unused_Maps.
