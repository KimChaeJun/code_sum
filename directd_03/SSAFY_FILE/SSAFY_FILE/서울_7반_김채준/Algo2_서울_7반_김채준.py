import sys
sys.stdin = open("algo2_sample_in.txt", "r")
#############################################
'''
가능한 조합들 중에 내부 요소가 겹치지 않게끔 만들어야한다.
따라서 부분조합으로 문제를 해결한다. 
'''
T = int(input())    # test_case 개수를 받아옴
for tc in range(1, T+1):
    # 입력값
    # N : 과일나무의 개수 / X : 목표 수확량
    # fruits : 각 과일나무의 수확량 / works : 각 과일나무 수확을 위해 쓰이는 노동력
    N, X = map(int, input().split())
    fruits = list(map(int, input().split()))
    works = list(map(int, input().split()))
    # 부분조합 중 조건에 맞는 경우의 노동력 합을 모을 배열
    arr_works = []
    # 비트연산을 활용한 부분집합
    for i in range(2**N):
        # 경우의 수마다 각각의 값을 임시로 저장할 배열들
        fruits_comb, works_comb = [], []
        for j in range(N):
            # 나올 수 있는 경우의 수 자리에 있는 값을 배열에 추가
            # 좌측 시프트로 비교중이기 때문에, fruits와 works의 끝값부터 가져오게 설정
            if i & (1 << j):
                fruits_comb.append(fruits[N-j-1])
                works_comb.append(works[N-j-1])
        # 총 수확량이 목표치 이상일때만,
        if sum(fruits_comb) >= X:
            # 총 노동력의 합을 arr_works에 저장
            arr_works.append(sum(works_comb))
    # len(arr_works)가 0인 경우는, 모든 경우의 수에서 수확량이 목표치를 못 넘은 것임
    # 따라서 len(arr_works)가 0이 아닐때만 arr_works 값 중 최소값을 출력하고,
    # len(arr_works)가 0일 경우, -1을 출력한다
    print(f"#{tc} {min(arr_works) if len(arr_works) else -1}")
