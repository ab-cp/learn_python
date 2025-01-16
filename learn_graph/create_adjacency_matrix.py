example_nodes = list(range(4)) # 0, 1, 2, 3
example_edges = [(0, 1), (1, 2), (0, 2), (1, 3), (3, 0)]    

example_adjacency_matrix = [
#    0  1  2  3
    [0, 1, 1, 0], # 0
    [0, 0, 1, 1], # 1
    [0, 0, 0, 0], # 2
    [1, 0, 0, 0], # 3
]

def create_adjacency_matrix(nodes, edges):
    matrix = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]
    for s, t in edges:
        matrix[s][t] = 1
    return matrix


new_matrix = create_adjacency_matrix(example_nodes, example_edges)

assert  new_matrix == example_adjacency_matrix
