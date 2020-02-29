from game_setting.board import Board
from game_setting.utils import *
from search_algorithms import dfs
from reversePuzzle import *
from search_algorithms.search import Search

# "1110101111000100"
# "1110111101101110"
# "1111110011110010"
# "101100011" 'A1', 'C3', 'A3'

print("start")
# config = "1011011010000011"
# config = "0000000000000000"
config = "011101110"
# config = "110010000"

for i in range(100):
    #selected_pos = 12
    board_size=7
    max_depth=10
    test_case = create_reverse_puzzle(board_size,max_depth)
    #test_case[0] = "111001011"
    #test_case[2] = ['A1', 'C3', 'A3']
    #print(test_case)
    board = Board(board_size, max_depth, 50, test_case[0])
    search = Search(board, Search.Astar)
    search.findsolution()

    #search.search()
    #path = search.generate_search_path()
    #sol = search.generate_solution()
    #trim_sol = []
    #for el in sol:
    #    trim_sol.append(el[0:2])
    #print(test_case[0],test_case[2], ",".join(trim_sol))

    
    #print(path)
    #for search in path:
    #    print(search)