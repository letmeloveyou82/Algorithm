import sys

def dfs(lst, start):
    for i in lst[start]:
        if not visited[i]:
            visited[i] = True
            dfs(lst, i)

input = sys.stdin.readline
N = int(input())
M = int(input())
heavy = [[] for _ in range(N)]
light = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split()) # a > b
    heavy[b-1].append(a-1)
    light[a-1].append(b-1)

for i in range(N):
    visited = [False] * N
    visited[i] = True
    dfs(heavy, i)
    dfs(light, i)
    print(visited.count(False))