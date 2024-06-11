import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int, input().split())
robots = dict() # 로봇 번호를 key로, 로봇 위치 y, x와 방향 d를 values로 하는 dict
board = [[0] * (A+1) for _ in range(B+1)] # 칸에 존재하는 로봇 번호를 저장
# N, W, S, E (왼쪽 방향으로 회전)
dir = {0:[1, 0], 1:[0, -1], 2:[-1, 0], 3:[0, 1]}

for i in range(1, N+1):
    x, y, d = input().split()
    x, y = int(x), int(y)
    board[y][x] = i

    if d == 'N':
        d = 0
    elif d == 'W':
        d = 1
    elif d == 'S':
        d = 2
    else:
        d = 3

    robots[i] = [y, x, d]

for _ in range(M):
    num, command_type, repeat_cnt = input().split()
    num = int(num)
    repeat_cnt = int(repeat_cnt)
    ny, nx, d = robots[num]
    if command_type == 'L':
        repeat_cnt %= 4
        robots[num][2] = (d+repeat_cnt)%4
    elif command_type == 'R':
        repeat_cnt %= 4
        robots[num][2] = (d-repeat_cnt)%4
    else:
        for _ in range(repeat_cnt):
            nx, ny = nx+dir[d][1], ny+dir[d][0]
            if nx < 1 or ny < 1 or nx > A or ny > B:
                print(f"Robot {num} crashes into the wall")
                exit(0)
            if board[ny][nx] != 0:
                print(f"Robot {num} crashes into robot {board[ny][nx]}")
                exit(0)
            board[ny][nx] = num
            board[robots[num][0]][robots[num][1]] = 0
            robots[num][0], robots[num][1] = ny, nx
print("OK")