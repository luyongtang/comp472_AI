from copy import deepcopy
from .tools.node import Node
from game_setting.utils import is_goal_state
class BFS:
    def __init__(self, board):
        self.initialboard = board
        self.openlist = []
        self.closelist = []
        self.rootnode = Node(deepcopy(board), None, {},0)
    
    def findsolution(self):
        self.search(self.rootnode)

    def search(self, node):
        if is_goal_state(node.board.config):
            print("solution found")
            return
        self.closelist.insert(0,node)
        print(self.closelist)
        print("cool")
        

    
