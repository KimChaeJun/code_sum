import sys
sys.stdin = open('5204_input.txt', 'r')
##########################


def merge(l_arr, r_arr):
    global cnt
    tmp = []
    l_idx, r_idx = 0, 0
    if l_arr[-1] > r_arr[-1]:
        cnt += 1
    while l_idx < len(l_arr) and r_idx < len(r_arr):
        if l_arr[l_idx] < r_arr[r_idx]:
            tmp.append(l_arr[l_idx])
            l_idx += 1
        else:
            tmp.append(r_arr[r_idx])
            r_idx += 1
    tmp.extend(l_arr[l_idx:])
    tmp.extend(r_arr[r_idx:])
    return tmp


def m_sort(m_arr):
    n = len(m_arr)
    if n <= 1:
        return m_arr
    arr_mid = n // 2
    left = m_sort(m_arr[:arr_mid])
    right = m_sort(m_arr[arr_mid:])
    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = m_sort(arr)
    print(f"#{tc} {arr[N//2]} {cnt}")
