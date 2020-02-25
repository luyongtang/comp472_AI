import csv
from game_setting.board import Board 
def create_boards_from_file(filepath):
    board_puzzles = []
    with open(filepath, 'r') as file:
            reader = csv.reader(file, delimiter=' ')
            for row in reader:
                board_puzzles.append(Board(int(row[0]), int(row[1]), int(row[2]), row[3]))

    return board_puzzles

def create_output_files_for_puzzle(search_type, puzzle_number, paths, solution):
    output_to_file(search_type,'search', puzzle_number, paths)
    output_to_file(search_type,'solution', puzzle_number, solution)

def output_to_file(search_type, file_short_name, puzzle_number, paths):
    with open ('output/'+str(puzzle_number)+'_'+search_type+'_'+file_short_name+'.txt', 'w') as file:
        for path in paths:
            file.write(path)