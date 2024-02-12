import sys
input = sys.stdin.readline

# M개 이상의 구간으로 나눌 수 있는지 체크
def is_valid(mid):
    global answer
    low, high = num[0], num[0] # 구간의 최솟값, 최댓값
    d = 1 # 나눈 구간의 개수

    for i in num:
        if high < i:
            high = i

        if low > i:
            low = i

        if high-low > mid:
            d += 1
            low = i
            high = i

    return M >= d

N, M = map(int, input().split())
num = list(map(int, input().split()))
answer = 10000
left, right = 0, max(num)

# 이분 탐색
while left <= right:
    mid = (left+right)//2
    if is_valid(mid):
        right = mid-1
        answer = min(mid, answer)
    else:
        left = mid+1

print(answer)