
class Node:
    def __init__(self, board, parent, pathlength):
        self.board = board
        self.parent = parent
        self.children = []
        self.pathlength = pathlength
        self.hscore = None
        self.gscore = None
        self.finalscore = None

    def getPathLength(self):
        return self.pathlength
    
    def reachedmaxpathlength(self):
        return self.board.max_length<=self.pathlength
    
    def initscore(self):
        self.hscore = 0
        self.gscore = 0
        self.finalscore = 0