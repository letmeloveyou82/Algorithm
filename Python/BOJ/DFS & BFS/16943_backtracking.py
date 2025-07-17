import sys

input = sys.stdin.readline
A, B = input().split()

A = sorted(A)  # 문자열 정렬
B = int(B)
C = 0
visited = [False] * len(A)
tmp = []

def dfs():
    global C
    if len(tmp) == len(A):
        if tmp[0] == "0":
            return
        case = int("".join(tmp))
        if case < B:
            C = max(C, case)

    remember = 0
    for i in range(len(A)):
        if not visited[i] and remember != A[i]:
            visited[i] = True
            tmp.append(A[i])
            remember = A[i]
            dfs()
            visited[i] = False
            tmp.pop()

dfs()
print(C if C != 0 else -1)