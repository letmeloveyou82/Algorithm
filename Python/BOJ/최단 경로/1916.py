import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [float('inf') for _ in range(N+1)]
q = []

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start_city, end_city = map(int, input().split())

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(q, [0, start]) # [현재까지 비용, 노드번호]

    while q:
        c, n = heapq.heappop(q)
        if distance[n] < c:
            continue
        for i in graph[n]:
            cost = c + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start_city)
print(distance[end_city])
