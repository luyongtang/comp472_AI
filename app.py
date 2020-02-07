from game.main import Board
from game.utils import *

print("start")
config = "1011011010000011"
selected_pos = 15
board = Board(4, 2, 2, config)
# board.display_info()
to_flip = board.find_adjacent_tokens(selected_pos)
to_flip.append(selected_pos)
print(flip(to_flip, config))
print(config)
print(calculate_heuristic(config))
print_config(board.size,board.original_config)

