import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
tmp = []

def dfs():
    if len(tmp) == M:
        print(*tmp)
        return
    for i in range(N):
        tmp.append(nums[i])
        dfs()
        tmp.pop()

dfs()