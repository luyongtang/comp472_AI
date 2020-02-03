
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


def calculate_heuristic(config):
    my_list = list(config)
    h = 0
    for p in my_list:
        if p == "0":
            h += 1
    return h
