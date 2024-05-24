import sys, heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # (최소 비용, 노드 번호)
    while q:
        dist, now_node = heapq.heappop(q)
        if distance[now_node] < dist:
            continue
        for i in graph[now_node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

dijkstra(1)

print(distance[-1])