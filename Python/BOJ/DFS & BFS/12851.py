from collections import deque

N, K = map(int, input().split()) # 수빈, 동생
visited = [0] * 100001 # 최대 0부터 100000까지 지점까지 걸리는 횟수 기록

# BFS 탐색
q = deque()
q.append(N) # 시작점

min_time, cnt = 0, 0 # 동생 찾는 가장 빠른 시간, 가장 빠른 시간으로 동생 찾는 방법의 수

while q:
    x = q.popleft()
    if x == K: # 도착지점이면 탐색 종료
        min_time = visited[x]
        cnt += 1
        continue

    for nx in [x+1, x-1, 2*x]:
        # 범위 내이고, 방문하지 않았거나 동일한 탐색횟수를 가졌으면 탐색
        if 0<=nx<=100000 and (visited[nx] == 0 or visited[nx] == visited[x]+1):
            visited[nx] = visited[x]+1 # 방문하고 횟수 1 늘림
            q.append(nx)
            
print(min_time)
print(cnt)