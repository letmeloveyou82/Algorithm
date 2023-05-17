import sys
input = sys.stdin.readline

# 입력
n = int(input())
arr = [[] for _ in range(n+1)]
for i in range(n):
    arr[i+1].append(int(input()))

def dfs(v, i):
    visited[v] = True
    for x in arr[v]:
        if not (visited[x]):
            dfs(x, i)
        elif visited[x] and x == i:
            result.append(x)

result = [] # 결과 담을 리스트
for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i, i)

# 결과 출력
length = len(result)
print(length)
for i in range(length):
    print(result[i])
