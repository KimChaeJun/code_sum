import sys
sys.stdin = open('input.txt', 'r')

##########################
bin_dict = {'0001101': 0,
            '0011001': 1,
            '0010011': 2,
            '0111101': 3,
            '0100011': 4,
            '0110001': 5,
            '0101111': 6,
            '0111011': 7,
            '0110111': 8,
            '0001011': 9}
T = int(input()) # 테스트 케이스 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(str, input().strip())) for _ in range(N)]
    bin_code = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '1' and '1' not in matrix[i][j+1:M]:
                bin_code += matrix[i][j-55:j+1]
                break
        if len(bin_code):
            break
    bin_code_arr = []
    for i in range(0, 56, 7):
        tmp = ''.join(bin_code[i:i+7])
        bin_code_arr.append(bin_dict.get(tmp))
    res = sum([bin_code_arr[i] for i in range(8) if i % 2 == 0]) * 3
    res += sum([bin_code_arr[i] for i in range(8) if i % 2 == 1])
    print(f"#{tc} {0 if res % 10 else sum(bin_code_arr)}")
    # print(bin_code, len(bin_code))
    # print(bin_code_arr)
    # print(res)
