import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

lst = []
visited = [0 for _ in range(N+1)]
def dfs():
    if len(lst) == M:
        return print(*lst)
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        lst.append(nums[i])
        dfs()
        visited[i] = 0
        lst.pop()

dfs()