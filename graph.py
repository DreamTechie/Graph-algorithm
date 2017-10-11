"""
@author: Saurab Dulal
Date: October 9, 2017
GPL License

Dependencies: Python 3.x +

"Python program to compute if a supplied directed graph is DAG or not.
If DAG, it finds linear sorting and also the logest path from a node or in total graph"
"""

import sys

# check if file is supplied while running the program and set the file_flag accordingly
# try:
#     file_flag = True
#     fromFile = sys.argv[1]
# except Exception as e:
#     file_flag = False

DAG_flag = True


# graph handler class
class graph:
    order_counter = 0  # this is a static variable
    node_ptr = {}
    list_of_traverse_path = []

    def __init__(self):
        # handling the other cases
        pass

    # currently no need of this function
    def return_node_ptr(self, node_id):

        return self.node_ptr[node_id]

    def set_parent_pointer(self):
        for i in self.c_node:
            temp = self.return_node_ptr(i)
            temp.parent_node.append(self.p_node)

    def dec_degree(self):
        for i in self.c_node:
            temp = self.return_node_ptr(i)
            temp.degree -= 1

    def __init_nodes__(self, p_node, c_node, degree):
        self.node_ptr.update({p_node: self})
        self.pre_order = 0
        self.post_order = 0
        self.visited = False  # node visited or not
        self.parent_node = [None]
        self.p_node = p_node  # present node
        self.c_node = c_node  # child to present node
        self.degree = degree
        self.rechable_node = []
        if self.c_node is None:
            self.is_leaf = True


# graph input function to handle input from file or from console
def graph_input(node_list=None):
    global file_flag
    no_of_nodes = None
    graph_dic = {}
    isolated_node = []

    print("Please 1 to input from file or press 2 to input from console")
    a = raw_input()

    if a == '1':
        print("Enter the file name")
        fromFile = raw_input()

        if not fromFile:
            print("File name not submitted")  # file not found error
            return
        else:
            with open(fromFile, 'r') as f:
                lines = f.readlines()
                no_of_nodes = int(lines[0].strip())

                for i in range(1, no_of_nodes + 1):
                    graph_dic[i] = []

                for line in range(1, len(lines)):
                    edges = lines[line].strip()
                    a = edges.split(',')
                    graph_dic[int(a[0])].append(int(a[1]))

            node_list = [graph() for i in range(len(graph_dic))]

    elif a == '2':
        node_list, isolated_node, graph_dic = graph_construction()

    else:
        print("wrong input program exited")
        exit()

    counter = -1
    for node in graph_dic.keys():
        degree = 0

        for key, val in graph_dic.items():
            if node in val:
                # if node in ([items for val,items in graph_dic.items()]):
                degree += 1  # node with degree 0 are source
        counter += 1
        node_list[counter].__init_nodes__(node, graph_dic[node], degree)

    path = graph_traversal(node_list)

    if (DAG_flag):
        print ("The Graph is a DAG")
        print("**********Summary of the given DAG**********")
        path_with_isolated_node = path + isolated_node
        print ("Linear ordering of the graph is " + str(path_with_isolated_node))
        total_possible_path = all_paths(graph_dic)
        print("All possible path in a Graph")
        print (total_possible_path)
        print("Longest path in the Graph")
        print(longest_path(total_possible_path))
        print("Enter a node to find a longest path")
        node = raw_input()
        result = longest_path_from_a_node(total_possible_path, int(node))
        print("Longest path for the given node " + str(node) + " is "
              + str(result))
        print("And the length of the longest path from node " + str(node) + " is " + str(len(result) - 1))
        # print(len(longest_path_from_a_node(total_possible_path,int(node)))-1)
    else:
        print ("The Graph is Not a DAG")


