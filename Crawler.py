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
urls = ["https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Ivysaur_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Venusaur_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Charmander_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Charmeleon_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Charizard_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Squirtle_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Wartortle_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Blastoise_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Caterpie_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Metapod_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Butterfree_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Weedle_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Kakuna_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Beedrill_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Pidgey_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Pidgeotto_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Pidgeot_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Rattata_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Raticate_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Spearow_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Fearow_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Ekans_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Arbok_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Pikachu_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Raichu_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Sandshrew_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Sandslash_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Nidoran♀_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Nidorina_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Nidoqueen_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Nidoran♂_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Nidorino_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Nidoking_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Clefairy_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Clefable_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Vulpix_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Ninetales_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Jigglypuff_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Wigglytuff_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Zubat_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Golbat_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Oddish_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Gloom_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Vileplume_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Paras_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Parasect_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Venonat_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Venomoth_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Diglett_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Dugtrio_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Meowth_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Persian_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Psyduck_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Golduck_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Mankey_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Primeape_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Growlithe_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Arcanine_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Poliwag_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Poliwhirl_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Poliwrath_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Abra_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Kadabra_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Alakazam_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Machop_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Machoke_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Machamp_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Bellsprout_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Weepinbell_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Victreebel_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Tentacool_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Tentacruel_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Geodude_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Graveler_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Golem_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Ponyta_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Rapidash_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Slowpoke_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Slowbro_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Magnemite_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Magneton_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Farfetch'd_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Doduo_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Dodrio_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Seel_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Dewgong_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Grimer_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Muk_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Shellder_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Cloyster_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Gastly_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Haunter_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Gengar_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Onix_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Drowzee_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Hypno_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Krabby_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Kingler_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Voltorb_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Electrode_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Exeggcute_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Exeggutor_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Cubone_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Marowak_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Hitmonlee_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Hitmonchan_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Lickitung_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Koffing_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Weezing_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Rhyhorn_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Rhydon_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Chansey_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Tangela_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Kangaskhan_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Horsea_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Seadra_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Goldeen_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Seaking_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Staryu_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Starmie_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Mr. Mime_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Scyther_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Jynx_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Electabuzz_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Magmar_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Pinsir_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Tauros_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Magikarp_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Gyarados_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Lapras_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Ditto_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Eevee_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Vaporeon_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Jolteon_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Flareon_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Porygon_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Omanyte_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Omastar_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Kabuto_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Kabutops_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Aerodactyl_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Snorlax_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Articuno_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Zapdos_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Moltres_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Dratini_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Dragonair_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Dragonite_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Mewtwo_(Pokémon)/Generation_I_learnset#By_leveling_up",
        "https://bulbapedia.bulbagarden.net/wiki/Mew_(Pokémon)/Generation_I_learnset#By_leveling_up"]
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

for url in urls:
    lmove_count = 0
    levels = []
    move = []
    tm_count = 1
    tm = False
    transfer = False
    lmove = {}
    tmove = "tmoves_"+pokedex[pokedex_number].lower()+" = ["
    hmove = "hmoves_"+pokedex[pokedex_number].lower()+" = ["
    if count < 10:
        html = requests.get(url).content
        unicode_str = html.decode('utf8')
        encoded_str = unicode_str.encode("ascii", 'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all("span")
        for item in a_text:
            item = re.sub("<span", "", str(item))
            item = re.sub("</span>", "", str(item))
            item = re.sub("^\s", "", item)
            item = re.sub("style=\"", "", item)
            item = re.sub("display:", "", item)
            item = re.sub("color:", "", item)
            item = re.sub("#000;\">", "", item)
            item = re.sub("none\">", "", item)
            item = re.sub("#FFFFFF\">", "", item)
            item = re.sub("}}", "", item)
            # print(item)
            if item not in removal and not tm:
                if item != tm_and_hm:
                    # print(item)
                    if len(item) == 2 and item != "00":
                        levels.append(item)
                    if item in move_number:
                        move.append(item)
                if item == tm_and_hm:
                    tm = True
            if tm and not transfer:
                if item not in removal and item != tm_and_hm:
                    if item != transfer_tag:
                        if item not in hms:
                            # print("TM/HM: ", item)
                            if item in move_number:
                                tmove = tmove+"\""+item+"\", "
                        if item in hms:
                            hmove = hmove+item+","
                    if item == transfer_tag:
                        transfer = True
    for level in levels:
        if level in lmove:
            lmove[level].append(move[lmove_count])
        if level not in lmove:
            lmove[level] = [move[lmove_count]]
        lmove_count += 1
    tmove = tmove+"]"
    hmove = hmove+"]"
    hmove = re.sub(",]", "]", hmove)
    tmove = re.sub(", ]", "]", tmove)
    print("lmove_"+pokedex[pokedex_number]+" = ", end="")
    print(lmove)
    print(tmove)
    print(hmove)
    pokedex_number += 1
    count += 1
    if count > 11:
        break
    # soup = BeautifulSoup(url, 'html.parser')
    # for tag in soup.find_all('table'):
    #     if count < 2:
    #         print(tag.text)
    #         count += 1
