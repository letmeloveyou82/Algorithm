import sys

def rotate(A):
    x, y = i, i
    value = A[x][y] # 맨 처음 값 저장

    # 왼쪽
    for j in range(i+1, N-i):
        x = j
        tmp = A[x][y]
        A[x][y] = value
        value = tmp

    # 아래쪽
    for j in range(i+1, M-i):
        y = j
        tmp = A[x][y]
        A[x][y] = value
        value = tmp


    # 오른쪽
    for j in range(i+1, N-i):
        x = N-j-1
        tmp = A[x][y]
        A[x][y] = value
        value = tmp

    # 위쪽
    for j in range(i+1, M-i):
        y = M-j-1
        tmp = A[x][y]
        A[x][y] = value
        value = tmp

    return A

input = sys.stdin.readline
N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

cycle = 2*(N-1) + 2*(M-1)
for i in range(min(N, M)//2):
    for _ in range(R%cycle):
        rotate(A)
    cycle -= 8

for i in A:
    print(*i)