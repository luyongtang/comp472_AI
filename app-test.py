from game.main import Board
from game.utils import *
from search_algorithms import dfs
from reversePuzzle import *

print("start")
# config = "1011011010000011"
# config = "0000000000000000"
config = "011101110"
# config = "110010000"

for i in range(1):
    selected_pos = 12
    board_size=3
    max_depth=2
    test_case = create_reverse_puzzle(board_size,max_depth)
    #print(test_case)
    board = Board(board_size, max_depth, 2, test_case[0])
    search = dfs.DFS(board_size, max_depth, test_case[0])
    search.search()
    search.generate_search_path()
    temp = search.generate_solution()
    print(test_case[0],test_case[2],temp)