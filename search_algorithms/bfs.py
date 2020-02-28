from copy import deepcopy
from .tools.node import Node
from game_setting.utils import *
from game_setting.childrenCreator import *
from game_setting.board import Board

class BFS:
    def __init__(self, board):
        self.initialboard = board
        self.openlist = []
        self.closelist = []
        self.rootnode = Node(deepcopy(board), None,0)
        self.addtoopenlist([self.rootnode])

    def findsolution(self):
        solutionnode = self.search()
        if solutionnode:
            print("solution yeah!")
        else:
            print("OUT")

    def search(self):
        if not self.openlist:
            return None
        #get best next node to visit
        node = self.openlist.pop(0)
        if is_goal_state(node.board.config):
            return node
        if node.reachedmaxpathlength() or node in self.closelist:
            #ignore this node, continue search
            return self.search()
        self.visitnode(node)
        print(self.openlist)
        return False
        #if is_goal_state(node.board.config):
        #    print("solution found")
        #    return
        #self.closelist.insert(0,node)
        #print(self.closelist)
        #print("cool")
    
    def addtoopenlist(self, nodelist):
        for node in nodelist:
            self.openlist.append(node)
    
    def addtocloselist(self,node):
        self.closelist.insert(0,node)

    def visitnode(self, node):
        configs = generate_children_configs(node.board.config, node.board.size)
        childrennodes = self.createnodefromconfigs(configs,node)
        self.openlist = self.openlist + childrennodes
        self.addtocloselist(node)
        
    def createnodefromconfigs(self, configslist, parentnode):
        nodes = []
        pathlength = parentnode.board.max_length+1
        for config in configslist:
            temp_board = Board(parentnode.board.size,None, parentnode.board.max_length,config)
            temp_node = Node(temp_board, parentnode, pathlength)
            nodes.append(temp_node)
        return nodes




    