# graph traversal to find if DAG or not
def graph_traversal(graph, vertex=None, trv_path=[]):
    """
    :type trv_path: object
    """

    source_flag = False
    sink_flag = False
    starting_node = vertex
    all_visited = True  # if all nodes are visited retrun
    for node in graph:
        if node.visited == True:
            continue
        all_visited = False
        if node.degree == 0:
            if starting_node == None:
                starting_node = node
            trv_path.append(starting_node.p_node)
            source_flag = True
            break

    if (all_visited):
        return trv_path

    for node in graph:
        if node.visited == True: continue
        if not node.c_node:
            sink_flag = True
            break

    if source_flag and sink_flag:

        starting_node.visited = True

        starting_node.dec_degree()
        starting_node.set_parent_pointer()
        ek_flag = True

        for childs in starting_node.c_node:
            if childs not in trv_path:
                temp = starting_node.return_node_ptr(childs)

                if temp.degree != 0:
                    continue
                ek_flag = False
                trv_path = graph_traversal(graph, temp, trv_path)

        if (ek_flag):
            trv_path = graph_traversal(graph, None, trv_path)

    else:
        print("reached here")
        global DAG_flag
        DAG_flag = False
        print(DAG_flag)
        return trv_path
    return trv_path


# find all the possible path from a node, only works for DAG
def dfs_find_all_path_from_node(graph, vertex, paths=[]):
    node = vertex[-1]  # start at the end of path
    if node in graph:
        if graph[node]:
            for val in graph[node]:
                new_path = vertex + [val]
                paths = dfs_find_all_path_from_node(graph, new_path, paths)
        else:
            paths += [vertex]
            return paths
    else:
        paths += [vertex]
    return paths


# find the longest path from a give node, only works for DAG
def longest_path_from_a_node(list, node):
    buf_path = []
    for path in list:
        if path[0] == node:
            if (len(path) > len(buf_path)):
                buf_path = path
    return buf_path


# longest path of a DAG, only works for DAG
def longest_path(list):
    buf_path = []
    for path in list:
        if len(path) > len(buf_path):
            buf_path = path
    return buf_path


# path finder init function
def all_paths(graph_dic_withouth_null_values):
    paths = []
    for key in graph_dic_withouth_null_values:
        paths = dfs_find_all_path_from_node(graph_dic_withouth_null_values, [key], paths)

    return paths


# graph construction from given console input
def graph_construction(node_list=None):
    no_of_nodes = None
    graph_dic = {}
    isolated_node = []

    print("Enter no of nodes and corresponding edges, and enter 'q' to end")
    while True:
        if no_of_nodes is None:
            no_of_nodes = raw_input()
            try:
                if isinstance(int(no_of_nodes), int):
                    no_of_nodes = int(no_of_nodes)
                elif no_of_nodes == 'q':
                    break
            except:
                print("invalid imput, program exited")
                exit()
        else:

            edge = raw_input()  # Format A -> B

            if edge == 'q':
                real_vertex = [keys for keys in graph_dic]

                if len(real_vertex) != no_of_nodes:
                    print("Your inital no of nodes doesn't matches actual no of nodes")
                    print("Updated no of nodes = " + str(len(real_vertex)))
                    print("Vertices" + str(real_vertex))
                else:
                    print("No of vertices " + str(len(real_vertex)))
                    print("Vertices" + str(real_vertex))
                break

            else:

                edge = edge.split(',')
                edge = [int(e) for e in edge]  # conversion to integer
                if len(edge) == 1:
                    isolated_node.append(edge[0])
                    continue

                if edge[0] not in [vertex for vertex in graph_dic.keys()]:
                    graph_dic.update({edge[0]: [edge[1]]})

                    if edge[1] not in [vertex for vertex in graph_dic.keys()]:
                        graph_dic.update(({edge[1]: []}))

                elif edge[0] in [vertex for vertex in graph_dic.keys()]:
                    if edge[1] not in [vertex for vertex in graph_dic[edge[0]]]:
                        graph_dic[edge[0]].append(edge[1])

                    if edge[1] not in [vertex for vertex in graph_dic.keys()]:
                        graph_dic.update(({edge[1]: []}))

                else:
                    continue

    # Getting graph only whose node has a child
    if not dict([(key, val) for key, val in graph_dic.items() if len(val) > 0]):
        print("Graph is a DAG, but no path exist from a node to other node")
        return

    # Innitilizing pointers for each node in a graph
    node_list = [graph() for i in range(len(graph_dic))]
    return node_list, isolated_node, graph_dic

#
# def main():
#     graph_input()
#
#
# if __name__ == '__main__':
#     main()
#
