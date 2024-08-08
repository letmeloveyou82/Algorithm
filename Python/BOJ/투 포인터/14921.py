import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))

left = 0
right = N-1
result = liquid[left] + liquid[right]

while left < right:
    tmp = liquid[left] + liquid[right]
    if abs(result) > abs(tmp):
        result = tmp
    if tmp < 0:
        left += 1
    else:
        right -= 1

print(result)


