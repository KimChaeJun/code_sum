import sys
sys.stdin = open('sample_input.txt', 'r')
##########################


def kcal_check(idx, taste_sum, kcal_sum):
    global res
    if idx >= N:
        if kcal_sum <= max_kcal:
            res = max(res, taste_sum)
        return
    kcal_check(idx+1, taste_sum, kcal_sum)
    kcal_check(idx+1, taste_sum + ingredient[idx][0], kcal_sum + ingredient[idx][1])


T = int(input())
for tc in range(1, T+1):
    N, max_kcal = map(int, input().split())
    ingredient = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    kcal_check(0, 0, 0)
    print(f"#{tc} {res}")
