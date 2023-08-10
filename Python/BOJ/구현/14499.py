# 세로 크기, 가로 크기, 주사위 놓을 곳의 좌표(x, y), 명령 개수
n, m, x, y, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))
# top, 북, 동, 서, 남, bottom
dice = [0, 0, 0, 0, 0, 0]

# 동쪽 1 서쪽 2 북쪽 3 남쪽 4
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: # 동쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2: # 서쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3: # 북쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else: # 남쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

nx, ny = x, y
for i in move:
    nx += dx[i-1]
    ny += dy[i-1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m: # 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    turn(i)
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[-1]
    else:
        dice[-1] = graph[nx][ny]
        graph[nx][ny] = 0
    print(dice[0])
