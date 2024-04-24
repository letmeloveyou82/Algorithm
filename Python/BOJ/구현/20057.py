import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
now = [N//2, N//2] # 현재 x, y 좌표

# 왼쪽 방향으로 퍼질 때
left = [(-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01),
        (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left] # 오른쪽 방향으로 퍼질 때
down = [(-y, x, z) for x, y, z in left] # 아래쪽 방향으로 퍼질 때
up = [(-x, y, z) for x, y, z in down] # 위쪽 방향으로 퍼질 때
rate = {'left': left, 'right': right, 'down': down, 'up': up}

# 모래를 흩날리는 함수
def move(cnt, dx, dy, direction):
    global answer
    for _ in range(cnt+1):
        # 현재 좌표 업데이트
        now[0], now[1] = now[0]+dx, now[1]+dy
        # 회오리를 돌다가 끝나버린 경우
        if now[0] < 0 or now[1] < 0:
            break
        spreads = 0 # 모래가 퍼진 값을 누적한 양
        for dx, dy, r in rate[direction]:
            nx, ny = now[0]+dx, now[1]+dy
            if r == 0: # 퍼지지 않는 모래들은 현재 자리에 누적해주기
                sand = board[now[0]][now[1]] - spreads
            else: # 퍼지는 모래들 계산
                sand = int(board[now[0]][now[1]] * r)
            # 모래양 업데이트
            if 0<=nx<N and 0<=ny<N:
                board[nx][ny] += sand
            else:
                answer += sand
            spreads += sand # 현재 자리 계산을 위한 퍼지는 모래의 누적값

for i in range(N):
    if i % 2 == 0:
        move(i, 0, -1, 'left')
        move(i, 1, 0, 'down')
    else:
        move(i, 0, 1, 'right')
        move(i, -1, 0, 'up')
print(answer)

