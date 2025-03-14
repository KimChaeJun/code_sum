import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
##########################
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def get_road_move_time(r, n, m):
    queue = deque([0, 0])
    distance = [[[-1] * m] for _ in range(n)]
    distance[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx in range(n) and ny in range(m) and not road[nx][ny] and distance[nx][ny] == -1:
                queue.append([nx, ny])
                distance[nx][ny] = distance[x][y] + 1
                if nx == n-1 and ny == m-1:
                    return distance[nx][ny]
    return -1


N, M = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
res = get_road_move_time(road, N, M)
print(res)
