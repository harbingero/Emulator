import urllib.request
import requests
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import time
import re

transfer_tag = "class=\"mw-headline\" id=\"By_transfer_from_another_generation\">By <a href=\"/wiki/Transfer\" title=\"Transfer\">transfer</a> from another generation"
tm_and_hm = "id=\"By_TM/HM\">"
pokedex = ['Bulbasaur',
           'Ivysaur',
           'Venusaur',
           'Charmander',
           'Charmeleon',
           'Charizard',
           'Squirtle',
           'Wartortle',
           'Blastoise',
           'Caterpie',
           'Metapod',
           'Butterfree',
           'Weedle',
           'Kakuna',
           'Beedrill',
           'Pidgey',
           'Pidgeotto',
           'Pidgeot',
           'Rattata',
           'Raticate',
           'Spearow',
           'Fearow',
           'Ekans',
           'Arbok',
           'Pikachu',
           'Raichu',
           'Sandshrew',
           'Sandslash',
           'Nidoran♀',
           'Nidorina',
           'Nidoqueen',
           'Nidoran♂',
           'Nidorino',
           'Nidoking',
           'Clefairy',
           'Clefable',
           'Vulpix',
           'Ninetales',
           'Jigglypuff',
           'Wigglytuff',
           'Zubat',
           'Golbat',
           'Oddish',
           'Gloom',
           'Vileplume',
           'Paras',
           'Parasect',
           'Venonat',
           'Venomoth',
           'Diglett',
           'Dugtrio',
           'Meowth',
           'Persian',
           'Psyduck',
           'Golduck',
           'Mankey',
           'Primeape',
           'Growlithe',
           'Arcanine',
           'Poliwag',
           'Poliwhirl',
           'Poliwrath',
           'Abra',
           'Kadabra',
           'Alakazam',
           'Machop',
           'Machoke',
           'Machamp',
           'Bellsprout',
           'Weepinbell',
           'Victreebel',
           'Tentacool',
           'Tentacruel',
           'Geodude',
           'Graveler',
           'Golem',
           'Ponyta',
           'Rapidash',
           'Slowpoke',
           'Slowbro',
           'Magnemite',
           'Magneton',
           "Farfetch'd",
           'Doduo',
           'Dodrio',
           'Seel',
           'Dewgong',
           'Grimer',
           'Muk',
           'Shellder',
           'Cloyster',
           'Gastly',
           'Haunter',
           'Gengar',
           'Onix',
           'Drowzee',
           'Hypno',
           'Krabby',
           'Kingler',
           'Voltorb',
           'Electrode',
           'Exeggcute',
           'Exeggutor',
           'Cubone',
           'Marowak',
           'Hitmonlee',
           'Hitmonchan',
           'Lickitung',
           'Koffing',
           'Weezing',
           'Rhyhorn',
           'Rhydon',
           'Chansey',
           'Tangela',
           'Kangaskhan',
           'Horsea',
           'Seadra',
           'Goldeen',
           'Seaking',
           'Staryu',
           'Starmie',
           'Mr. Mime',
           'Scyther',
           'Jynx',
           'Electabuzz',
           'Magmar',
           'Pinsir',
           'Tauros',
           'Magikarp',
           'Gyarados',
           'Lapras',
           'Ditto',
           'Eevee',
           'Vaporeon',
           'Jolteon',
           'Flareon',
           'Porygon',
           'Omanyte',
           'Omastar',
           'Kabuto',
           'Kabutops',
           'Aerodactyl',
           'Snorlax',
           'Articuno',
           'Zapdos',
           'Moltres',
           'Dratini',
           'Dragonair',
           'Dragonite',
           'Mewtwo',
           'Mew']
hms = ["Fly",
       "Surf",
       "Strength",
       "Cut",
       "Flash"]
urls_pokemon = ['https://bulbapedia.bulbagarden.net/wiki/Beedrill_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Clefairy_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Clefable_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Jigglypuff_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Wigglytuff_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Poliwag_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Poliwhirl_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Poliwrath_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Geodude_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Graveler_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Golem_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Slowpoke_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Slowbro_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Drowzee_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Hypno_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Krabby_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Kingler_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Hitmonchan_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Lickitung_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Mr._Mime_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Jynx_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Electabuzz_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Mewtwo_(Pokémon)/Generation_I_learnset#By_leveling_up',
                'https://bulbapedia.bulbagarden.net/wiki/Mew_(Pokémon)/Generation_I_learnset#By_leveling_up']

