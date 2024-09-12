import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
max_result = -int(1e9)
min_result = int(1e9)

def dfs(depth, val, plus, minus, multiply, divide):
    global max_result, min_result
    if depth == N:
        if max_result < val:
            max_result = val
        if min_result > val:
            min_result = val
        return

    if plus:
        dfs(depth+1, val+num[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, val-num[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, val*num[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(val/num[depth]), plus, minus, multiply, divide-1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(max_result)
print(min_result)