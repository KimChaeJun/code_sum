import sys
sys.stdin = open('5207_input.txt', 'r')
##########################


def binary_search(arr, st, end, key):
    global cnt
    if st > end:
        return -1
    else:
        mid = (st + end) // 2
        if key == arr[mid]:
            cnt += 1
            if len(arr[:mid]):
                return binary_search(arr, st, mid - 1, key)
            elif len(arr[mid:]):
                return binary_search(arr, mid + 1, end, key)
        elif key < arr[mid]:
            return binary_search(arr, st, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, end, key)


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
    N, M = map(int, input().split())
    listA = m_sort(list(map(int, input().split())))
    listB = m_sort(list(map(int, input().split())))
    cnt = 0
    if N < M:
        for i in range(N):
            binary_search(listB, 0, M-1, listA[i])
    else:
        for i in range(M):
            binary_search(listA, 0, N-1, listB[i])
    print(f"#{tc} {cnt}")
