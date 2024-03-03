import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
lecture = list(map(int, input().split()))

left = max(lecture)
right = sum(lecture)
result = 0

while left <= right:
    mid = (left+right)//2
    total = 0
    cnt = 1
    for i in range(N):
        if total + lecture[i] > mid:
            cnt += 1
            total = 0
        total += lecture[i]

    if cnt <= M:
        right = mid - 1
        result = mid
    else:
        left = mid + 1

print(result)