import sys
sys.stdin = open('sample_input.txt', 'r')
##########################
T = int(input()) # 테스트 케이스 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    statement = [0] * 200
    for _ in range(N):
        v1, v2 = map(int, input().split())
        st, end = min(v1, v2), max(v1, v2)
        road = abs(st // 2 - end // 2)
        for i in range(st // 2, road):
            statement[i] += 1
    print(f"#{tc} {max(statement) + 1}")
