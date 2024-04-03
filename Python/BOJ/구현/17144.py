import sys, math
from collections import deque

# 1. 미세먼지 위치 저장
def find_dust():
    for i in range(R):
        for j in range(C):
            if A[i][j] > 0:
                dust.append((i, j))

# 2. 미세먼지 확산
def spread_of_find_dust(q):
    add_find_dust = deque()
    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and A[nx][ny] != -1:
                cnt += 1
                add_find_dust.append((nx, ny, math.floor(A[x][y] / 5)))
        A[x][y] -= math.floor(A[x][y] / 5) * cnt
    while add_find_dust:
        x, y, val = add_find_dust.popleft()
        A[x][y] += val

# 3. 공기청정기 작동
def air_clean():
    move_q = deque()
    
    # 반시계방향으로 회전
    x, y = air_cleaner[0]
    anti_clockwise_x = [0, -1, 0, 1]
    anti_clockwise_y = [1, 0, -1, 0]
    d = 0
    while d < 4:
        nx = x + anti_clockwise_x[d]
        ny = y + anti_clockwise_y[d]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            d += 1
            continue
        if nx == air_cleaner[0][0] and ny == air_cleaner[0][1]:
            break
        move_q.append((nx, ny, A[x][y]))
        x, y = nx, ny

    # 시계방향으로 회전
    x, y = air_cleaner[1]
    d = 0
    while d < 4:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            d += 1
            continue
        if nx == air_cleaner[1][0] and ny == air_cleaner[1][1]:
            break
        move_q.append((nx, ny, A[x][y]))
        x, y = nx, ny

    while move_q:
        x, y, val = move_q.popleft()
        if val == -1:
            val = 0
        A[x][y] = val

input = sys.stdin.readline
R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
air_cleaner = []
dust = deque()

# 시계 방향 순서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 공기청정기 위치 저장
for i in range(R):
    for j in range(C):
        if A[i][j] == -1:
            air_cleaner.append((i, j))

for _ in range(T):
    find_dust()
    spread_of_find_dust(dust)
    air_clean()

# 남아있는 미세먼지 양 계산
result = 0
for i in range(R):
    for j in range(C):
        if A[i][j] > 0:
            result += A[i][j]
print(result)