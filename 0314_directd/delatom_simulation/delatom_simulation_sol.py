import sys
sys.stdin = open('sample_input.txt', 'r')
##########################
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [[0]*2000 for _ in range(2000)]
    atoms_info = [list(map(int, input().split())) for _ in range(N)]
    for x, y, direction, power in atoms_info:
        atom = (direction, power)
        matrix[x][y] = atom

