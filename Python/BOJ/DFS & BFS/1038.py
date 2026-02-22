import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

if N > 1022 :
    print(-1)
    sys.exit(0)

q = deque(range(10))
arr = []

while q:
    x = q.popleft()
    arr.append(x)

    last = x % 10
    for next in range(last):
        q.append(x*10+next)

print(arr[N])
