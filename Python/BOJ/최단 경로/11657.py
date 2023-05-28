import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split()) # 도시(노드) 개수, 버스 노선(간선)의 개수
graph = []
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split()) # 시작도시 a, 도착도시 b, 걸리는 시간 c 
    graph.append((a,b,c))

# 벨만 - 포드 알고리즘 
def bellmanFord(start):
    distance[start] = 0 # 시작 노드에 대해 초기화
    for i in range(n): # n번 edge relaxation을 반복
        for j in range(m): # 매 반복마다 모든 간선을 확인하며 갱신
            a, b, c = graph[j]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[a] != INF and distance[a] + c < distance[b]:
                distance[b] = distance[a] + c
                # n번째 반복에서 갱신되는 값이 있으면 Negative cycle 존재
                if i == n - 1:
                    print("-1")
                    exit(0) # 프로그램 종료
bellmanFord(1)
for i in range(2, n+1):
    if distance[i] == INF:
        print("-1")
    else:
        print(distance[i])