n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)] # 칸의 색
chess = [[[] for _ in range(n)] for _ in range(n)] # 해당 체스칸에 있는 말 번호

# 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
horse = [] # 각 말의 위치와 이동 방향
for i in range(k):
    x, y, d = map(int, input().split())
    horse.append([x-1, y-1, d-1])
    chess[x-1][y-1].append(i)
count = 0

# 이동 방향을 반대로 하는 함수
def change_dir(d):
    if d in [0, 2]:
        d += 1
    elif d in [1, 3]:
        d -= 1
    return d

# 0은 흰색, 1은 빨간색, 2는 파란색
def solve(h_num):
    x, y, d = horse[h_num]
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
        d = change_dir(d)
        horse[h_num][2] = d
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
            return True
    
    horse_up = []
    for h_idx, h_n in enumerate(chess[x][y]):
        if h_n == h_num:
            horse_up.extend(chess[x][y][h_idx:]) # 현재 이동하려는 말 ~ 그 위에 쌓아져있는 말에 대한 정보를 저장
            chess[x][y] = chess[x][y][:h_idx] # 말을 이동하기 위해 chess 리스트에서 현재 이동하려는 말 ~ 그 위에 쌓아져있는 말에 대한 번호를 지운다. 
            break

    if board[nx][ny] == 1:
        horse_up = horse_up[-1::-1]
    
    for h in horse_up:
        horse[h][0], horse[h][1] = nx, ny
        chess[nx][ny].append(h)
    
    if len(chess[nx][ny]) >= 4:
        return False
    return True

while True:
    what = False 
    if count > 1000:
        print(-1)
        break
    for i in range(k):
        if solve(i) == False:
            what = True
            break
    count += 1
    if what:
        print(count)
        break