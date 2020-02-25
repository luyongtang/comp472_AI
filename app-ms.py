from game_setting.board import Board
from game_setting.utils import *
from search_algorithms import dfs

print("start")
# config = "1011011010000011"
# config = "0000000000000000"
config = "1100100000000000"
# config = "110010000"
selected_pos = 12
board = Board(4, 2, 2, config)
search = dfs.DFS(4, 3, config)
search.search()
path = search.generate_search_path()
print(path)
sol = search.generate_solution()
print(sol)
