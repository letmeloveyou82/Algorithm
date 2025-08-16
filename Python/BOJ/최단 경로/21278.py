import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
INF = float('inf')
graph = [[INF] * N for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A-1][B-1] = 1
    graph[B-1][A-1] = 1

for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0

# 플로이드 워셜
for k in range(N): # 거치는 점
    for i in range(N): # 시작 점
        for j in range(N): # 끝 점
            # k를 거쳤을 때 경로가 더 적은 경로
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

chicken_place = []
min_dist = INF

for case in combinations([i for i in range(N)], 2):
    a, b = case
    lst = []
    for i in range(N):
        lst.append(min(graph[a][i], graph[b][i]))
    if sum(lst) <= min_dist:
        if sum(lst) < min_dist:
            chicken_place = []
        min_dist = sum(lst)
        chicken_place.append([a+1, b+1, sum(lst)*2])

print(*sorted(chicken_place, key=lambda x : (x[0], x[1]))[0])
