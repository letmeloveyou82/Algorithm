import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

virus = []
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            virus.append([board[i][j], i, j])
virus = deque(sorted(virus))

for _ in range(S):
    tmp = []
    while virus:
        virus_num, x, y = virus.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and board[nx][ny] == 0:
                tmp.append((virus_num, nx, ny))
                board[nx][ny] = virus_num
    for t in tmp:
        virus.append(t)

print(board[X-1][Y-1])