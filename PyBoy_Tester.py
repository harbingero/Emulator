from pyboy import PyBoy, WindowEvent
import re


map_number_name = ["Pallet Town",  # 0
                   "Viridian City",
                   "Pewter City",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",  # 10
                   "",
                   "Route 1",
                   "Route 2",
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
                   "Route 22",
                   "",
                   "",
                   "",
                   "Mom's Room",
                   "Bedroom",
                   "Gary's House",
                   "Oak's Lab",  # 40
                   "Viridian City Pokecenter",
                   "Viridian City Pokemart",
                   "Viridian City South House",
                   "Viridian City North House",
                   "",
                   "",
                   "Forest Post-house",
                   "",
                   "",
                   "Forest Pre-house",  # 50
                   "Viridian Forest",
                   "",
                   "",
                   "Brock's Gym",
                   "",
                   "Pewter City Pokemart",
                   "",
                   "Pewter City Pokecenter",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""]
actions = {}
overworld = False
game_flag = "No_Parcel"
pyboy = PyBoy('Roms/Pokemon Red.gb')
manager = pyboy.botsupport_manager()
parcel_item_slot_1 = 70
item_memory_values = [54046,
                      54048,  # 2
                      54050,
                      54052,  # 4
                      54054,
                      54056,  # 6
                      54058,
                      54060,  # 8
                      54062,
                      54064,  # 10
                      54066,
                      54068,  # 12
                      54070,
                      54072,  # 14
                      54074,
                      54076,  # 16
                      54078,
                      54080,  # 18
                      54082,
                      54084]
item_name_list = ["",
                  "",
                  "",
                  "",
                  "Pokeball",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",  # 10
                  "Antidote",
                  "Burn_Heal",
                  "",
                  "",
                  "Paralyze_Heal",
                  "",
                  "",
                  "",
                  "",
                  "Potion",  # 20
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
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",  # 40
                  "",
                  "",
                  "",
                  "",
                  "",
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
                  "Oak's_Parcel",  # 70
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
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",  # 180
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",  # 190
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",  # 200
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",  # 210
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",  # 220
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",  # 230
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",  # 240
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",  # 250
                  "",
                  "",
                  "",
                  "",
                  "Empty_Slot"]

while not pyboy.tick():
    back_pack_numbers = []
    for i in item_memory_values:
        back_pack_numbers.append(pyboy.get_memory_value(i))
    print(back_pack_numbers)
    map_number = pyboy.get_memory_value(54110)
    sprite0 = manager.sprite(0).on_screen
    parcel = pyboy.get_memory_value(54797)
    if game_flag == "No_Parcel" and parcel == parcel_item_slot_1:
        game_flag = "Parcel"
    if game_flag == "Parcel":  # Need to add another check for if parcel is in pack
        game_flag = "Pokedex"
    print(map_number)
    if map_number > 0 and sprite0:
        overworld = True
    if len(pyboy.get_input()) > 0 and overworld and sprite0:
        for i in pyboy.get_input():
            i = re.sub("RELEASE_BUTTON", "R", str(i))
            i = re.sub("PRESS_BUTTON", "P", str(i))
            i = re.sub("PRESS_ARROW", "P", str(i))
            i = re.sub("RELEASE_ARROW", "P", str(i))
            i = re.sub("WINDOW_UNFOCUS", "", str(i))
            i = re.sub("WINDOW_FOCUS", "", str(i))
            stringer = map_number_name[map_number] + "_" + str(i) + "_" + game_flag
            if len(i) == 0:
                break
            if stringer not in actions:
                actions[stringer] = 1
            else:
                actions[stringer] += 1
    print(actions)
    pass
pyboy.stop()
