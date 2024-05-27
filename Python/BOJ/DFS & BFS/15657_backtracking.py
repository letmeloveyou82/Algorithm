import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def dfs(start, lst):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(start, N):
        lst.append(nums[i])
        dfs(i, lst)
        lst.pop()

dfs(0, [])