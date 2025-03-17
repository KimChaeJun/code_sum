import sys
sys.stdin = open('algo2_sample_in.txt', 'r')
############################################


# 복합 선택을 하면서 비교하기 위해 DFS 사용
def dfs(songs_idx, time_sum, cnt):
    global res
    # L개 이하의 노래로 M분 이상의 재생 길이가 나왔을 때
    if time_sum >= M and cnt <= L:
        # res에 저장된 값과 time_sum 값을 비교하여 더 작은 값을 res에 저장
        res = min(res, time_sum)
    # 제일 끝 인덱스까지 도달할 때, 재귀 종료
    if songs_idx >= N:
        return
    # 곡을 선택했을 때와 선택하지 않았을 때의 재귀를 별도 시행
    # 곡을 선택했을 때만 cnt 값을 1씩 증가시킴
    dfs(songs_idx + 1, time_sum + song_time[songs_idx], cnt + 1)
    dfs(songs_idx + 1, time_sum, cnt)


T = int(input())    # Test case 개수를 받아오는 코드
for tc in range(1, T + 1):
    # N : 곡 수 / M : 최소 재생시간 / L : 곡 선택 가능 수
    N, M, L = map(int, input().split())
    # 곡 별 재생시간(분)
    song_time = list(map(int, input().split()))
    # 최솟값 저장을 위해 임의로 제일 큰 수 지정
    res = float('inf')
    # DFS 실행
    dfs(0, 0, 0)
    # 초기값과 동일할 경우 -1 출력, 그 외에는 res 출력
    print(f"#{tc} {res if res != float('inf') else -1}")
