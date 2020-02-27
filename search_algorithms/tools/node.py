
class Node:
    def __init__(self, board, parent, children, pathlength):
        self.board = board
        self.parent = parent
        self.children = children
        self.pathlength = pathlength
    
    def incrementpathlengh(self):
        self.pathlength +=1