from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    answer = 0
    q = deque()
    q.append((0, 0))

    # 동서남북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y]+1
                q.append((nx, ny))
                
    destination = maps[n-1][m-1]
    if destination == 1:
        answer = -1
    else:
        answer = destination
    return answer