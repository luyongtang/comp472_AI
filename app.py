import sys
from game_setting.inputOutput import *
from search_algorithms.dfs import DFS

#default path
path = "sample/test.txt"
if len(sys.argv)>1:
    path = str(sys.argv[1])
else:
    print("No file path provided in argument. Exiting the app")
    print("Using default path:", path)

print()

board_puzzles = create_boards_from_file(path)

index = 0
for puzzle in board_puzzles:
    print(puzzle.size, puzzle.max_depth, puzzle.max_length, puzzle.original_config)
    dfs = DFS(puzzle.size,puzzle.max_depth,puzzle.original_config)
    dfs.search()
    path = dfs.generate_search_path()
    sol = dfs.generate_solution()
    create_output_files_for_puzzle("dfs",index, path, sol)
    index += 1
