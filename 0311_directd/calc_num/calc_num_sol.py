import sys
sys.stdin = open('sample_input.txt', 'r')
##########################
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    op_sign = list(map(int, input().split()))
    nums = list(map(int, input().split()))

