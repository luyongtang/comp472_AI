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
