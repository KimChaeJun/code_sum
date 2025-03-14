import sys
sys.stdin = open("algo1_sample_in.txt", "r")

#############################################
'''
이동 후에 연료 양이 0보다 작으면 움직일 수 없음
편한 비교를 위해 while문과 deque 활용
'''
from collections import deque
T = int(input())    # test_case 개수를 받아옴
for tc in range(1, T+1):
    # 입력값 저장
    # N : 나루터 개수, M : 출발 나루터 (index 기준)
    # charges : 나루터에서 충전하는 모터 전력 (+)
    # costs : 이 나루터로 오기 위해 필요한 모터 전력 (-)
    N, M = map(int, input().split())
    charges = deque(map(int, input().split()))
    costs = deque(map(int, input().split()))
    # 둘다 비교하기 용이하게 하기 위해 M번 인덱스 값이 0번으로 오게 회전
    for _ in range(M):
        charges.rotate(-1)
        costs.rotate(-1)
    # 보트 시작 시 충전값 설정(출발지의 충전량)
    boat = charges[0]
    # print(charges, costs, boat) # 검증용 코드
    # 출발지로 돌아온 것을 확인하기 위한 변수
    move_cnt = 0
    # 도중에 연료가 모자를 경우를 나타내기 위한 변수
    flag = True
    # 제자리 도착할 때까지 무한루프
    while True:
        # 이동횟수 증가
        move_cnt += 1
        # boat 값을 costs[0] 값만큼 차감
        # 계속 0번 인덱스로 값을 가져오기 위해 costs를 회전시킴
        boat -= costs[0]
        costs.rotate(-1)
        # print(boat) # 검증용 코드
        # 만약 연료가 모잘라서 움직일 수 없다면,
        if boat < 0:
            # 중도에 멈춘 것을 알리고 무한루프 종료
            flag = False
            break
        # 만약 이동 완료 후 위치가 처음 시작 위치이면,
        if move_cnt >= N:
            # 무한반복 종료
            break
        # 여기까지 온것은 아직 시작지점이 아니지만, 정상적으로 도착했음을 의미
        # 도착위치의 충전량을 더해줘야 하기 때문에 먼저 charges.rotate(-1) 실행
        # 아직 제자리가 아니기 때문에 boat 값에 charges[0] 값만큼 더해줌
        charges.rotate(-1)
        boat += charges[0]
        # print(boat) # 검증용 코드
    # 중도에 멈추지 않았으면 boat 값을, 멈췄으면 -1을 출력함
    print(f"#{tc} {boat if flag else -1}")
