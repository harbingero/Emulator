import re
file = "Pokemon_List.txt"
removal = ["Rock",
           "Electric",
           "Ice",
           "Grass",
           "Fire",
           "Water",
           "Ghost",
           "Dragon",
           "Normal",
           "Psychic",
           "Dark",
           "Flying",
           "Fighting",
           "Bug",
           "Fairy",
           "Ground",
           "Poison",
           "Steel"]
appended = []

with open(file, "r") as f1:
    for line in f1:
        items = line.split()
        for item in items:
            if re.search("^#", item):
                print("passed ^#: ", item)
                continue
            if item in removal:
                print("In removal: ", item)
                continue
            if item in appended:
                continue
            appended.append(item)

print(appended)
