import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
result = int(1e9)

# 백트래킹 사용
def dfs(start, now, cost, cnt):
    if cnt == N:
        if graph[now][start]:
            global result
            result = min(result, cost + graph[now][start])
        return

    if cost > result:
        return

    for i in range(N):
        if graph[now][i] != 0 and visited[i] == 0:
            visited[i] = 1
            dfs(start, i, cost+graph[now][i], cnt+1)
            visited[i] = 0

for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0

print(result)