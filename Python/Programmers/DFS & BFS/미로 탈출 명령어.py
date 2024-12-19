import sys
sys.setrecursionlimit(10**6)

answer = "z"
d_char = ["d", "l", "r", "u"]
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]   

def dfs(n, m, x, y, r, c, k, path, cnt):
    global answer
    if k < cnt + abs(x-r) + abs(y-c):
        return
    if x == r and y == c and cnt == k:
        answer = path
        return 
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and path < answer:
            dfs(n, m, nx, ny, r, c, k, path+d_char[i], cnt+1)
    
def solution(n, m, x, y, r, c, k):
    x, y, r, c = x-1, y-1, r-1, c-1
    dist = abs(x-r) + abs(y-c)
    if dist > k or (k-dist) % 2 == 1:
        return "impossible"
    
    dfs(n, m, x, y, r, c, k, "", 0)
    
    return answer