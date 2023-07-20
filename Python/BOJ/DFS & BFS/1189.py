import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 목표 : (R-1, 0)에서 시작해서 (0, C-1)까지 갈 수 있는 경우의 수 중 거리가 K인 것의 개수

def dfs(x, y, count):
    global answer
    if (x, y) == (0, c-1) and count == k:
        answer += 1
        return
    for i in range(4): # 갈 수 있는 위치 확인
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c: # 범위 벗어난다면 무시
            continue
        if visited[nx][ny] == 0 and graph[nx][ny] == '.':
            visited[nx][ny] = 1
            dfs(nx, ny, count+1)
            visited[nx][ny] = 0 # 다시 탐색할 때 방문처리 안 되어있어야 하니까 0으로 다시 바꿈

answer = 0
visited[r-1][0] = 1
dfs(r-1, 0, 1)
print(answer)