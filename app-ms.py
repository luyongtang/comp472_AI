from game.inputOutput import *
from search_algorithms.dfs import DFS

board_puzzles = create_boards_from_file("sample/test.txt")

index = 0
for puzzle in board_puzzles:
    print(puzzle.size, puzzle.max_depth, puzzle.original_config)
    dfs = DFS(puzzle.size,puzzle.max_depth,puzzle.original_config)
    dfs.search()
    path = dfs.generate_search_path()
    sol = dfs.generate_solution()
    create_output_files_for_puzzle("dfs",index, path, sol)
    index += 1
