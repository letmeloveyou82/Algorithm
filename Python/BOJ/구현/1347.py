import sys

input = sys.stdin.readline
n = int(input())
note = input().rstrip()

# 남, 서, 북, 동(오른쪽으로 90도 회전)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0
d = 0
board = [[0, 0]]
min_x, min_y = 0, 0
max_x, max_y = 0, 0

for move in note:
    if move == 'L':
        d = (d-1)%4
    elif move == 'R':
        d = (d+1)%4
    else:
        nx, ny = x+dx[d], y+dy[d]
        board.append([nx, ny])
        if nx < min_x:
            min_x = nx
        if ny < min_y:
            min_y = ny
        if nx > max_x:
            max_x = nx
        if ny > max_y:
            max_y = ny
        x, y = nx, ny

for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
        if [i, j] in board:
            print(".", end='')
        else:
            print("#", end='')
    print()
