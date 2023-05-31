import sys
import heapq
input = sys.stdin.readline
n, m, x = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split()) # 시작점, 끝점, 소요시간
    graph[s].append((e,t))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # (최단 거리, 노드 번호)
    distance[start] = 0
    while q: 
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

result = [0] * (n+1)
for i in range(1, n+1):
    distance = [INF] * (n+1)
    dijkstra(i)
    if i == x:
        for j in range(1, n+1):
            result[j] += distance[j]
    else:
        result[i] += distance[x]
print(max(result))