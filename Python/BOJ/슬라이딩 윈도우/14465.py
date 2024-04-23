import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
traffic_light = [-1] + [0] * N
for _ in range(B):
    broken = int(input())
    traffic_light[broken] = 1

left, right = 1, K
fix = traffic_light[left:right+1].count(1)
result = fix

while right < N+1:
    if fix < result:
        result = fix
    fix -= traffic_light[left]
    left += 1
    right += 1
    if right == N+1:
        break
    fix += traffic_light[right]

print(result)