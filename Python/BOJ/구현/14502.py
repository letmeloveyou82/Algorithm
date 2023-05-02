import sys
import copy
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
answer = 0 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    tmp_map = copy.deepcopy(map) # 깊은 복사
    for i in range(n):
        for j in range(m):
            if tmp_map[i][j] == 2: # 바이러스 위치 queue 에 저장
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_map[nx][ny] == 0: # 빈칸이라면 전염되었음
                tmp_map[nx][ny] = 2
                queue.append((nx, ny)) # queue에 바이러스 위치 추가
    global answer
    count = 0
    for i in range(n):
        count += tmp_map[i].count(0)
    answer = max(answer, count)

def makeWall(possible_wall):
    if possible_wall == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0: # 빈 칸이라면 벽 세우기
                map[i][j] = 1
                makeWall(possible_wall+1) # 두번째 벽 세우러 가기
                map[i][j] = 0 # 다시 벽을 허문다
makeWall(0)
print(answer)