import sys
sys.stdin = open('4875_input.txt', 'r')
##########################
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(dfs_i, dfs_j):
    global cnt
    visited[dfs_i][dfs_j] = True
    if matrix[dfs_i][dfs_j] == 3:
        return
    for adj_i, adj_j in graph[N*dfs_i+dfs_j+1]:
        if not visited[adj_i][adj_j]:
            cnt += matrix[adj_i][adj_j]
            dfs(adj_i, adj_j)


def delta_dict(di, dj):
    global graph
    start_v = N * di + dj + 1
    if start_v not in graph.keys():
        graph[start_v] = []
    for dx, dy in dxy:
        ni, nj = di + dx, dj + dy
        if ni in range(N) and nj in range(N) and matrix[ni][nj] != 1:
            graph[start_v].append([ni, nj])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    start_pos_i, start_pos_j = 0, 0
    graph = {}
    cnt = 2
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                start_pos_i, start_pos_j = i, j
            delta_dict(i, j)
    dfs(start_pos_i, start_pos_j)
    print(f"#{tc} {0 if cnt % 5 else 1}")
