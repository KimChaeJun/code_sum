import sys
sys.stdin = open('input.txt', 'r')
##########################
from collections import deque
T = 10
for tc in range(1, T+1):
    N, start = map(int, input().split())
    network = list(map(int, input().split()))
    visited = [False] * 101
    contacts = {}
    res = 0
    for i in range(0, N, 2):
        sv, ev = network[i], network[i+1]
        contacts.setdefault(sv, []).append(ev)
    queue = deque([[start, 0]])
    max_depth = 0
    visited[start] = True
    while queue:
        vertex, depth = queue.popleft()
        if depth > max_depth:
            max_depth = depth
            res = vertex
        elif depth == max_depth:
            res = max(vertex, res)
        for neighbor in contacts.get(vertex, []):
            if not visited[neighbor]:
                queue.append([neighbor, depth+1])
                visited[neighbor] = True
    print(f"#{tc} {res}")

