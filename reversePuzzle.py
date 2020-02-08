from random import randrange
from game.utils import *

def create_reverse_puzzle(board_size, iteration):
    lis_length = board_size*board_size
    config = "0"*(lis_length)
    rand_pos = 0
    reverse_solution = []
    for i in  range(iteration):
        rand_pos = randrange(lis_length)
        positions_list = find_adjacent_tokens(board_size, rand_pos, config)
        positions_list.append(rand_pos)
        config = flip(positions_list, config)
        reverse_solution.append(transform_pos(board_size, rand_pos))
    solution = reverse_solution.copy()
    solution.reverse()    
    return (config, reverse_solution, solution)
