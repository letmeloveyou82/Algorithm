# PyPy3
def dfs(depth):
    global answer
    if depth == N*M:
        answer += 1
        return
    x = depth//M+1
    y = depth%M+1

    # 넴모를 놓을 수 있는 경우
    if not board[x-1][y] or not board[x-1][y-1] or not board[x][y-1]:
        board[x][y] = True
        dfs(depth+1)
        board[x][y] = False
    dfs(depth+1) # 넴모를 안 놓음

N, M = map(int, input().split())
board = [[False] * (M+1) for _ in range(N+1)]
answer = 0

dfs(0)
print(answer)
