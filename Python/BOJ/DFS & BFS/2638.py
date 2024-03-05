import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

time = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
    visited = [[0] * M for _ in range(N)]

    q = deque()
    q.append([0, 0])
    visited[0][0] = -1  # 방문 처리

    while q:
        x, y = q.popleft()
        if board[x][y] == 1:
            continue  # 이미 치즈인 곳이면 탐색할 필요가 없으므로

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if visited[nx][ny] == -1:
                continue  # 방문 했던 곳이므로

            if board[nx][ny] == 1:  # 치즈이면
                visited[nx][ny] += 1  # 접촉 횟수 추가
            else:
                visited[nx][ny] = -1  # 치즈가 아니면 방문처리
            q.append([nx, ny])  # q에 추가

    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:  # 2번 이상 접촉한 경우라면
                board[i][j] = 0  # 치즈 녹이기


while True:
    find_cheese = False

    # 종료 조건
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                find_cheese = True
    if not find_cheese:
        break

    bfs()
    time += 1

print(time)