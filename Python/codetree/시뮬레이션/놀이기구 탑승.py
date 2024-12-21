import sys
input = sys.stdin.readline 

def find_best_seat(num):
    bf, be, br, bc = 5, 5, n, n
    for i in range(n):
        for j in range(n):
            if board[i][j] == -1:
                f, e = 4, 4
                for k in range(4):
                    nr, nc = i+dx[k], j+dy[k]
                    if 0<=nr<n and 0<=nc<n:
                        if board[nr][nc] in like_info[num]:
                            f -= 1
                        elif board[nr][nc] == -1:
                            e -= 1
                if (bf, be, br, bc) > (f, e, i, j):
                    bf, be, br, bc = f, e, i, j
    board[br][bc] = num

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
board = [[-1] * n for _ in range(n)]
like_info = dict()

for i in range(n*n):
    n0, n1, n2, n3, n4 = map(int, input().split())
    like_info[n0-1] = [n1-1, n2-1, n3-1, n4-1]
    find_best_seat(n0-1)

score = {0:0, 1:1, 2:10, 3:100, 4:1000}
result = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] in like_info[board[i][j]]:
                cnt += 1
        result += score[cnt]
print(result)