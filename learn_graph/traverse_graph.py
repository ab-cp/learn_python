from collections import deque
# Create a dequeue with deque()
# Add items to the right with q.append()
# Remove from the left with with q.popleft() 

# In this graph, using BFS you should go through 0, 1, and 2 on the way.
# So, 'visited' will be {0, 1, 2}.
graph = [
    [0, 1],
    [2, 3],
    [3],
    [0]
]

def bfs(graph, initial, target):
    visited = set()
    parent = {}
    to_visit = deque()
    while to_visit:
        current = get_next(to_visit)
        if current is target:
            return path_to_end(parent, current, source)
        if current not in visited:
            visited.add(current)
            neighbours = graph[current]         
            for neighbour in neighbours:
                if neighbour not in parent:
                    parent[neighbour] = current
                add_node(to_visit, neighbour)
    pass

def path_to_end(parents, current, source):
    if current == source:
        return [source]
    else:
        return path_to_end(parents, parents[current], source) + [current]


