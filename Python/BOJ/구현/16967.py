h, w, x, y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(h+x)]

A = [[0] * w for _ in range(h)]

for i in range(h+x):
    for j in range(w+y):
        if B[i][j] == 0:
            continue
        if x <= i < h and y <= j < w:
            A[i][j] = B[i][j] - A[i-x][j-y]
        elif 0 <= i < h and 0 <= j < w:
            A[i][j] = B[i][j]
        elif x <= i < h+x and y <= j < w+y:
            A[i-x][j-y] = B[i][j]

for i in range(h):
    for j in range(w):
        print(A[i][j], end=' ')
    print("")
