import math
from game.utils import *
from copy import copy, deepcopy

def create_children_settings(setting):
    config_list = list(setting[2])
    board_size = int(math.sqrt(len(config_list)))
    duplicate_settings = create_duplicates(setting,len(config_list))
    print("board_size of puzzle", board_size )
    print("board_size of duplicate childens", len(duplicate_settings))
    flipped_settings = flip_settings(board_size, duplicate_settings)
        
def create_duplicates(setting, number_of_copies):
    copies = []
    for i in range(number_of_copies):
        copies.append(deepcopy(setting))
    return copies

def flip_settings(board_size, settings):
    pos = 0
    for item in settings:
        print("FLIPPING FOR POSITION",pos)
        item[1]=pos
        item[2]=apply_flip(board_size, pos, item[2])
        pos += 1
    return settings

def apply_flip(board_size, pos, config) :
    flip_positions = find_adjacent_tokens(board_size, pos, config)
    flip_positions.append(pos)
    return flip(flip_positions,config)