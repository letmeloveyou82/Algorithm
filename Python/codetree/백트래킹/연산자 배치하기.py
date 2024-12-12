import sys 

def dfs(i, val, pl, mi, mu):
    global minimum, maximum
    if i == n-1:
        minimum = min(minimum, val)
        maximum = max(maximum, val)
        return

    if pl > 0:
        dfs(i+1, val+nums[i+1], pl-1, mi, mu)
    if mi > 0 :
        dfs(i+1, val-nums[i+1], pl, mi-1, mu)
    if mu > 0 :
        dfs(i+1, val*nums[i+1], pl, mi, mu-1)

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
plus, minus, multi = map(int, input().split())

minimum, maximum = int(1e9), int(-1e9)
dfs(0, nums[0], plus, minus, multi)
print(minimum, maximum)