import sys
sys.stdin = open('algo2_sample_in.txt', 'r')
##########################
from collections import deque
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(bi, bj):
    global res
    queue = deque([(bi, bj)])
    visited[bi][bj] = True
    tmp = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            # if visited[nx][ny]: continue
            # if 0 <= nx < N: continue
            # if 0 <= ny < M: continue
            # if planet[nx][ny]: continue
            # visited[nx][ny] = True
            # queue.append((nx, ny))
            # tmp += 1
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not planet[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                tmp += 1
    if tmp >= L:
        res += 1


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    planet = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    res = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] or planet[i][j]:
                continue
            bfs(i, j)
    print(f"#{tc} {res}")
