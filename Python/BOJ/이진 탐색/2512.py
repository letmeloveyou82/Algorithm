n = int(input())
region = list(map(int, input().split()))
m = int(input()) # 예산

start, end = 0, max(region)

# 이분 탐색(Binary Search)
while start <= end:
    mid = (start+end)//2
    total = 0 # 총 지출 양
    for i in region:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)