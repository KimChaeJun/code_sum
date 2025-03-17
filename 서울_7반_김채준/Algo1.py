import sys
sys.stdin = open('algo1_sample_in.txt', 'r')
############################################
# BFS 구현을 위한 모듈 호출
from collections import deque
# 델타 탐색을 위한 변수 선언
dxy = [[0, 1], [0, -1], [-1, 0], [1, 0]]


# 최단 경로 탐색을 위한 함수
def bfs(di, dj):
    # 시작좌표 방문처리
    visited[di][dj] = True
    # 좌표값과 레벨을 파악하기위한 변수를 저장
    # 시작 좌표도 경로 길이에 포함해야하기 때문에 레벨 초기값은 1로 설정
    queue = deque([[di, dj, 1]])
    # 조건부 무한루프 시작
    while queue:
        x, y, n = queue.popleft()
        # 좌표값이 도착지점일 경우, 현재 레벨 값을 return
        if matrix[x][y] == 4:
            return n
        # 방문 처리
        visited[x][y] = True
        # 델타 탐색 시작
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            # 다음 좌표가 N * N 범위 내이고, 장애물이 아니고, 방문한 적이 없다면,
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != 1 and not visited[nx][ny]:
                # 조건에 충족한 델타 좌표값과 자신 레벨값을 저장
                queue.append([nx, ny, n+1])
    # 여기까지 왔다는 것은 도착지점에 갈 수 없다는 의미임
    # 따라서, -1을 반환
    return -1


# Test case 개수를 받아오는 코드
T = int(input())
for tc in range(1, T + 1):
    # N : 식당 크기, matrix : 식당 정보, visited : 방문 확인용
    # start_x, start_y : 시작 지점의 좌표
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    start_x, start_y = 0, 0
    # 시작 지점 탐색, 발견 후 start_x, start_y에 저장
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 3:
                start_x, start_y = i, j
                break
            else:
                continue
    # BFS로 최단경로 탐색 시작
    res = bfs(start_x, start_y)
    # 결과값 출력
    print(f"#{tc} {res}")
