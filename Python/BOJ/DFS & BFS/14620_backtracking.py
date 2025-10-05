import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx, dy = [0, 0, 0, -1, 1], [0, -1, 1, 0, 0]
answer = float('inf')

# 5칸 모두 비어있는지 확인
def can_place(x, y):
    for d in range(5):
        nx, ny = x+dx[d], y+dy[d]
        if visited[nx][ny]:
            return False
    return True

# 다섯 칸 일괄 표시/해제 하고, 비용(표시할 때만) 반환
def place(x, y, flag):
    add = 0
    for d in range(5):
        nx, ny = x+dx[d], y+dy[d]
        visited[nx][ny] = flag
        if flag:
            add += board[nx][ny]
    return add

def dfs(start_idx, flower, cost):
    global answer
    if cost >= answer : # 가지치기
        return
    if flower == 3:
        answer = min(answer, cost)
        return

    # 선형 탐색으로 해서 중복 조합 방지
    m = (N-2) * (N-2)
    for pos in range(start_idx, m):
        i = pos // (N-2) + 1
        j = pos % (N-2) + 1
        if can_place(i, j):
            add = place(i, j, True)
            dfs(pos+1, flower+1, cost+add)
            place(i, j, False)

dfs(0, 0, 0)
print(answer)