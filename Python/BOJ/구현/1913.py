n = int(input())
target = int(input())

board = [[0] * n for _ in range(n)]
target_x, target_y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

r, c = 0, 0
num = n*n
for k in range(n-1, 0, -2): # 테두리 한 겹
    # 방향(아래, 오른쪽, 위, 왼쪽)
    for i, j in zip(dx, dy):
        for _ in range(k):
            board[r][c] = num
            r += i
            c += j
            num -= 1
    r+=1
    c+=1
board[r][c] = 1

for i in range(n):
    for j in range(n):
        if board[i][j] == target:
            target_x, target_y = i, j
        print(board[i][j], end =' ')
    print()
print(target_x+1, target_y+1)