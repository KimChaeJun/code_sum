import sys
sys.stdin = open('input.txt', 'r')

##########################


def dfs(sv):
    visited[sv] = True
    for adj_v in graph[sv]:
        if not visited[adj_v]:
            res.append(str(adj_v))
            dfs(adj_v)


T = 1
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    visited = [False] * (N+1)
    graph = {}
    res = ['1']
    for i in range(0, M*2, 2):
        start_v, end_v = data[i], data[i+1]
        if start_v not in graph.keys():
            graph[start_v] = []
        if end_v not in graph.keys():
            graph[end_v] = []
        graph[start_v].append(end_v)
        graph[end_v].append(start_v)
    dfs(1)
    print(f"#{tc} {'-'.join(res)}")
