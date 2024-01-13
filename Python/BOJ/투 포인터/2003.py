import sys

input = sys.stdin.readline
N, M = map(int, input().split())
num = list(map(int, input().split()))
left, right = 0, 0
case = 0
now = 0

while left < N:
    while now < M and right < N:
        now += num[right]
        right += 1
    if now == M:
        case += 1
    now -= num[left]
    left += 1
    
print(case)