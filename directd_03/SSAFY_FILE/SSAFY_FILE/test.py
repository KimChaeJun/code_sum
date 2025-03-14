import sys
sys.stdin = open("input.txt", "r")

#############################################
import itertools
T = int(input())    # test_case 개수를 받아옴
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    perm = list(itertools.permutations(arr))
    comb = list(itertools.combinations(arr, 3))
    print(f"perm = {perm} {len(perm)}")
    print(f"comb = {comb}")
