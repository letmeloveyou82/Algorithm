from collections import deque

def solution(maps):
    def bfs(sx, sy, target):
        q = deque([])
        q.append((sx, sy, 0)) # x위치, y위치, 거리
        visited = [[False] * m for _ in range(n)]
        visited[sx][sy] = True
        
        while q:
            x, y, cnt = q.popleft()
            if maps[x][y] == target:
                return cnt
            
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    q.append([nx, ny, cnt+1])
        return -1
    
    n, m = len(maps), len(maps[0])
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    
    sx = sy = lx = ly = 0
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx, sy = i, j
            elif maps[i][j] == 'L':
                lx, ly = i, j
    
    d1 = bfs(sx, sy, 'L') # S -> L
    if d1 == -1:
        return -1

    d2 = bfs(lx, ly, 'E') # L -> E
    if d2 == -1:
        return -1 
    
    return d1 + d2