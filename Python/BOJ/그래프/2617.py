import sys

# 연결된 구슬 개수 구하기
def dfs(lst, root):
    cnt = 0
    for node in lst[root]:
        if not visited[node]:
            visited[node] = True
            cnt += 1
            cnt += dfs(lst, node)
    return cnt

input = sys.stdin.readline
N, M = map(int, input().split())
answer = 0

heavy_list = [[] for _ in range(N+1)] # 인덱스 구슬보다 무거운 구슬 번호 저장하는 리스트
light_list = [[] for _ in range(N+1)] # 인덱스 구슬보다 가벼운 구슬 번호 저장하는 리스트

for _ in range(M):
    a, b = map(int, input().split()) # a > b
    heavy_list[a].append(b)
    light_list[b].append(a)

mid = (N+1)/2
for root in range(1, N+1):
    visited = [False] * (N+1)
    if dfs(heavy_list, root) >= mid:
        answer += 1
    if dfs(light_list, root) >= mid:
        answer += 1

print(answer)
