import sys
from collections import deque
input = sys.stdin.readline

# 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지
n = int(input())
place = []
for _ in range(n):
    place.append(list(map(int, input().split())))

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

count = 0
x, y, size = 0, 0, 2

# 아기 상어 시작 위치
for i in range(n):
    for j in range(n):
        if place[i][j] == 9:
            x = i
            y = j

def biteFish(x, y, shark_size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야 하는 칸의 개수의 최솟값 (BFS)
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    temp = []
    while queue:
        q_x, q_y = queue.popleft()
        for i in range(4):
            nx = q_x+dx[i]
            ny = q_y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if place[nx][ny] <= shark_size:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[q_x][q_y] + 1
                    if place[nx][ny] < shark_size and place[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    return sorted(temp, key=lambda x : (-x[2], -x[0], -x[1])) 

count = 0
result = 0
while 1:
    shark = biteFish(x, y, size)
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    if len(shark) == 0:
        break
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    # 정렬한 결과를 반영해준다.
    nx, ny, dist = shark.pop()

    # 움직이는 칸수는 곧 시간이 된다.
    result += dist
    place[x][y], place[nx][ny] = 0, 0
    # 상어좌표를 먹은 물고기 좌표로 옮겨준다.
    x, y = nx, ny
    count+=1 
    if count == size:
        size += 1
        count = 0
print(result)
