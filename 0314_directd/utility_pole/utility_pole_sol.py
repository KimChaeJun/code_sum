import sys
sys.stdin = open('input.txt', 'r')
##########################
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pole, res = [], 0
    for _ in range(N):
        st, end = map(int, input().split())
        for x, y in pole:
            if st < x and end > y or st > x and end < y:
                res += 1
        pole.append([st, end])
    print(f"#{tc} {res}")
