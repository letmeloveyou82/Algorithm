import sys
from collections import deque
from itertools import combinations

def bfs(pick_virus):
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    for x, y in pick_virus:
        q.append([x, y])
        visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and board[nx][ny] != 1 and visited[nx][ny] == -1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    for i in range(N):
        for j in range(N):
            if board[i][j] != 1 and visited[i][j] == -1:
                return -1

    return max(map(max, visited))

input = sys.stdin.readline
N, M = map(int, input().split())
virus = []
board = [list(map(int, input().split())) for _ in range(N)]

# 바이러스 위치 저장
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i, j])

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = int(1e9)
for i in combinations(virus, M):
    time = bfs(list(i))
    if time != -1:
        answer = min(answer, time)

if answer == int(1e9):
    print(-1)
else:
    print(answer)