import sys

input = sys.stdin.readline 
n = int(input())
P = [list(map(int, input().split())) for _ in range(n)]

def score(c):
    result = 0
    for i in range(n//2):
        for j in range(i+1, n//2):
            result += P[c[i]][c[j]]
            result += P[c[j]][c[i]]
    return result

def dfs(idx, depth):
    global answer
    if depth == n//2:
        tmp2 = [i for i in range(n) if i not in tmp]
        answer = min(answer, abs(score(tmp) - score(tmp2)))
    
    for i in range(idx+1, n):
        tmp.append(i)
        dfs(i, depth+1)
        tmp.pop()

tmp = [0]
answer = float('inf')

dfs(0, 1)
print(answer)