import sys
from collections import deque 
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
painting = 0
max_area = 0

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    graph[i][j] = -1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                cnt += 1
                graph[nx][ny] = -1
                q.append((nx, ny))
    return cnt

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            result = bfs(i, j)
            painting += 1
            if max_area < result:
                max_area = result

print(painting)
print(max_area)