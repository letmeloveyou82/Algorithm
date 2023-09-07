import sys
input = sys.stdin.readline
r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
ans = 0

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# set 사용
q = {(0, 0, graph[0][0])}

while q:
    x, y, temp = q.pop()
    ans = max(ans, len(temp))

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in temp:
            q.add((nx, ny, temp+graph[nx][ny]))

print(ans)