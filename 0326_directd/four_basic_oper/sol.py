import sys
sys.stdin = open('input.txt', 'r')
##########################
T = 1
for tc in range(1, T+1):
    N = int(input())
    tree = {}
    for _ in range(N):
        value = list(map(str, input().split()))
        for i in range(1, len(value)):
            tree.setdefault(value[0], []).append(value[i])
            tree.setdefault(value[i], []).append(value[0])
    print(tc, tree)
