import sys
sys.stdin = open('input.txt', 'r')
##########################
'''
카운트정렬?
'''
T = int(input())
for tc in range(1, T+1):
    client, time, cnt = map(int, input().split())
    arrival_times = list(map(int, input().split()))

    sell, flag = 0, True
    print(f"#{tc} {'Possible' if flag else 'Impossible'}")
