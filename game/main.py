import numpy as np


class Board:
    def __init__(self, size, max_depth, max_length, original_config):
        self.size = size
        self.max_depth = max_depth
        self.max_length = max_length
        self.original_config = original_config

    def flip(self, pos, pre_config):
        print(self.original_config)

    def display_info(self):
        print(self.size, self.original_config)

    def find_adjacent_tokens(self, pos):
        adjacent = [(pos - self.size) < 0 and -1 or (pos - self.size),  # find pos of up
                    (pos + self.size) > len(self.original_config) and -1 or (pos + self.size),  # find pos of down
                    (pos % self.size) == 0 and -1 or (pos - 1),  # find pos of left
                    (pos % self.size) == (self.size - 1) and -1 or (pos + 1)]  # find pos of right
        print(adjacent)
        return adjacent
