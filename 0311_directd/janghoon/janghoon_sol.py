import sys
sys.stdin = open('input.txt', 'r')
##########################
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     max_len = 2 ** N
#     res = 10000 * N
#     for i in range(max_len):
#         tmp = []
#         for j in range(N):
#             if i & (1 << j):
#                 tmp.append(arr[N-j-1])
#         tmp_sum = sum(tmp)
#         if tmp_sum == M:
#             res = tmp_sum
#             break
#         if tmp_sum >= M:
#             res = min(res, tmp_sum)
#     print(f"#{tc} {abs(res-M)}")


def dfs(idx, h_sum):
    global res
    if h_sum >= res:
        return
    if idx == N:
        if h_sum >= M:
            res = min(res, h_sum)
        return
    dfs(idx+1, h_sum+arr[idx])
    dfs(idx+1, h_sum)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    res = float('inf')
    dfs(0, 0)
    print(f"#{tc} {abs(res-M)}")
