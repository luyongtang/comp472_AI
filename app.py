import sys
from game_setting.inputOutput import *
from search_algorithms.dfs import DFS
from search_algorithms.search import Search

#default path
path = "sample/test.txt"
if len(sys.argv)>1:
    path = str(sys.argv[1])
else:
    print("No file path provided in argument")
    print("Using default path:", path)

print()

board_puzzles = create_boards_from_file(path)

index = 0
for board in board_puzzles:
    print(board.size, board.max_depth, board.max_length, board.config)
    #dfs
    print("DFS search started...")
    dfs = DFS(board.size,board.max_depth, board.config)
    dfs.search()
    path = dfs.generate_search_path()
    sol = dfs.generate_solution()
    print("DFS search done")
    create_output_files_for_puzzle("dfs",index, path, sol)
    #bfs-astar props
    Printer.puzzlenumber=index
    #bfs
    Printer.puzzletype="bfs"
    print("BFS search started...")
    search = Search(board, Search.BFS)
    search.findsolution()
    print("BFS search done")
    #astar
    Printer.puzzletype="astar"
    print("Astar search started...")
    search = Search(board, Search.Astar)
    search.findsolution()
    print("Astar search done")
    print()
    index += 1
