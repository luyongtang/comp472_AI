
class Board:
    def __init__(self, size, max_depth, max_length, config):
        self.size = size
        self.max_depth = max_depth
        self.max_length = max_length
        self.config = config

    def flip(self, pos, pre_config):
        print(self.config)

    def display_info(self):
        print(self.size, self.config)
