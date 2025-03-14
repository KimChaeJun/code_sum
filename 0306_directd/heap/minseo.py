import sys
sys.stdin = open('input.txt', 'r')
##################################################


# 힙을 만드는 클래스
# 연산 1: 힙에 삽입하는 함수

# 연산2
def calculate2():
    pass


# Test case 개수를 받아오는 코드
# 가끔 10번 돈다고 하면 int(input())이 아니라 그냥 정수 10 적어주기
T = int(input())
for tc in range(1, T + 1):
    maxheap=[]
    # 쿼리문 길이 입력받기
    querylen = int(input())
    # 쿼리문 입력받아 배열에 저장
    querys = [list(map(int, input().split())) for _ in range(querylen)]
    result = []
    for idx in range(querylen):
        if querys[idx][0] == 1:
            query1 = querys[idx]
            maxheap.append(query1[1])
        else:
            # 연산 2인 경우 최대 힙 삭제하고 루트값을 가져오는 함수 실행
            if not maxheap:
                result.append(-1)
                continue
            result.append(maxheap[0])
            calculate2()
            # print(result)
    print(f"#{tc} {result[0]} {result[1]}")
