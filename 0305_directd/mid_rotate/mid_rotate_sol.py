import sys
sys.stdin = open('input.txt', 'r')

##########################


def make_tree(arrs):
    res = {}
    for arr in arrs:
        res[arr[0]] = arr[1]
    return res


def in_oder(v_tree, c_n):
    global res
    if str(c_n) not in v_tree.keys():
        return
    in_oder(v_tree, c_n*2)
    res += v_tree.get(str(c_n))
    in_oder(v_tree, c_n*2+1)


# 테스트 케이스 받아오는 코드
T = 10
for tc in range(1, T+1):
    N = int(input())
    tree_in = [list(input().split()) for _ in range(N)]
    tree = make_tree(tree_in)
    res = ''
    in_oder(tree, 1)
    print(f"#{tc} {res}")


