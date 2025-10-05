import sys
input = sys.stdin.readline

# 8방향 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 초기 구름
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

def move_and_rain(d, s):
    new_clouds = []
    for x, y in clouds:
        nx = (x+dx[d]*s) % N
        ny = (y+dy[d]*s) % N
        new_clouds.append((nx, ny))
    # 비 내리기
    for x, y in new_clouds:
        board[x][y] += 1
    return new_clouds

def water_copy_bug(current_clouds):
    # 대각선만 체크
    for x, y in current_clouds:
        cnt = 0
        for i in range(1, 8, 2):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and board[nx][ny] >= 1:
                cnt += 1
        board[x][y] += cnt

def make_new_clouds(current_clouds):
    # 이번 턴에 구름이 있던 칸을 표시
    was_cloud = [[False] * N for _ in range(N)]
    for x, y in current_clouds:
        was_cloud[x][y] = True

    new_clouds = []
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and not was_cloud[i][j]:
                new_clouds.append((i, j))
                board[i][j] -= 2
    return new_clouds

for _ in range(M):
    d, s = map(int, input().split())
    d -= 1
    # 1 ~ 2단계 : 이동 + 비
    clouds = move_and_rain(d, s%N)
    # 3단계 : 물복사버그
    water_copy_bug(clouds)
    # 4단계 : 새 구름 생성
    clouds = make_new_clouds(clouds)

print(sum(map(sum, board)))