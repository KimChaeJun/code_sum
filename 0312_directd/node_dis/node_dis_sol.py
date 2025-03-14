import sys
sys.stdin = open('5102_input.txt', 'r')
##########################
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = {}
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph.setdefault(v1, []).append(v2)
        graph.setdefault(v2, []).append(v1)
    sv, ev = map(int, input().split())
    res = 0
    visited = [False] * (max(graph.keys()) + 1)
    queue = deque([[sv, 0]])
    while queue:
        vertex, cnt = queue.popleft()
        if vertex == ev:
            res = cnt
            break
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append([neighbor, cnt+1])
    print(f"#{tc} {res}")
