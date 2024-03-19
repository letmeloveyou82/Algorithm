from collections import deque
import sys

input = sys.stdin.readline
test_case = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(r, c, depth):
    q = deque()
    q.append((r, c, depth))
    while q:
        x, y, cnt = q.popleft()
        if x == target_x and y == target_y:
            return cnt
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<l and 0<=ny<l and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx, ny, cnt+1))
    return

for _ in range(test_case):
    l = int(input())
    graph = [[0]*l for _ in range(l)]
    knight_x, knight_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    print(bfs(knight_x, knight_y, 0))