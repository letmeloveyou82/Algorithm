import sys

input = sys.stdin.readline
N = int(input())
liquid = sorted(list(map(int, input().split())))

result = [float('inf'), []]

for i in range(N-2):
    first = liquid[i]
    left, right = i+1, N-1
    while left < right:
        now = first + liquid[left] + liquid[right]
        if abs(now) < result[0]:
            result[0] = abs(now)
            result[1] = [first, liquid[left], liquid[right]]
        if now < 0:
            left += 1
        elif now > 0:
            right -= 1
        else:
            print(*result[1])
            exit(0)
            
print(*result[1])