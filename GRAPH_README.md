***"There are people who are very poor at documentation, spelling and grammar, 
voila! you found one. Good Luck"*** 

Problem 1
=========

Write a program that takes as input a directed graph (in the format described below) and outputs (I) ‘YES’ or ‘NO’ depending on whether the graph is a DAG, and, (II) in case it is a DAG, it outputs a linear ordering of the DAG, and, (III) in case it is a DAG, outputs the length of the longest path in the DAG starting from vertex 1.

The input will consist of several lines and will be given either as a text file or on the command prompt. The first line will be a positive integer n. This is the number of vertices of the graph - the names of the vertices will be 1, 2, 3, . . . , n. The next few lines will contain the edges of the graph as i, j where 1 ≤ i ≤ n and 1 ≤ j ≤ n and i 6= j. You can rest assured that the input will be in the correct format and as expected. A valid input could be for example:

Algorithm Explanation
---------------------

    -  Take input from file or from the console 
    -  Construct adjacency listing from the given input of format {1: [2], 2: [4], 3: [4, 1]}
    -  Create a graph class with all the required parameters, such as node pointer, visited flag, parent node, child node etc 
        - I have created some unnecessary fields in this program, it's just for some future works, if future exist == Ture
    -  Create graph objects mapped to equals no of available nodes, and initialize all the node as per the requirement
    -  Create all the necessary functions such as DFS, longest path finder and so on
        - Some created function may be useless for this problem 
    -  Call DFS function for the graph traversal and find if the graph is DAG or not
    -  If graph is DAG, find all the possible paths and linear ordering of the given directed graph
    -  Print the necessities and exit

Limitations
-----------

        - Graph should be in the following formats in the file 
        - 5 - no of nodes 
            1,3
            2,3
            4,1 - no line break after this line, i.e. this should be the last line of the file
        - While reading from file, it will create a dictionary of adjacency matrix(graph) of size equal to no of nodes 
        - While reading from file, file name should be supplied in following way
            "python graph.py file_name" #important 
            - If file name not submitted while running the program 
            and if option 1 (i.e. 1 - input from file) selected, then program will exit with following message. 
            "File name not submitted"
        - Program is tested for limited no of test cases and may contain some bugs and logical syntax error, forgive me !!!
        
        

Test Cases
==========

    ---------------------- While reading from file ------------------------
    
    #! /bin/bash
    python Main.py graphinput.txt
    Please 1 to input from file or press 2 to input from console
    input -> 1
    The Graph is a DAG
    **********Summary of the given DAG**********
    Linear ordering of the graph is [3, 4, 1, 2, 5]
    All possible path in a Graph
    [[1, 2], [2], [3, 4], [3, 1, 2], [4], [5]]
    Longest path in the Graph
    [3, 1, 2]
    Enter a node to find a longest path
    input -> 2

    ---------------------- While reading from Console ------------------------
    #! /bin/bash
    python Main.py input.txt
    Please 1 to input from file or press 2 to input from console
    input -> 2
    Enter no of nodes and corresponding edges, and enter 'q' to end
    4
    1,2
    3,4
    3,1
    q
    No of vertices 4
    Vertices[1, 2, 3, 4]
    The Graph is a DAG
    **********Summary of the given DAG**********
    Linear ordering of the graph is [3, 4, 1, 2]
    All possible path in a Graph
    [[1, 2], [2], [3, 4], [3, 1, 2], [4]]
    Longest path in the Graph
    [3, 1, 2]
    Enter a node to find a longest path
    3
    Longest path for the given node 3 is [3, 1, 2]
    And the length of the longest path from node 3 is 2
    
    ---------------------- While reading file but no file name supplied ------------------------
    Please 1 to input from file or press 2 to input from console
    input -> 1
    Output -> File name not submitted
    
 Functions used in the program
 -----------------------------
        graph_input(node_list=None):
           - Function to handle user input from file or from console
    
        def graph_construction(node_list=None)
           - Construct graph from the node_list i.e. adjanceny list
    
        graph_traversal(graph, vertex=None, trv_path=[])
           - Graph traversal to find if DAG or not, it uses a modified DFS 
    
        def dfs_find_all_path_from_node(graph, vertex, paths=[])
           - Find all the possible path from a node, only works for DAG. 
           - Future enhancement, this function can be merged with graph_traversal 
 
        def longest_path_from_a_node(list, node):
           - Finds a longest path from a node, it takes list of list of all paths as a argument 
 
        def longest_path(list):
           - Finds longest path in a give DAG 
    
        def all_paths(graph_dic)
           - Initilizer function to calculate all paths and longest path 
 
 
 
