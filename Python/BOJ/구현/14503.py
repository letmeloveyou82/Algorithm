import sys

input = sys.stdin.readline

N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

direction = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}

# 북(0) -> 서(3)-> 남(2) -> 동(1) -> 북(0)
# 반시계 방향으로 90도 회전
def rotate_dir(d):
    if d == 0:
        d = 3
    else:
        d -= 1
    return d

# 로봇 청소기 작동
def robot_move(x, y, d):
    while True:
        # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
        if board[x][y] == 0:
            board[x][y] = 2 # 청소

        moved = False # 어떤 턴에 전진했는지

        # 4방향 탐색
        for _ in range(4):
            d = rotate_dir(d) # 방향부터 돌림
            nx, ny = x+direction[d][0], y+direction[d][1]

            if board[nx][ny] == 0: # 청소되지 않은 빈 칸이 있는 경우 전진
                x, y = nx, ny
                moved = True
                break

        if moved :
            continue

        # 4방향 모두 못 갔으면 후진
        nx, ny = x-direction[d][0], y-direction[d][1]
        if board[nx][ny] == 1:
            return # 벽이면 작동 멈춤
        x, y = nx, ny

robot_move(x, y, d)

cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            cnt += 1
print(cnt)