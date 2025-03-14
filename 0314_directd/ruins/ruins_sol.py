import sys
sys.stdin = open('input1.txt', 'r')
##########################
dxy = [[1, 0], [0, 1]]


def counting(x, y, ddx, ddy):
    global cnt
    if x not in range(N) or y not in range(M):
        return
    if matrix[x][y] == 0:
        return
    cnt += 1
    counting(x + ddx, y + ddy, ddx, ddy)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for i in range(N):
        for j in range(M):
            if not matrix[i][j]:
                continue
            for dx, dy in dxy:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny]:
                    cnt = 1
                    counting(nx, ny, dx, dy)
            res = max(res, cnt)
    print(f"#{tc} {res}")


'''
dxy = [[1, 0], [0, 1]]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for i in range(N):
        for j in range(M):
            if not matrix[i][j]:
                continue
            for dx, dy in dxy:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny]:
                    cnt = 2
                    while True:
                        ndx, ndy = nx + dx, ny + dy
                        if 0 <= ndx < N and 0 <= ndy < M and matrix[ndx][ndy]:
                            cnt += 1
                            nx, ny = ndx, ndy
                        else:
                            break
            res = max(res, cnt)
    print(f"#{tc} {res}")
'''