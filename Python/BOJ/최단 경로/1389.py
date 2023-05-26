INF = int(1e9) # 무한값으로 10억 설정
n, m = map(int, input().split()) # 유저의 수(노드 수), 친구 관계의 수(간선 수)
graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트(그래프 표현)를 만들고, 모든 값 무한으로 초기화
kevin_bacon_num = []
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 케빈 베이커 수 계산
for i in range(1, n+1):
    sum = 0
    for j in range(1, n+1):
        if graph[i][j] != INF:
            sum += graph[i][j] 
    kevin_bacon_num.append((sum, i))
print(sorted(kevin_bacon_num, key= lambda x : (x[0], x[1])).pop(0)[1]) # 정렬 우선순위 1. 케빈 베이커 수 2. 유저 번호