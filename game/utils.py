import numpy as np
fake_children = [
    [1, 0, ['010110010']], [1, 1, ['010110010']], [1, 2, ['010110010']],
    [2, 0, ['010110010']], [2, 1, ['010110010']], [2, 2, ['010110010']],
    [3, 0, ['010110010']], [3, 1, ['010110010']], [3, 2, ['010110010']],
    [4, 0, ['010110010']], [4, 1, ['010110010']], [4, 2, ['010110010']],
    ]


def flip(positions, config):
    # print("========================START=======================")
    my_config = list(config)
    # print(config)
    # print(positions)
    # print("STARTING FLIPPING")
    for p in positions:
        if p == -1:
            continue
        # print(p)
        if my_config[p] == "0":
            my_config[p] = "1"
        else:
            my_config[p] = "0"
    # print("========================END=======================")
    result = ''

    return result.join(my_config)

def find_adjacent_tokens(size, pos, config):
    # print("GETTING POSITION")
    adjacent = [(pos - size) < 0 and -1 or (pos - size),  # find pos of up
                (pos + size) >= len(config) and -1 or (pos + size),  # find pos of down
                (pos % size) == 0 and -1 or (pos - 1),  # find pos of left
                (pos % size) == (size - 1) and -1 or (pos + 1)]  # find pos of right
    # print(adjacent)
    return adjacent

def calculate_heuristic(config):
    my_list = list(config)
    h = 0
    for p in my_list:
        if p == "0":
            h += 1
    return h

def config_to_array(size,config):
    my_config = list(config)
    index = 0
    array = []
    temp_array = []

    for item in my_config:
        if index % size==0 and index is not 0:
            array.append(temp_array[:])
            temp_array = []
        temp_array.append(my_config[index])
        index += 1
    array.append(temp_array[:])
    return array

def print_config(size, config):
    array = config_to_array(size, config)
    for item in array:
        print(item)

def is_goal_state(config):
    return "1" not in config


def transform_pos(size, pos):
    row_base = ord("A")
    row = chr(int(pos/size)+row_base)
    column_base = 1
    column = column_base + int(pos % size)
    return row+str(column)


# temporary use
def get_children(node):
    if not node:
        return []
    return fake_children


