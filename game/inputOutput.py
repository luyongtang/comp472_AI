import csv
from game.main import Board 
def create_boards_from_file(filepath):
    board_puzzles = []
    with open(filepath, 'r') as file:
            reader = csv.reader(file, delimiter=' ')
            for row in reader:
                board_puzzles.append(Board(row[0], row[1], row[2], row[3]))
                
    return board_puzzles
    