import sys
sys.stdin = open('input.txt', 'r')
##########################
# 테스트 케이스 받아오는 코드
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    res = []
    for i in range(N):
        if i < 2:
            tmp = [1] * (i+1)
        else:
            tmp = [1] + [res[i-1][j] + res[i-1][j-1] for j in range(1, i)] + [1]
        res.append(tmp)
    print(f"#{tc}")
    for i in range(N):
        print(*res[i])
