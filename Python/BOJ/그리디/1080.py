import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().rstrip())) for _ in range(N)]
B = [list(map(int, input().rstrip())) for _ in range(N)]
cnt = 0

# 3x3 부분 행렬에 있는 모든 원소 뒤집기 (0 -> 1, 1 -> 0)
def change(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if A[i][j] == 0:
                A[i][j] = 1
            else:
                A[i][j] = 0

if (N < 3 or M < 3) and A != B:
    cnt = -1
else:
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                cnt += 1
                change(i, j)

if cnt != -1:
    if A != B:
        cnt = -1
print(cnt)