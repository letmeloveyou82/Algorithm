import sys
from collections import deque
input = sys.stdin.readline

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
shortest_distance = [-1] * (n+1)
shortest_distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
queue = deque([x])
while queue:
    now = queue.popleft()
    # 해당 도시에서 이동할 수 있는 모든 도시를 확인
    for i in graph[now]:
        # 아직 방문하지 않은 도시라면
        if shortest_distance[i] == -1:
            # 최단 거리 갱신
            queue.append(i)
            shortest_distance[i] = shortest_distance[now] + 1

# 최단 거리가 K인 도시가 없다면, -1 출력
if k not in shortest_distance:
    print(str(-1))
else: 
    for i in range(1, n+1): # 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
        if shortest_distance[i] == k:
            print(i)