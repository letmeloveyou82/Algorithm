import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
house, chicken = [], [] # 집 좌표, 치킨집 좌표
result = int(1e9)

for i in range(n):
    city = list(map(int, input().split()))
    for j in range(n):
        if city[j] == 1:
            house.append((i, j))
        elif city[j] == 2:
            chicken.append((i, j))

for combi in combinations(chicken, m): # m개의 치킨집 선택
    total_distance = 0 # 도시의 치킨 거리
    for r1, c1 in house:
        distance = int(1e9) # 각 집마다 치킨 거리
        for r2, c2 in combi:
            distance = min(distance, abs(r1-r2) + abs(c1-c2))
        total_distance += distance
    result = min(result, total_distance)
print(result)
