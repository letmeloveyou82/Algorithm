import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
tmp = []

def dfs(start):
    if len(tmp) == M:
        print(*tmp)
        return
    remember = 0
    for i in range(start, N):
        if remember != nums[i]:
            tmp.append(nums[i])
            remember = nums[i]
            dfs(i)
            tmp.pop()
dfs(0)