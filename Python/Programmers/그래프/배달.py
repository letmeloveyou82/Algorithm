import heapq

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    time = [int(1e9)] * (N+1) # 최단시간 저장하기 위한 리스트

    for i in range(len(road)):
        a, b, c = road[i]
        graph[a].append((b, c)) # a번 노드에서 b번 노드로 가는 시간이 c라는 의미
        graph[b].append((a, c))
    
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start)) # (최단시간, 노드번호)
        time[start] = 0
        while q:
            t, now = heapq.heappop(q)
            if time[now] < t:
                continue
            for i in graph[now]: # i는 (인접한 노드, 그 노드까지 가는 시간)
                cost = t + i[1]
                if cost < time[i[0]]:
                    time[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(1)

    for i in range(1, N+1):
        if time[i] <= K:
            answer += 1
            
    return answer