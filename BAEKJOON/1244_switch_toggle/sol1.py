import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
switch = list(map(int, input().split()))
student = int(input())
for _ in range(student):
    gd, ctrl = map(int, input().split())
    if gd == 1:
        for i in range(ctrl-1, N, ctrl):
            switch[i] = switch[i] ^ 1
    if gd == 2:
        switch[ctrl-1] = switch[ctrl-1] ^ 1
        i = 1
        while True:
            left, right = ctrl - i - 1, ctrl + i - 1
            if left < 0 or right > N - 1:
                break
            i += 1
            if switch[left] == switch[right]:
                switch[left], switch[right] = switch[left] ^ 1, switch[right] ^ 1
            else:
                break
for i in range(0, N, 20):
    print(*switch[i:i+20])
