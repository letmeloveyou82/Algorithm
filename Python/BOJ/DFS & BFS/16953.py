A, B = map(int, input().split())
result = int(1e9)
def dfs(x, depth):
    if x == B:
        global result
        result = min(result, depth)
        return
    elif x > B:
        return
    elif x < B:
        dfs(x*2, depth+1)
        dfs(x*10+1, depth+1)

dfs(A, 1)
if result == int(1e9):
    print(-1)
else:
    print(result)
