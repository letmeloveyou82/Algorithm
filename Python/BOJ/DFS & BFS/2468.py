import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
high = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] > high:
            high = graph[i][j]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
queue = deque()

def bfs(i, j, high):
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] > high and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))


result = 0
for h in range(high):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] > h and visited[i][j] == 0:
                bfs(i, j, h)
                cnt += 1

    if result < cnt: # 최댓값 갱신
        result = cnt

print(result)