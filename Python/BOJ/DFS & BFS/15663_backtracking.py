# 백트래킹 사용
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    remember = 0
    for i in range(n):
        if not visited[i] and remember != num[i]:
            visited[i] = True
            temp.append(num[i])
            remember = num[i]
            dfs()
            visited[i] = False
            temp.pop()

dfs()