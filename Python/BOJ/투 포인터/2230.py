import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort()

left = 0
right = 0
result = max(A) - min(A)
while left < N-1:
    gap = A[right]-A[left]
    if gap >= M:
        if gap < result:
            result = gap
        left += 1
    else:
        if right < N-1:
            right += 1
        else:
            left += 1
print(result)