# 플로이드 워셜
N = int(input()) 
M = int(input())
INF = int(1e9)
graph = [[INF] * N for _ in range(N)]
temp = []

for i in range(N):
    temp.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
        if i == j:
            graph[i][j] = 0
        # 도시 사이에 길이 있으면 1로 설정
        elif temp[i][j] == 1:
            graph[i][j] = 1

travel_plan = list(map(int, input().split()))

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for i in range(len(travel_plan)-1):
    # 도달할 수 없는 경우 "NO" 출력 후 종료
    if graph[travel_plan[i]-1][travel_plan[i+1]-1] == INF:
        print("NO")
        exit(0)
# 도달할 수 있는 경우 "YES" 출력
print("YES")
