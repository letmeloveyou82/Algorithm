INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
n, m = map(int, input().split()) # 전체 회사(노드) 개수 N, 경로(간선) 개수 M 입력받기
graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트(그래프 표현) 만들고, 모든 값을 무한으로 초기화

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # 양방향이기 때문에 서로에게 가는 비용은 1로 설정
    c, d = map(int, input().split())
    graph[c][d] = 1
    graph[d][c] = 1

x, k = map(int, input().split()) # 거쳐갈 노드 X와 최종 목적지 노드 K 입력받기

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

# 1에서 k까지의 최단 거리 + k에서 x까지의 최단 거리
distance = graph[1][k]+graph[k][x]

if distance >= INF: # 도달할 수 없는 경우, -1을 출력
    print("-1")
else: # 도달할 수 있다면, 최단 거리를 출력
    print(distance)