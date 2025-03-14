import sys
sys.stdin = open('5205_input.txt', 'r')
##########################


def part(p_arr, ps, pe):
    pp = p_arr[ps]
    left = ps + 1
    right = pe
    while True:
        while left <= pe and p_arr[left] < pp:
            left += 1
        while right > ps and p_arr[right] >= pp:
            right -= 1
        if left < right:
            p_arr[left], p_arr[right] = p_arr[right], p_arr[left]
        else:
            break
    p_arr[ps], p_arr[right] = p_arr[right], p_arr[ps]
    return right


def quick_sort(q_arr, s, e):
    if s < e:
        p = part(q_arr, s, e)
        quick_sort(q_arr, s, p-1)
        quick_sort(q_arr, p+1, e)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr) - 1)
    print(f"#{tc} {arr[N//2]}")
