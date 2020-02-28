from copy import deepcopy
from .tools.node import Node
from game_setting.utils import *
from game_setting.childrenCreator import *
from game_setting.board import Board
from random import randrange

class Search:
    def h(node):
        node.hscore = calculate_heuristic(node.board.config)
        node.finalscore += node.hscore
    def g(node):
        node.gscore = node.pathlength
        node.finalscore += node.gscore   
    BFS = [h]
    Astar = [h,g]
    def __init__(self, board, searchalgo):
        self.initialboard = board
        self.openlist = []
        self.closelist = []
        self.rootnode = Node(deepcopy(board), None,0, 0)
        self.addtoopenlist([self.rootnode])
        self.searchalgo = searchalgo

    def findsolution(self):
        solutionnode = self.search()
        if solutionnode:
            print("solution yeah!")
            solutionpath = self.collectsolutionpath(solutionnode)
            for item in solutionpath:
                print()
                print_config(4,item)
        else:
            print("OUT")

    def search(self):
        print(len(self.closelist), len(self.openlist))
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
        #for item in self.openlist:
        #    print(item.finalscore)
        return self.search()
    
    def addtoopenlist(self, nodelist):
        for node in nodelist:
            self.openlist.append(node)
    
    def addtocloselist(self,node):
        self.closelist.insert(0,node)

    def visitnode(self, node):
        configs = generate_children_configs(node.board.config, node.board.size)
        childrennodes = self.createnodefromconfigs(configs,node)
        nodeswithscores = self.calcularescore(childrennodes)
        self.openlist = self.openlist + nodeswithscores
        self.openlist.sort(key = lambda x:x.finalscore)
        self.addtocloselist(node)
    
    def calcularescore(self, nodes):
        for node in nodes:
            node.initscore()
        for formula in self.searchalgo:
            for node in nodes:
                formula(node)
        return nodes

    def createnodefromconfigs(self, configslist, parentnode):
        nodes = []
        pathlength = parentnode.pathlength+1
        for config in configslist:
            temp_board = Board(parentnode.board.size,None, parentnode.board.max_length,config)
            temp_node = Node(temp_board, parentnode, pathlength)
            nodes.append(temp_node)
        return nodes

    def collectsolutionpath(self, solutionnode):
        return self.traversetillroot([],solutionnode)

    def traversetillroot(self, pathlist, node):
        pathlist.insert(0,node.board.config)
        if node.parent is None:
            return pathlist
        return self.traversetillroot(pathlist, node.parent)
        
        



    
