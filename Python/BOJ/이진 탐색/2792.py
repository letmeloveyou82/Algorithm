import sys

input = sys.stdin.readline
N, M = map(int, input().split()) # 아이들의 수, 색상 수
colors = [int(input()) for _ in range(M)]
ans = float("inf")
left, right = 1, max(colors)

# 이분 탐색
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for jew in colors:
        cnt += (jew // mid) + (1 if jew % mid != 0 else 0)

    if cnt <= N:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)