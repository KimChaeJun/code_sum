import sys
sys.stdin = open('input.txt', 'r')

##########################
T = 10
for tc in range(1, T+1):
    N, pw_arr = input().split()
    stack = []
    for ch in pw_arr:
        if not stack:
            stack.append(ch)
            continue
        if stack[-1] == ch:
            stack.pop()
            continue
        stack.append(ch)
    print(f"#{tc}", ''.join(stack))
