import sys
from collections import defaultdict

input = sys.stdin.readline
M, N = map(int, input().split())
universe = defaultdict(int)

for _ in range(M):
    planets = list(map(int, input().split()))
    sorted_planets = sorted(list(set(planets))) # 구성 같은 행성 한 개만 세기 위해 중복 제거하고, 오름차순으로 정렬
    rank = {sorted_planets[i] : i for i in range(len(sorted_planets))} # 행성 순위 지정
    vector = tuple([rank[i] for i in planets]) # 입력 받은 행성에 맞게 순위 저장
    universe[vector] += 1 

answer = 0
for i in universe.values():
    answer += (i * (i-1)) // 2 # nC2
print(answer)