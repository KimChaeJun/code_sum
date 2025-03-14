import sys
sys.stdin = open('input.txt', 'r')
##########################
'''
파스칼 공식(이항정리)
nCr (r = 0 ~ n)이 n번째 항에 모두 한줄로 출력되어야한다.
'''
import itertools
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f"#{tc}")
    for i in range(N):
        res = []
        for j in range(0, i+1):
            combs = list(itertools.combinations(list(range(1, i+1)), j))
            res.append(len(combs))
        print(*res)
