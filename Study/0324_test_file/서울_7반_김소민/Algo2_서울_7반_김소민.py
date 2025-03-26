dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def find_start(field):   #시작점 찾으면서 주변 칸 탐색해서 또 0이 있다면 처음 시작점 반환
    for row in range(n):
        for col in range(m):
            if field[row][col] == 0:
                for idx in range(4):
                    nrow = row + dx[idx]
                    ncol = col = dy[idx]
                    if 0 <= nrow < n and 0 <= ncol < m and field[nrow][ncol] == 0:
                        return row, col
    return None, None #
def find_island(field):
    global cnt
    if 0 in field:
        srow, scol = find_start(field)
        if srow == None and scol == None:
            cnt += 0
        else:
            stack = [(srow, scol, 1)]
            while stack:
                cur_row, cur_col, cnn = stack.pop()
                for idx in range(4):
                    nrow = cur_row + dx[idx]
                    ncol = cur_col = dy[idx]
                    if 0 <= nrow < n and 0 <= ncol < m and field[nrow][ncol] == 0:
                        stack.append((nrow, ncol, cnn + 1))
                        field[nrow][ncol] = 1
            if cnn >= minimum: #한 시작점과 이어진 땅을 모두 탐색 완료할 때마다 최소 지형 이상이라면 카운트 증가
                cnt += 1
    else:
        return

T = int(input())
for tc in range(1, T+1):
    n, m, minimum = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    print(f"#{tc} {cnt}")