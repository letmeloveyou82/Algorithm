import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H+X)]
A = [[0] * W for _ in range(H)]

for i in range(H+X):
    for j in range(W+Y):
        if X <= i < H and Y <= j < W:
            A[i][j] = B[i][j] - A[i-X][j-Y]
        elif 0 <= i < H and 0 <= j < W:
            A[i][j] = B[i][j]
        elif X <= i < H+X and Y <= j < W+Y:
            A[i-X][j-Y] = B[i][j]

for i in range(H):
    for j in range(W):
        print(A[i][j], end=" ")
    print()