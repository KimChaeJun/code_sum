import sys
sys.stdin = open('input.txt', 'r')
##########################
# 입력
# 스위치 개수
N = int(input())
# 스위치 상태
switch = list(map(int, input().split()))
# 학생 수
student = int(input())
# 학생 수만큼 반복
for _ in range(student):
    # gd = 성별, ctrl = 동작할 기준 스위치
    gd, ctrl = map(int, input().split())
    # 남학생일 때
    if gd == 1:
        # 리스트 0번까지 다 쓰기 때문에, ctrl-1로 시작해서 ctrl 값만큼 점프
        for i in range(ctrl-1, N, ctrl):
            # 내부 값 반전
            switch[i] = switch[i] ^ 1
    # 여학생일 때
    if gd == 2:
        # 지정된 번호는 항상 반전
        switch[ctrl-1] = switch[ctrl-1] ^ 1
        # 범위 변경을 위한 변수
        i = 1
        # 무한루프 시작
        while True:
            # 좌, 우로 1칸씩 늘려가며 탐지할 좌표값
            left, right = ctrl - i - 1, ctrl + i - 1
            # index out of range 감지 시
            if left < 0 or right > N - 1:
                # 무한루프 종료
                break
            # 통과했으면 i값 증가
            i += 1
            # switch[left]와 switch[right]가 같으면
            if switch[left] == switch[right]:
                # 값을 XOR 연산하여 저장
                switch[left], switch[right] = switch[left] ^ 1, switch[right] ^ 1
            # switch[left]와 switch[right]가 다르면
            else:
                # 무한루프 종료
                break
# 20자리씩 끊어서 출력하기 위한 반복문
for i in range(0, N, 20):
    print(*switch[i:i+20])
