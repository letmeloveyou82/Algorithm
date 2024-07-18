import sys
from itertools import permutations

def rotate(r, c, s):
    A_copy = [i[:] for i in A]
    x, y = r-s, c-s
    for i in range(2 * s, 0, -2):
        idx = 0
        while idx < 4:
            for j in range(i):
                nx, ny = x + dx[idx], y + dy[idx]
                A_copy[nx][ny] = A[x][y]
                x, y = nx, ny
            idx += 1
        x, y = x+1, y+1

    return A_copy

def calculate_A(arr):
    global result

    for i in arr:
        if sum(i) < result:
            result = sum(i)
            
input = sys.stdin.readline
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
original_A = [i[:] for i in A]
rotate_info = []
for _ in range(K):
    r, c, s = map(int, input().split())
    rotate_info.append([r-1, c-1, s])

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = int(1e9)
for case in list(permutations(rotate_info)):
    for r, c, s in case:
        A = rotate(r, c, s)
    calculate_A(A)
    A = original_A
print(result)