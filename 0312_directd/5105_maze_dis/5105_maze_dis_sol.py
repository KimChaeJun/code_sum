import sys
sys.stdin = open('5105_input.txt', 'r')
##########################
from collections import deque
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(r, n, m):
    queue = deque([[n, m]])
    distance = [[-1] * N for _ in range(N)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx in range(N) and ny in range(N) and r[nx][ny] != '1' and distance[nx][ny] == -1:
                queue.append([nx, ny])
                distance[nx][ny] = distance[x][y] + 1
                if r[nx][ny] == '3':
                    return distance[nx][ny]
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [str(input()) for _ in range(N)]
    start_pos_x, start_pos_y = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start_pos_x, start_pos_y = i, j
    res = bfs(maze, start_pos_x, start_pos_y)
    print(f"#{tc} {res}")

