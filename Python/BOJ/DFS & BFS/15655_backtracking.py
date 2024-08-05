import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

tmp = []

def dfs(start):
    if len(tmp) == M:
        print(*tmp)
        return
    for i in range(start, N):
        tmp.append(nums[i])
        dfs(i+1)
        tmp.pop()

dfs(0)