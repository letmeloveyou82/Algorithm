import sys

input = sys.stdin.readline
N = int(input())
building = list(map(int, input().split()))
answer = [0] * N

for i in range(N-1):
    max_slope = -float('inf')
    for j in range(i+1, N):
        slope = (building[j] - building[i]) / (j - i)
        if slope <= max_slope:
            continue
        max_slope = max(max_slope, slope)
        answer[i] += 1
        answer[j] += 1

print(max(answer))