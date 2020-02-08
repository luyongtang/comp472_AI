from game import utils, childrenCreator


class DFS:
    def __init__(self, size, max_depth, config):
        self.initial_config = config
        self.size = size
        self.max_depth = max_depth - 1
        self.is_solved = False
        self.candidate_list = []
        self.solution_list = []
        self.search_list = []

    def update_candidate(self, children):
        result = children
        result.extend(self.candidate_list)
        self.candidate_list = result
        # print(self.candidate_list)

    def add_to_search_list(self, config):
        text = '0 0 0 ' + config + '\n'
        # print(text)
        self.search_list.append(text)

    def generate_solution(self):
        if not self.is_solved:
            #print('no solution')
            return ['no solution']
        output = []
        text = "0 " + self.initial_config + '\n'
        output.append(text)
        for node in self.solution_list:
            text = '' + utils.transform_pos(self.size, node[1]) + ' ' + node[2] + '\n'
            output.append(text)
        #print('solution is: ', output)
        return output
    def generate_search_path(self):

        #print('search path: ', self.search_list)
        return self.search_list

    def search(self):
        self.add_to_search_list(self.initial_config)
        if utils.is_goal_state(self.initial_config):
            self.is_solved = True
            return
        current_node = []
        root = [1, 0, self.initial_config]
        self.update_candidate(childrenCreator.create_children_settings(root))
        while len(self.candidate_list) > 0 and not self.is_solved:
            # print("while loop starts...")
            # print(self.candidate_list)
            current_node = self.candidate_list.pop(0)
            if len(self.solution_list) < self.max_depth - 1:
                self.update_candidate(childrenCreator.create_children_settings(current_node))
            self.is_solved = utils.is_goal_state(current_node[2])
            self.solution_list.append(current_node)
            self.add_to_search_list(current_node[2])
            if self.is_solved:
                # self.generate_solution()
                # print("solved")
                return
            if len(self.solution_list) < self.max_depth:  # explore the next child
                # print('add more to solution_list')
                continue
            else:
                # print('reach the max depth')
                if len(self.candidate_list) == 0:
                    continue
                self.solution_list.pop()  # solution list is full so we cannot add more node
                # top the first node in the candidates to check if it is a node in a less depth
                to_check = self.candidate_list[0]
                # print(self.solution_list)
                while len(self.solution_list) > 0 and to_check[0] <= (self.solution_list[len(self.solution_list)-1])[0]:
                    # print('go up by 1 in depth')
                    self.solution_list.pop()  # explore another parent node so we need to pop the current one
        # print('no solution is found')







