# import sys
# sys.stdin = open('algo1_sample_in.txt', 'r')
####################################################
from collections import deque
'''
주방이 3, 테이블이 4 
최단경로로 이동할 때 지나가는 칸의 개수 출력 
만약 못가면 -1 출력 
'''
def FindStartPoint(matrix,N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 3:
                startpoint = [i,j]
    return startpoint
# BFS로 최단거리를 구하는 함수
def BFS(matrix,N,start):
    # visited 배열을 만들어 체크한다. (똑같은 배열크기로 )
    visited = [[0]*N for _ in range(N)]
    # 시작점을 True로 체크
    visited[start[0]][start[1]] = 1
    #---
    # BFS로 탐색이므로 큐 선언해서 사용
    queue = deque()
    start_x,start_y = start[0],start[1]
    #큐에 값을 넣어주기
    queue.append((start_x,start_y,0))


    # 4방향으로 탐색할 예정
    #dxy 선언
    dxy = [[-1,0],[1,0],[0,-1],[0,1]]
    while queue:
        # 큐의 값을 하나씩 가져오기
        x,y,dist = queue.popleft()
        for dx,dy in dxy:
            nx = x + dx
            ny = y + dy

            #nx,ny가 범위 내인지 탐색
            if 0 <= nx < N and 0 <= ny < N:
                #방문하지 않은 곳인지 확인
                if not visited[nx][ny]:
                    # 방문했다고 체크
                    visited[nx][ny] = 1
                    #만약 0 인 경우(통로라 갈 수 있는 경우)
                    if matrix[nx][ny] == 0:
                        # 큐에 값을 넣어주기
                        queue.append((nx,ny,dist + 1))
                        # x,y = nx,ny

                    elif matrix[nx][ny] == 4:
                        return dist
    return -1

T = int(input())
for test_case in range(1,T+1):
    # N : 배열의 길이 /
    N = int(input())
    matrix =[list(map(int,input().split())) for _ in range(N)]

    #3의 위치를 찾기
    start = FindStartPoint(matrix,N)
    # 4의 위치를 찾는 BFS(가장 짧은 경로 이므로)
    print(f"#{test_case} {BFS(matrix,N,start)}")


