import sys
sys.stdin = open('sample_input.txt', 'r')
##########################
from collections import deque
T = int(input())
for tc in range(1, T+1):
    K = int(input())
    N = 4
    RIGHT_POS, LEFT_POS, ARROW_POS = 2, 6, 0
    magnet = [deque(list(map(int, input().split()))) for _ in range(N)]
    rotate = [list(map(int, input().split())) for _ in range(K)]
    score = 0
    for mn, rd in rotate:
        visited = [False] * N
        queue = deque([[mn-1, rd]])
        visited[mn-1] = True
        while queue:
            mag_idx, r = queue.popleft()
            if mag_idx != N-1:
                if magnet[mag_idx][RIGHT_POS] != magnet[mag_idx+1][LEFT_POS]:
                    if not visited[mag_idx+1]:
                        queue.append([mag_idx+1, -r])
                        visited[mag_idx+1] = True
            if mag_idx != 0:
                if magnet[mag_idx][LEFT_POS] != magnet[mag_idx-1][RIGHT_POS]:
                    if not visited[mag_idx-1]:
                        queue.append([mag_idx-1, -r])
                        visited[mag_idx-1] = True
            if r == 1:
                magnet[mag_idx].rotate(1)
            else:
                magnet[mag_idx].rotate(-1)
    for idx, mag in enumerate(magnet):
        if not mag[ARROW_POS]:
            continue
        score += (2**idx)
    print(f"#{tc} {score}\n")
#############################################################################
# def rotate_magnet(mag, rot, check):
#     if check[mag] == 1 or check[mag] == -1:
#         return
#     check[mag] = rot
#     if mag == 0:
#         if magnet[mag][2] != magnet[mag+1][6]:
#             rotate_magnet(mag+1, -rot, check)
#     elif mag == 3:
#         if magnet[mag][6] != magnet[mag-1][2]:
#             rotate_magnet(mag-1, -rot, check)
#     else:
#         if magnet[mag][2] != magnet[mag+1][6]:
#             rotate_magnet(mag+1, -rot, check)
#         if magnet[mag][6] != magnet[mag-1][6]:
#             rotate_magnet(mag-1, -rot, check)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     magnet = [deque(list(map(int, input().split()))) for _ in range(4)]
#     rotate = [list(map(int, input().split())) for _ in range(N)]
#     score = 0
#     for magnet_n, rotate_dir in rotate:
#         visited = [0] * 4
#         rotate_magnet(magnet_n-1, rotate_dir, visited)
#         for i, v in enumerate(visited):
#             if v != 0:
#                 magnet[i].rotate(v)
#     print(f"#{tc} {score}")
