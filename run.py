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


def build_locations(dict_key, locations_dict):
    if dict_key in locations_dict:
        locations_dict[dict_key] += 1
    else:
        locations_dict[dict_key] = 1


def build_transitions(location_b, transitions_dict, dict_key):
    if location_b:
        location_a = location_b
        location_b = dict_key
        transition = get_transition(location_a, location_b)
        if transition in transitions_dict:
            transitions_dict[transition] += 1
        else:
            transitions_dict[transition] = 1


def build_location_prize_combos(dict_key, location_prize_combos_dict, word):
    if dict_key in location_prize_combos_dict:
        dict_list = location_prize_combos_dict[dict_key]
        dict_list.append(word)
        location_prize_combos_dict[key] = dict_list
    else:
        location_prize_combos_dict[key] = [word]


def print_dict(some_dict):
    for dict_key in some_dict:
        print('{} :'.format(dict_key, some_dict[dict_key]))
        for some_item in sorted(some_dict[dict_key]):
            print('   {}'.format(some_item))
    print(" ")
    print(" ")
    print(" ")


def print_list(some_list):
    for entry in some_list:
        if entry[1] != 1:
            print("{} : {}".format(entry[0], entry[1]))
    print(" ")
    print(" ")
    print(" ")


def print_report(locations_dict, transitions_dict, locations_prize_combos_dict, file_count_number):
    print(" ")
    print_list(sort_dictionary(locations_dict))
    print_list(sort_dictionary(transitions_dict))
    print_dict(locations_prize_combos_dict)
    print("File Count: {}".format(file_count_number))


pp = pprint.PrettyPrinter(indent=0, width=1000)

os.getcwd()

location_prize_combos = {}

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
            play_through = False
            for line in openFile:
                part = line.split(":")
                key = crop(part[0])
                if not play_through:
                    next
                else:
                    try:
                        item = crop(part[1])
                        if item in items:
                            build_transitions(current_location, transitions, key)
                            build_locations(key, locations)
                            build_location_prize_combos(key, location_prize_combos, item)
                            current_location = key
                    except IndexError:
                        pass
                if key == 'playthrough':
                    play_through = True
print_report(locations, transitions, location_prize_combos, file_count)