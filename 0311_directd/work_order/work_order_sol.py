import sys
sys.stdin = open('sample_input.txt', 'r')
##########################
from collections import deque
T = 10
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    graph = {}
    for i in range(M):
        graph.setdefault(data[2*i], []).append(data[2*i+1])
    in_degree = [0] * (N + 1)
    print(in_degree)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    print(in_degree)
    queue = deque()
    for i in range(1, N+1):
        if in_degree[i] == 0:
            queue.append(i)
    print(queue)
    res = []
    while queue:
        node = queue.popleft()
        res.append(node)
        print(graph[node])
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(res) != N:
        print('find cycle')
    print(f"#{tc}", *res)