move_number = ["Pound",
               "Karate Chop",
               "Double Slap",
               "Comet Punch",
               "Mega Punch",
               "Pay Day",
               "Fire Punch",
               "Ice Punch",
               "Thunder Punch",
               "Scratch",  # 10
               "Vicegrip",
               "Guillotine",
               "Razor Wind",
               "Swords Dance",
               "Cut",
               "Gust",
               "Wing Attack",
               "Whirlwind",
               "Fly",
               "Bind",  # 20
               "Slam",
               "Vine Whip",
               "Stomp",
               "Double Kick",
               "Mega Kick",
               "Jump Kick",
               "Rolling Kick",
               "Sand-Attack",
               "Headbutt",
               "Horn Attack",  # 30
               "Fury Attack",
               "Horn Drill",
               "Tackle",
               "Body Slam",
               "Wrap",
               "Take Down",
               "Thrash",
               "Double-Edge",
               "Tail Whip",
               "Poison Sting",  # 40
               "Twineedle",
               "Pin Missle",
               "Leer",
               "Bite",
               "Growl",  # 45
               "Roar",
               "Sing",
               "Supersonic",
               "SonicBoom",
               "Disable",  # 50
               "Acid",
               "Ember",
               "Flamethrower",
               "Mist",
               "Water Gun",
               "Hydro Pump",
               "Surf",
               "Ice Beam",
               "Blizzard",
               "Psybeam",  # 60
               "BubbleBeam",
               "Aurora Beam",
               "Hyper Beam",
               "Peck",
               "Drill Peck",
               "Submission",
               "Low Kick",
               "Counter",
               "Seismic Toss",
               "Strength",  # 70
               "Absorb",
               "Mega Drain",
               "Leech Seed",
               "Growth",
               "Razor Leaf",
               "SolarBeam",
               "PoisonPowder",
               "Stun Spore",
               "Sleep Powder",
               "Petal Dance",  # 80
               "String Shot",
               "Dragon Rage",
               "Fire Spin",
               "ThunderShock",
               "Thunderbolt",
               "Thunder Wave",
               "Thunder",
               "Rock Throw",
               "Earthquake",
               "Fissure",  # 90
               "Dig",
               "Toxic",
               "Confusion",
               "Hypnosis",
               "Meditate",
               "Agility",
               "Quick Attack",
               "Rage",
               "Teleport",  # 100
               "Night Shade",
               "Mimic",
               "Screech",
               "Double Team",
               "Recover",
               "Harden",
               "Minimize",
               "SmokeScreen",
               "Confuse Ray",
               "Withdraw",  # 110
               "Barrier",
               "Light Screen",
               "Haze",
               "Reflect",
               "Focus Energy",
               "Bide",
               "Metronome",
               "Mirror Move",
               "Selfdestruct",
               "Egg Bomb",  # 120
               "Lick",
               "Smog",
               "Sludge",
               "Bone Club",
               "Fire Blast",
               "Waterfall",
               "Clamp",
               "Swift",
               "Skull Bash",
               "Spike Cannon",  # 130
               "Constrict",
               "Amnesia",
               "Kenesis",
               "Softboiled",
               "Hi Jump Kick",
               "Glare",
               "Dream Eater",
               "Poison Gas",
               "Barrage",
               "Leech Life",  # 140
               "Lovely Kiss",
               "Sky Attack",
               "Sky Attack",
               "Transform",
               "Bubble",
               "Dizzy Punch",
               "Spore",
               "Flash",
               "Psywave",
               "Splash",  # 150
               "Acid Armor",
               "Crabhammer",
               "Explosion",
               "Fury Swipes",
               "Bonemerang",
               "Rest",
               "Rock Slide",
               "Hyper Fang",
               "Sharpen",
               "Conversion",  # 160
               "Tri Attack",
               "Super Fang",
               "Slash",
               "Substitute",
               "Struggle",
               "",
               "",
               "",
               "",
               "",  # 170
               ""]
