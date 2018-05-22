import os
import pprint
import operator


def crop(word):
    if 'Hi-Jump' not in word and 'X-Ray' not in word and 'C-Shaped' not in word:
        word = word.split("-")
        word = word[0]
    word = word.replace(",", "")
    word = word.replace('"', '')
    word = word.lstrip()
    word = word.rstrip()
    return word


def sort_dictionary(unsorted_locations):
    sorted_locations = sorted(unsorted_locations.items(), key=operator.itemgetter(1))
    return sorted_locations


def get_transition(location_a, location_b):
    transition = location_a + " => " + location_b
    return transition


pp = pprint.PrettyPrinter(indent=0)

os.getcwd()

locations = {}

transitions = {}

items = ['Bow', "Silver Arrows Upgrade", "Hookshot", "Fire Rod", "Ice Rod", "Bombos", "Ether", "Quake", "Lamp",
         "Hammer", "Book Of Mudora", "Cane Of Somaria", "Magic Mirror", "Pegasus Boots", "Progressive Glove",
         "Flippers", "Flute", "Magic Cape", "Cane of Byrna", "Varia Suit", "Gravity Suit", "Morphing Ball", "Bombs",
         "Charge Beam", "Ice Beam", "Wave Beam", "Spazer", "Plasma Beam", "Hi-Jump Boots", "Space Jump", "Spring Ball",
         "Screw Attack", "Speed Booster", "Grappling Beam", "Power Bomb", "Super Missile"]

for root, dirs, files in os.walk("spoilerLogs"):
    file_count = len(files)
    for file in files:
        if file.endswith(".txt"):
            openFile = open(os.path.join(root, file))
            current_location = None
            playthrough = False
            for line in openFile:
                part = line.split(":")
                if not playthrough:
                    next
                else:
                    try:
                        if crop(part[1]) in items:
                            key = crop(part[0])
                            if current_location:
                                previous_location = current_location
                                current_location = key
                                current_transition = get_transition(previous_location, current_location)
                                if current_transition in transitions:
                                    transitions[current_transition] += 1
                                else:
                                    transitions[current_transition] = 1
                            current_location = key
                            if key in locations:
                                locations[key] += 1
                            else:
                                locations[key] = 1
                    except IndexError:
                        pass
                if crop(part[0]) == 'playthrough':
                    playthrough = True

pp.pprint(sort_dictionary(locations))
print(" ")
print(" ")
print(" ")
pp.pprint(sort_dictionary(transitions))
print(file_count)