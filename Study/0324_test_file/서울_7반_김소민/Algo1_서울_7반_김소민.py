
def snack(idx, res_cnt, res_cal):
    global min_cnt, res_cals
    #가지 치기
    if res_cnt >= min_cnt: #현 개수가 최소 개수보다 많을 때 더 볼 필요 없음
        return

    if res_cal >= m: # 현재 칼로리가 최소 칼로리보다 높거나 같을 때
        min_cnt = min(res_cnt, min_cnt) # 최소 개수 갱신
        res_cals.append(res_cal)

    if idx == n: #모든 요소를 고르거나 고르지 않았을 때
        return

    snack(idx + 1, res_cnt + 1, res_cal + cals[idx]) # 선택 o
    snack(idx + 1, res_cnt, res_cal) # 선택 x


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    cals = list(map(int, input().split()))
    min_cnt = float('inf')
    res_cals = []
    res_snack = snack(0, 0, 0)
    res = res_snack if res_snack != None else -1
    print(f"#{tc} {res}")

