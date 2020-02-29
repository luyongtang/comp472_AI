import sys
from game_setting.inputOutput import *
from search_algorithms.dfs import DFS
from search_algorithms.search import Search

#default path
path = "sample/test.txt"
if len(sys.argv)>1:
    path = str(sys.argv[1])

board_puzzles = create_boards_from_file(path)
board = board_puzzles[0]
bfs = Search(board, Search.Astar)

bfs.findsolution()

exit()
index = 0
for board in board_puzzles:
    print(board.size, board.max_depth, board.max_length, board.original_config)
    #DFS Search
    dfs = DFS(board.size,board.max_depth,board.original_config)
    dfs.search()
    path = dfs.generate_search_path()
    sol = dfs.generate_solution()
    create_output_files_for_puzzle("dfs",index, path, sol)
    #BFS
    
    index += 1
