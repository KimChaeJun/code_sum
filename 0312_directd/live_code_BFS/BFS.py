from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B', 'F'],
    'E': ['B', 'F'],
    'F': ['D', 'E', 'G'],
    'G': ['F']
}
start_node = 'A'
res = []
nodes = list(graph.keys())
visited = [False] * len(nodes)
queue = deque([start_node])
visited[nodes.index(start_node)] = True
while queue:
    vertex = queue.popleft()
    res.append(vertex)
    for neighbor in graph[vertex]:
        neighbor_index = nodes.index(neighbor)
        if not visited[neighbor_index]:
            queue.append(neighbor)
            visited[neighbor_index] = True
print(res)