removal = ["II",
           "III",
           "IV",
           "V",
           "VI",
           "VII",
           "VIII",
           "IX",
           "Level",
           "Move",
           "Type",
           "Power",
           "Accuracy",
           "PP",
           "STAB",
           "Gen.",
           "Pwr.",
           "Acc.",
           "class=\"mw-headline\"id=\"By_leveling_up\">By<ahref=\"/wiki/Level\"title=\"Level\">levelingup</a>",
           "class=\"mw-headline\"id=\"By_TM.2FHM\">By<ahref=\"/wiki/TM\"title=\"TM\">TM</a>/<ahref=\"/wiki/HM\"title=\"HM\">HM</a>",
           "TM"]
pokedex_number = 0

url1 = r"https://bulbapedia.bulbagarden.net/wiki/"
url2 = r"_(Pokémon)/Generation_I_learnset#By_leveling_up"
final_url = []
count = 0

# for pokemon in pokedex:
#     throw = pokemon + url2
#     appendable = url1 + throw
#     print(appendable)
#     appendable = appendable.encode('utf-8')
#     final_url.append(appendable)


# for url in urls:
#     try:
#         pokemon = re.sub(url1, "", url)
#         pokemon = re.sub(url2, "", url)
#         print("Removed: ", url1, url2, "\nPokemon: ", pokemon)
#         lmove_count = 0
#         levels = []
#         move = []
#         tm_count = 1
#         tm = False
#         transfer = False
#         lmove = {}
#         tmove = "tmoves_" + pokedex[pokedex_number].lower() + " = ["
#         hmove = "hmoves_" + pokedex[pokedex_number].lower() + " = ["
#         if count < 1:  # 25
#             html = requests.get(url).content
#             unicode_str = html.decode('utf8')
#             encoded_str = unicode_str.encode("ascii", 'ignore')
#             news_soup = BeautifulSoup(encoded_str, "html.parser")
#             a_text = news_soup.find_all("span")
#             for item in a_text:
#                 item = re.sub("<span", "", str(item))
#                 item = re.sub("</span>", "", str(item))
#                 item = re.sub("^\s", "", item)
#                 item = re.sub("style=\"", "", item)
#                 item = re.sub("display:", "", item)
#                 item = re.sub("color:", "", item)
#                 item = re.sub("#000;\">", "", item)
#                 item = re.sub("none\">", "", item)
#                 item = re.sub("#FFFFFF\">", "", item)
#                 item = re.sub("}}", "", item)
#                 print(item)
#                 if item not in removal and not tm:
#                     if item != tm_and_hm:
#                         # print(item)
#                         if len(item) == 2 and item != "00":
#                             levels.append(item)
#                         if item in move_number:
#                             move.append(item)
#                     if item == tm_and_hm:
#                         tm = True
#                 if tm and not transfer:
#                     if item not in removal and item != tm_and_hm:
#                         if item != transfer_tag:
#                             if item not in hms:
#                                 # print("TM/HM: ", item)
#                                 if item in move_number:
#                                     tmove = tmove + "\"" + item + "\", "
#                             if item in hms:
#                                 hmove = hmove + "\"" + item + "\","
#                         if item == transfer_tag:
#                             transfer = True
#         for level in levels:
#             if level in lmove:
#                 lmove[level].append(move[lmove_count])
#             if level not in lmove:
#                 lmove[level] = [move[lmove_count]]
#             lmove_count += 1
#         tmove = tmove + "]"
#         hmove = hmove + "]"
#         hmove = re.sub(",]", "]", hmove)
#         tmove = re.sub(", ]", "]", tmove)
#         print("lmove_" + pokedex[pokedex_number].lower() + " = ", end="")
#         print(lmove)
#         print(tmove)
#         print(hmove)
#         pokedex_number += 1
#         count += 1
#     except:
#         print(url)
#         pokedex_number += 1
#         count += 1
#     # soup = BeautifulSoup(url, 'html.parser')
#     # for tag in soup.find_all('table'):
#     #     if count < 2:
#     #         print(tag.text)
#     #         count += 1


url = "https://bulbapedia.bulbagarden.net/wiki/List_of_moves"
appender = []

html = requests.get(url).content
unicode_str = html.decode('utf8')
encoded_str = unicode_str.encode("ascii", 'ignore')
news_soup = BeautifulSoup(encoded_str, "html.parser")
a_text = news_soup.find_all("tr")
for a in a_text:
    appender.append(a)
for i in appender:
    print(i)