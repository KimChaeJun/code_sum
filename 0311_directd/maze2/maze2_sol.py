import sys
sys.stdin = open('input.txt', 'r')
##########################
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(dfs_i, dfs_j):
    global cnt, visited
    visited[dfs_i][dfs_j] = True
    if matrix[dfs_i][dfs_j] == 3:
        return
    gp = 100*dfs_i+dfs_j+1
    for adj_i, adj_j in graph[gp]:
        adj_gp = 100*adj_i+adj_j+1
        if not graph[adj_gp]:
            visited[adj_i][adj_j] = True
        if not visited[adj_i][adj_j]:
            cnt.append(matrix[adj_i][adj_j])
            dfs(adj_i, adj_j)


def delta_dict(di, dj):
    global graph
    start_v = 100 * di + dj + 1
    for dx, dy in dxy:
        ni, nj = di + dx, dj + dy
        if ni in range(100) and nj in range(100):
            if start_v not in graph.keys():
                graph[start_v] = []
            graph[start_v].append([ni, nj])


T = 1
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(100)]
    visited = [[False]*100 for _ in range(100)]
    start_pos_i, start_pos_j = 0, 0
    graph = {}
    cnt = []
    for i in range(100):
        for j in range(100):
            if matrix[i][j] == 2:
                start_pos_i, start_pos_j = i, j
            delta_dict(i, j)
    dfs(start_pos_i, start_pos_j)
    print(f"#{tc} {cnt}")
