import math
from game_setting.utils import *
from copy import copy, deepcopy

def create_children_settings(setting):
    flipped_settings = init_children(setting)
    flipped_settings.sort(key = lambda x:x[2])
    # print(flipped_settings)
    return flipped_settings

def init_children(setting):
    config_list = list(setting[2])
    board_size = int(math.sqrt(len(config_list)))
    duplicate_settings = create_duplicates(setting,len(config_list))
    # print("board_size of puzzle", board_size )
    # print("board_size of duplicate childens", len(duplicate_settings))
    flipped_settings = flip_settings(board_size, duplicate_settings)
    return flipped_settings

def generate_children_configs(config, board_size):
    duplicate_configs = create_duplicates(config, board_size*board_size)
    flipped_configs = flip_configs(duplicate_configs, board_size)
    return flipped_configs

def flip_configs(config_list, board_size):
    pos = 0
    flipped_configs = []
    for config in config_list:
        flipped_configs.append(apply_flip(board_size, pos, config))
        pos +=1
    return flipped_configs

def print_settings(board_size, settings):
    pos = 0
    for item in settings:
        # print(pos)
        print_config(board_size,item[2])
        pos += 1
        
def create_duplicates(setting, number_of_copies):
    copies = []
    for i in range(number_of_copies):
        copies.append(deepcopy(setting))
    return copies

def flip_settings(board_size, settings):
    pos = 0
    for item in settings:
        # print("FLIPPING FOR POSITION",pos)
        item[0] = item[0] + 1
        item[1]=pos
        item[2]=apply_flip(board_size, pos, item[2])
        pos += 1
    return settings

def apply_flip(board_size, pos, config) :
    flip_positions = find_adjacent_tokens(board_size, pos, config)
    flip_positions.append(pos)
    return flip(flip_positions,config)