def solution(n):
    answer = 0
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    dir = [(-1, 0), (-1, -1), (-1, 1)] # 윗칸 3개 확인

    def check(x, y):
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            
            while 0<=nx<n and 0<=ny<n:
                if board[nx][ny] == 1:
                    return False
                nx += dx
                ny += dy
                
        return True
    
    def dfs(r):
        nonlocal answer
        
        if r == n:
            answer += 1
            return
        
        for c in range(n):
            if check(r, c):
                board[r][c] = 1
                dfs(r+1)
                board[r][c] = 0
            
    dfs(0)
    
    return answer