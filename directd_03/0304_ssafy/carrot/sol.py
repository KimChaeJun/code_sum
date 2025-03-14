import sys
sys.stdin = open('sample_in.txt', 'r')

##########################

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = sorted(list(map(int, input().split())))
