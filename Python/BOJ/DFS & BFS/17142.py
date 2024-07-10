import sys
from collections import deque
from itertools import combinations

def bfs(active_virus):
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    for x, y in active_virus:
        q.append([x, y])
        visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == -1 and board[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and visited[i][j] == -1:
                return int(1e9)

    max_time = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and max_time < visited[i][j]:
                max_time = visited[i][j]
    return max_time

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus = []
result = int(1e9)

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 위치 저장
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i, j])

for case in combinations(virus, M):
    time = bfs(case)
    if time < result:
        result = time

if result == int(1e9):
    print(-1)
else:
    print(result)
