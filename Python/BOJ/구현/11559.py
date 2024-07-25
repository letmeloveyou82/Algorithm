import sys
from collections import deque

# BFS 사용해서 없어지는 뿌요 있는지 체크
def check_pop(x, y, color):
    q = deque()
    visited = [[False] * 6 for _ in range(12)]
    q.append([x, y])
    visited[x][y] = True

    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny] and board[nx][ny] == color:
                cnt += 1
                q.append([nx, ny])
                visited[nx][ny] = True

    if cnt >= 4:
        for i in range(12):
            for j in range(6):
                if visited[i][j]:
                    board[i][j] = "."
        return 1

    return 0

# 중력 영향 받아 내리기
def down_puyo():
    next_board = []
    for i in range(6):
        column_list = []
        for j in range(12):
            if board[j][i] != ".":
                column_list.append(board[j][i])
        next_board.append(["."] * (12 - len(column_list)) + column_list)

    for i in range(12):
        for j in range(6):
            board[i][j] = next_board[j][i]

input = sys.stdin.readline
board = [list(input().rstrip()) for _ in range(12)]
answer = 0

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

disappear = 0 # 사라지는 뿌요 그룹 개수 카운트
while True:
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                disappear += check_pop(i, j, board[i][j])
    if disappear > 0:
        down_puyo()
        answer += 1
        disappear = 0
    else:
        break

print(answer)