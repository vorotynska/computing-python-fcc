# In this project, you'll learn how to use functions, loops, conditional 
# statements, and dictionary comprehensions to implement a Shortest Path algorithm.

my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)],
}

# The algorithm will start at a specified node. Then it will explore the graph 
# to find the shortest path between the starting node, or source, and all the other nodes.

def shortest_path(graph, start):
    #To keep track of the visited nodes, you need a list of all the nodes in the graph. 
    # Once a node is visited, it will be removed from that list.
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[node] = 0
        else:
            distances[node] = float('inf')
    print(f'Unvisited: {unvisited}\nDistances: {distances}')

shortest_path(my_graph, 'A')
