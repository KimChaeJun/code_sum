import sys
sys.stdin = open('input.txt', 'r')
##########################
from collections import deque
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs():
    queue = deque([[1, 1]])
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx in range(length) and ny in range(length):
                if maze[nx][ny] != '1' and not road[nx][ny]:
                    queue.append([nx, ny])
                    road[nx][ny] = True
                    if maze[nx][ny] == '3':
                        return 1
    return 0


T = 10
for tc in range(1, T+1):
    N = int(input())
    length = 16
    maze = [str(input()) for _ in range(length)]
    road = [[False]*length for _ in range(length)]
    road[1][1] = True
    res = bfs()
    print(f"#{tc} {res}")
