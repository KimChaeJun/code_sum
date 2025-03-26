import sys
sys.stdin = open('algo1_sample_in.txt', 'r')
##########################

'''
def dfs(idx, kcal, cnt):
    global res_dict
    if kcal >= max_kcal:
        res_dict.setdefault(cnt, []).append(kcal)
    if idx == N:
        return
    dfs(idx+1, kcal + kcal_arr[idx], cnt+1)
    dfs(idx+1, kcal, cnt)


T = int(input())
for tc in range(1, T+1):
    N, max_kcal = map(int, input().split())
    kcal_arr = list(map(int, input().split()))
    res_dict = {}
    dfs(0, 0, 0)
    res = min(res_dict.get(min(res_dict.keys()))) if res_dict else -1
    print(f"#{tc} {res}")
'''

'''
def dfs(idx, kcal, cnt):
    global res_kcal, res_cnt
    if kcal >= max_kcal:
        res_kcal.append(kcal)
        res_cnt.append(cnt)
    if idx == N:
        return
    dfs(idx+1, kcal + kcal_arr[idx], cnt+1)
    dfs(idx+1, kcal, cnt)


T = int(input())
for tc in range(1, T+1):
    N, max_kcal = map(int, input().split())
    kcal_arr = list(map(int, input().split()))
    res_kcal, res_cnt = [], []
    dfs(0, 0, 0)
    if res_cnt:
        std_cnt = min(res_cnt)
        res = float('inf')
    else:
        std_cnt = 0
        res = -1
    for i in range(len(res_kcal)):
        if res_cnt[i] == std_cnt:
            res = min(res, res_kcal[i])
    print(f"#{tc} {res}")
'''


def dfs(idx, kcal, cnt):
    global tmp_res
    if kcal >= max_kcal:
        tmp_res[cnt].append(kcal)
    if idx == N:
        return
    dfs(idx+1, kcal + kcal_arr[idx], cnt+1)
    dfs(idx+1, kcal, cnt)


T = int(input())
for tc in range(1, T+1):
    N, max_kcal = map(int, input().split())
    kcal_arr = list(map(int, input().split()))
    tmp_res = [[] for _ in range(11)]
    dfs(0, 0, 0)
    res = -1
    for i in range(1, 11):
        if tmp_res[i]:
            res = min(tmp_res[i])
            break
    print(f"#{tc} {res}")