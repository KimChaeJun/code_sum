import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
##########################
dxy = [[1, 0], [-1, 0], [0, -1], [0, 1]]


def get_road_move_time(r, n, m):
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    queue = deque([0, 0, 0])
    while queue:
        x, y, dist = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            n_dist = dist + 1
            if nx not in range(n) or ny not in range(m):
                continue
            if visited[nx][ny]:
                continue
            if road[nx][ny] == 0:
                continue
            queue.append([nx, ny, n_dist])
            if nx == n-1 and ny == m-1:
                return n_dist
    return -1


N, M = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
print(road)
res = get_road_move_time(road, N, M)
print(res)
