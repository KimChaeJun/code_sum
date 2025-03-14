import sys
sys.stdin = open('input.txt', 'r')

##########################


def make_tree(arr_in):
    res = {}
    for i in range(0, len(arr_in), 2):
        k, v = arr_in[i], arr_in[i+1]
        if k not in res.keys():
            res[k] = []
        res[k].append(v)
    return res


def pre_oder(v_tree, c_n):
    global pre_res
    if str(c_n) not in v_tree.keys():
        return
    pre_res += v_tree.get(str(c_n))
    pre_oder(v_tree, c_n*2)
    pre_oder(v_tree, c_n*2+1)


def in_oder(v_tree, c_n):
    global in_res
    if str(c_n) not in v_tree.keys():
        return
    in_oder(v_tree, c_n*2)
    in_res += v_tree.get(str(c_n))
    in_oder(v_tree, c_n*2+1)


def post_oder(v_tree, c_n):
    global post_res
    if str(c_n) not in v_tree.keys():
        return
    post_oder(v_tree, c_n*2)
    post_oder(v_tree, c_n*2+1)
    post_res += v_tree.get(str(c_n))


N = int(input())
arr = list(map(str, input().split()))
tree = make_tree(arr)
print(tree)
# pre_res, in_res, post_res = '', '', ''
# pre_oder(tree, 1)
# in_oder(tree, 1)
# post_oder(tree, 1)
# print(pre_res)
# print(in_oder)
# print(post_oder)
