import sys
# sys.stdin = open('sample_input.txt', 'r')
sys.stdin = open('input.txt', 'r')
##########################
dict_code = {
    0: '0001101',
    1: '0011001',
    2: '0010011',
    3: '0111101',
    4: '0100011',
    5: '0110001',
    6: '0101111',
    7: '0111011',
    8: '0110111',
    9: '0001011',
}
# 테스트 케이스 받아오는 코드
T = int(input())
for tc in range(1, T+1):
    print(f"#{tc}")
    N, M = map(int, input().split())
    code_hex = [str(input()) for _ in range(N)]
    code_list = []
    # for i in range(N):
    #     print(code_hex[i])
    #
    for code in code_hex:
        for c in code:
            print(format(int(c, 16), '04b'), end='')
        print()

