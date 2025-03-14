import sys
sys.stdin = open('sample_input.txt', 'r')
##########################
import itertools
T = int(input())    # 테스트 케이스 받아오는 코드
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for fs_i in range(N):
        for fs_j in range(N-M+1):
            fs_honey = matrix[fs_i][fs_j:fs_j+M]
            fs_honey_max = 0
            for sel in range(1, M+1):
                combs = itertools.combinations(fs_honey, sel)
                fs_comb_max = 0
                for comb in combs:
                    if sum(comb) > C:
                        continue
                    res = 0
                    for c in comb:
                        res += (c**2)
                fs_comb_max = max(res, fs_comb_max)
                fs_honey_max = max(fs_honey_max, fs_comb_max)
            for nd_i in range(fs_i, N):
                for nd_j in range(N-M+1):
                    if fs_i == nd_i and nd_j < fs_j + M:
                        continue
                    nd_honey = matrix[fs_i][fs_j:fs_j + M]
                    nd_honey_max = 0
                    for sel in range(1, M + 1):
                        combs = itertools.combinations(nd_honey, sel)
                        nd_comb_max = 0
                        for comb in combs:
                            if sum(comb) > C:
                                continue
                            res = 0
                            for c in comb:
                                res += (c ** 2)
                        nd_comb_max = max(res, nd_comb_max)
                        nd_honey_max = max(nd_honey_max, nd_comb_max)
                    max_sum = max(max_sum, fs_honey_max + nd_honey_max)
    print(f"#{tc} {max_sum}")
