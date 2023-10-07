from collections import deque
import sys

input = sys.stdin.readline
m, n, h = map(int, input().split())
graph = []
q = deque([])

for i in range(h):
  temp = []
  for j in range(n):
    temp.append(list(map(int, input().split())))
    for k in range(m):
      if temp[j][k] == 1:
        q.append((i, j, k))
  graph.append(temp)

dz = (1, -1, 0, 0, 0, 0)
dx = (0, 0, 0, 0, 1, -1)
dy = (0, 0, -1, 1, 0, 0)

while q:
  z, x, y = q.popleft()
  for i in range(6):
    nz = z+dz[i]
    nx = x+dx[i]
    ny = y+dy[i]
    if 0<=nz<h and 0<=nx<n and 0<=ny<m and graph[nz][nx][ny] == 0:
      q.append((nz, nx, ny))
      graph[nz][nx][ny] = graph[z][x][y] + 1
      
day = 0
for i in graph:
  for j in i:
    for k in j:
      if k == 0:
        print(-1)
        exit(0)
    day = max(day, max(j))
print(day-1)