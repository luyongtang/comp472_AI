import math
from copy import copy, deepcopy

def create_children_settings(setting):
    config_list = list(setting[2])
    size = math.sqrt(len(config_list))
    duplicate_settings = create_duplicates(setting,len(config_list))
    print("size of puzzle", size )
    print("size of duplicate childens", len(duplicate_childens))
    
def create_duplicates(setting, number_of_copies):
    copies = []
    for i in range(number_of_copies):
        copies.append(deepcopy(setting))
    return copies
