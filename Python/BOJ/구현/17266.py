N = int(input())
M = int(input())
streetlamp = list(map(int, input().split()))
H = streetlamp[0]
for i in range(1, M):
    distance = streetlamp[i] - streetlamp[i-1]
    if distance % 2 == 0: # 짝수이면
        distance = distance // 2
    else: # 홀수이면
        distance = distance // 2 + 1
    H = max(H, distance)
H = max(H, N - streetlamp[-1])
print(H)