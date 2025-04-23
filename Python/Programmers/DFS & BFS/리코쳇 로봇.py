from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    
    def bfs(i, j):
        q = deque([])
        q.append([0, i, j])
        visited = [[False] * m for _ in range(n)]
        visited[i][j] = True
        
        while q:
            cnt, x, y = q.popleft()
            
            if board[x][y] == 'G':
                return cnt
            
            for d in range(4):
                nx, ny = x, y
                while True:
                    tx, ty = nx+dx[d], ny+dy[d]
                    if not (0<=tx<n and 0<=ty<m) or board[tx][ty] == 'D':
                        break
                    nx, ny = tx, ty
                    
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([cnt+1, nx, ny])
        return -1
        
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                answer = bfs(i, j)
    return answer