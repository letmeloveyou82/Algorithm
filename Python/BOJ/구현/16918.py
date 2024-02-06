import sys
from collections import deque
input = sys.stdin.readline

R, C, N = map(int, input().split())
board = [list(input()) for _ in range(R)]
bomb = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 폭탄 위치 저장
def save_bomb(b):
    for i in range(R):
        for j in range(C):
            if b[i][j] == 'O':
                bomb.append((i, j))

# 격자판 상태 출력
def print_board(b):
    for i in range(R):
        for j in range(C):
            print(b[i][j], end="")
        print()

def bfs():
    time = 0
    save_bomb(board)

    while True:
        if time == N:
            break

        time += 1
        if time % 2 == 0:
            save_bomb(board)
            # 모든 칸 폭탄으로 만듦
            for i in range(R):
                for j in range(C):
                    board[i][j] = 'O'
        elif time >= 3 and time % 2 == 1:
            # 폭탄 터짐
            while bomb:
                x, y = bomb.popleft()
                board[x][y] = '.'
                for i in range(4):
                    if 0 <= x + dx[i] < R and 0 <= y + dy[i] < C:
                        board[x + dx[i]][y + dy[i]] = '.'

bfs()
print_board(board)
