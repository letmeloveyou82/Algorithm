import sys

input = sys.stdin.readline
N, M = map(int, input().split())
power = []
for i in range(N):
    p_name, p_number = input().split()
    power.append([i, p_name, int(p_number)])
power.sort(key=lambda x : (x[2], x[0]))

for _ in range(M):
    x = int(input())
    # 이분 탐색
    left, right = 0, N-1
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if x <= power[mid][2]:
            right = mid-1
            answer = mid
        else:
            left = mid+1
    print(power[answer][1])