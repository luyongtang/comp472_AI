from game.main import Board
from game.utils import *
from search_algorithms import dfs
from reversePuzzle import *

# "1110101111000100"
# "1110111101101110"
# "1111110011110010"
# "101100011" 'A1', 'C3', 'A3'

print("start")
# config = "1011011010000011"
# config = "0000000000000000"
config = "011101110"
# config = "110010000"

for i in range(200):
    selected_pos = 12
    board_size=4
    max_depth=3
    test_case = create_reverse_puzzle(board_size,max_depth)
    #test_case[0] = "101100011"
    #test_case[2] = ['A1', 'C3', 'A3']
    #print(test_case)
    board = Board(board_size, max_depth, 2, test_case[0])
    search = dfs.DFS(board_size, max_depth, test_case[0])
    search.search()
    path = search.generate_search_path()
    sol = search.generate_solution()
    trim_sol = []
    for el in sol:
        trim_sol.append(el[0:2])
    print(test_case[0],test_case[2], ",".join(trim_sol))

    
    #print(path)
    #for search in path:
    #    print(search)