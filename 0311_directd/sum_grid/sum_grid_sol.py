import sys
sys.stdin = open('sample_input.txt', 'r')
##########################


def search_7(n, tmp):
    global res
    tmp_len = len(tmp)
    if tmp_len == 7:
        res.append(tmp)
        return
    for node_x, node_y in graph[n]:
        if not visited[node_x][node_y]:
            nn = node_x * 4 + node_y + 1
            search_7(nn, tmp + f'{grid[node_x][node_y]}')


dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
T = int(input())
for tc in range(1, T+1):
    grid = [list(map(int, input().split())) for _ in range(4)]
    graph = {}

    res = []
    for i in range(4):
        for j in range(4):
            key = 4*i+j+1
            for dx, dy in dxy:
                idx, jdy = i + dx, j + dy
                if idx in range(4) and jdy in range(4):
                    graph.setdefault(key, []).append([idx, jdy])
    for i in range(1, 17):
        visited = [[False] * 4 for _ in range(4)]
        search_7(i, '')
    res_len = len(list(set(res)))
    print(f"#{tc} {res_len}")
