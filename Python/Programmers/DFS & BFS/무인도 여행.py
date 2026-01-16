from collections import deque

def solution(maps):
    answer = []
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    def bfs(start_x, start_y):
        nonlocal visited, n, m
        
        q = deque([])
        q.append((start_x, start_y))
        visited[start_x][start_y] = True
        cnt = int(maps[start_x][start_y])
        
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    cnt += int(maps[nx][ny])
                    q.append((nx, ny))
                    visited[nx][ny] = True
        
        return cnt
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(bfs(i, j))
    
    if len(answer) == 0:
        return [-1]
           
    return sorted(answer)