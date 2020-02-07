import numpy as np
def flip(positions, config):
    my_config = list(config)
    for p in positions:
        if my_config[p] == "0":
            my_config[p] = "1"
        else:
            my_config[p] = "0"
    print("flipped!")
    result = ''
    return result.join(my_config)

def find_adjacent_tokens(size,pos, config):
    adjacent = [(pos - size) < 0 and -1 or (pos - size),  # find pos of up
                (pos + size) > len(config) and -1 or (pos + size),  # find pos of down
                (pos % size) == 0 and -1 or (pos - 1),  # find pos of left
                (pos % size) == (size - 1) and -1 or (pos + 1)]  # find pos of right
    print(adjacent)
    return adjacent

def calculate_heuristic(config):
    my_list = list(config)
    h = 0
    for p in my_list:
        if p == "0":
            h += 1
    return h

def config_to_array(size,config):
    print("printing config", config)
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


