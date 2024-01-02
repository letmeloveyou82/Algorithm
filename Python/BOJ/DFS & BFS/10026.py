from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[r][c] == graph[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

cnt1 = 0
cnt2 = 0

# 적록색약이 아닌 사람이 봤을 때
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt1 += 1

# 적록색약인 사람이 봤을 때
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)