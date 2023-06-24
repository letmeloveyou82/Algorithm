import copy

space = [[] for _ in range(4)]

# 8방향 정의 (1~8)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    temp_list = list(map(int, input().split()))
    fish = []
    for j in range(4):
        fish.append([temp_list[2*j], temp_list[2*j+1]-1]) # 물고기 번호, 방향
    space[i] = fish

max_score = 0

def dfs(sx, sy, score, space):
    global max_score
    score += space[sx][sy][0] # 물고기 번호 더해줌
    max_score = max(max_score, score)
    space[sx][sy][0] = 0 # 상어 시작위치 번호는 0으로

    # 물고기 이동
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if space[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = space[f_x][f_y][1]

        for i in range(8):
            nd = (f_d+i) % 8 # 다음 방향 번호
            nx, ny = f_x + dx[nd], f_y + dy[nd]
            if not(0<=nx<4 and 0<=ny<4) or (nx == sx and ny == sy): # 상어 아니면 swap 이동 후 멈춤
                continue
            space[f_x][f_y][1] = nd
            space[f_x][f_y], space[nx][ny] = space[nx][ny], space[f_x][f_y]
            break
    # 상어 이동
    s_d = space[sx][sy][1]
    for i in range(1, 5):
        nx = sx+dx[s_d]*i
        ny = sy+dy[s_d]*i
        if (0<=nx<4 and 0<=ny<4) and space[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(space))
dfs(0, 0, 0, space)
print(max_score)
