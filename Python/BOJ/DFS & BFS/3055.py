from collections import deque
import sys

input = sys.stdin.readline
R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
distance = [[0] * C for _ in range(R)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
house_x, house_y = 0, 0 # 비버의 집 위치
q = deque()

def bfs(Dx, Dy):
    while q:
        x, y = q.popleft()
        if board[Dx][Dy] == 'S':
            return distance[Dx][Dy]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if (board[nx][ny] == '.' or board[nx][ny] == 'D') and board[x][y] == 'S':
                    board[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
                elif (board[nx][ny] == '.' or board[nx][ny] == 'S') and board[x][y] == '*':
                    board[nx][ny] = '*'
                    q.append((nx, ny))
    return "KAKTUS"

for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            q.appendleft((i, j))
        elif board[i][j] == 'D':
            house_x, house_y = i, j
        elif board[i][j] == '*':
            q.append((i, j))

print(bfs(house_x, house_y))