import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * (C) for _ in range(R)]

def dfs(x, y):
    if y == C-1:
        return True
    for dx in [-1, 0, 1]:
        nx = x+dx
        ny = y+1
        if 0<=nx<R and 0<=ny<C:
            if graph[nx][ny] != 'x' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if dfs(nx, ny):
                    return True
    return False

answer = 0
for i in range(R):
    if dfs(i, 0):
        answer += 1

print(answer)