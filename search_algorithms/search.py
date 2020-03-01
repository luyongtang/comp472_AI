from copy import deepcopy
from .tools.node import Node
from game_setting.utils import *
from game_setting.childrenCreator import *
from game_setting.board import Board
from random import randrange
from game_setting.inputOutput import *
from operator import attrgetter

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
        self.rootnode = Node(deepcopy(board), None,0, 0, board.config)
        self.rootnode.initscore()
        self.addtoopenlist([self.rootnode])
        self.searchalgo = searchalgo

    def findsolution(self):
        #assume no solution at start
        solutionnode = None
        while self.openlist:
            solutionnode = self.search()
            if solutionnode:
                break

        if solutionnode:
            #print("solution yeah!")
            solutionpath = self.collectsolutionpath(solutionnode)
            Printer.solutionpath(solutionpath)
            #for item in solutionpath:
            #    print()
            #    print(item[0])
            #    print_config(4,item[1])
        else:
            Printer.solutionpath(None)
            print("OUT")

    def search(self):
        #print(len(self.closelist), len(self.openlist))
        #get best next node to visit
        node = self.openlist.pop(0)
        if is_goal_state(node.board.config):
            return node
        if node.reachedmaxpathlength() or self.check_duplicate_config(node, self.closelist) != -1:
            #ignore this node, continue search
            # print("scope out")
            return None
        self.visitnode(node)
        #for item in self.openlist:
        #    print(item.finalscore)
        return None

    def addtoopenlist(self, nodelist):
        for node in nodelist:
            check = self.check_duplicate_config(node, self.openlist)
            if check == -1:
                self.openlist.append(node)
            # update the scores if a better path is found to current node
            elif self.openlist[check].finalscore > node.finalscore:
                self.openlist[check].finalscore = node.finalscore
                self.openlist[check].gscore = node.gscore
            #     print("update a better path")
            # else:
            #     print("duplicate!")

    def addtocloselist(self,node):
        self.closelist.insert(0,node)

    def visitnode(self, node):
        configs = generate_children_configs(node.board.config, node.board.size)
        childrennodes = self.createnodefromconfigs(configs,node)
        nodeswithscores = self.calcularescore(childrennodes)
        # self.openlist = self.openlist + nodeswithscores
        self.addtoopenlist(nodeswithscores)
        self.sort_open_list()
        self.addtocloselist(node)
        Printer.searchpath(node)

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
        for configprop in configslist:
            position = configprop[0]
            config = configprop[1]
            temp_board = Board(parentnode.board.size,None, parentnode.board.max_length,config)
            temp_node = Node(temp_board, parentnode, pathlength, position, config)
            nodes.append(temp_node)
        return nodes

    def collectsolutionpath(self, solutionnode):
        return self.traversetillroot([],solutionnode)

    def traversetillroot(self, pathlist, node):
        pathlist.insert(0,(node.flippedposition, node.board.config))
        if node.parent is None:
            return pathlist
        return self.traversetillroot(pathlist, node.parent)

    def check_duplicate_config(self, node, list_to_check):
        for index, element in enumerate(list_to_check):
            if element.board.config == node.board.config:
                return index
        return -1

    def sort_open_list(self):
        self.openlist = sorted(self.openlist, key=attrgetter('config'))
        self.openlist = sorted(self.openlist, key=attrgetter('finalscore'))

