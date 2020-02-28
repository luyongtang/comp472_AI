
class Node:
    def __init__(self, board, parent, pathlength):
        self.board = board
        self.parent = parent
        self.children = []
        self.pathlength = pathlength

    def getPathLength(self):
        return self.pathlength
    
    def reachedmaxpathlength(self):
        return self.board.max_length<=self.pathlength