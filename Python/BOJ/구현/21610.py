from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 8방향 정의
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

cloud_q = deque()  # 비구름 위치

# 초기 비구름 위치 저장
for a, b in [(N, 1), (N, 2), (N - 1, 1), (N - 1, 2)]:
    cloud_q.append((a - 1, b - 1))

# 대각선 방향 중 물 있는 칸의 개수 세기
def water_exist(x, y):
    cnt = 0
    for i in range(2, 9, 2):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[x + dx[i]][y + dy[i]] > 0:
            cnt += 1
    return cnt

def move(d, s):
    cloud_visited = [[0] * N for _ in range(N)] # 사라진 구름 위치인지 체크하는 용도
    more_water_q = deque() # 대각선 방향에서 물을 더 받아올 수 있는지 확인해야 하는 위치
    while cloud_q:
        x, y = cloud_q.popleft()
        nx, ny = x + (dx[d] * s), y + (dy[d] * s)

        # 범위 넘어갈 경우 계산
        if nx < 0:
            while True:
                nx += N
                if nx >= 0:
                    break
        elif nx >= N:
            nx = nx % N
        if ny < 0:
            while True:
                ny += N
                if ny >= 0:
                    break
        elif ny >= N:
            ny = ny % N

        graph[nx][ny] += 1
        more_water_q.append((nx, ny))

    while more_water_q:
        x, y = more_water_q.popleft()
        graph[x][y] += water_exist(x, y)
        cloud_visited[x][y] = 1

    for i in range(N):
        for j in range(N):
            if cloud_visited[i][j] == 0 and graph[i][j] >= 2:
                cloud_q.append((i, j))
                graph[i][j] -= 2

for _ in range(M):
    d, s = map(int, input().split())
    move(d, s)

result = 0
for i in range(N):
    for j in range(N):
        result += graph[i][j]
print(result)