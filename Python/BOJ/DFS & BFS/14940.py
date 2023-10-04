import sys
from collections import deque

# 입력
input = sys.stdin.readline
n, m = map(int, input().split()) # 세로 크기, 가로 크기
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, end):
  q = deque()
  q.append((start, end))
  visited[start][end] = 0
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1:
        if board[nx][ny] == 0:
          visited[nx][ny] = 0
        elif board[nx][ny] == 1:
          visited[nx][ny] = visited[x][y] + 1
          q.append((nx, ny))

for i in range(n):
  for j in range(m):
    if board[i][j] == 2 and visited[i][j] == -1:
      bfs(i, j)

# 출력
for i in range(n):
  for j in range(m):
    if board[i][j] == 0:
      print(0, end=' ')
    else:
      print(visited[i][j], end=' ')
  print()