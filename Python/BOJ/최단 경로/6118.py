import sys, heapq

input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append([b, 1])
    graph[b].append([a, 1])
distance = [INF] * (N+1)

# 다익스트라
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, [0, start]) # [거리, 노드]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for n, c in graph[now]: # 노드, 거리
            cost = c + dist
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, [cost, n])

dijkstra(1)
d = max(distance[1:])
num = distance.index(d)
cnt = distance.count(d)
print(num, d, cnt)