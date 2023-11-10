def adjacent(x): 
    for i in range(x): # index가 행, queen[i]값이 열
        # 열이 같거나 대각선이 같으면 false
		# 두 좌표에서 행 - 행 = 열 - 열 이 같으면 두 개는 같은 대각선상에 있다.
        if queen[x] == queen[i] or abs(queen[x]-queen[i]) == x-i:
            return False
    return True

# 한 줄씩 재귀하며 dfs 실행
def dfs(x):
    global result

    if x == N:
        result += 1
    else:
        # 각 행에 퀸 놓기
        for i in range(N):
            queen[x] = i # i는 열번호 0부터 N-1까지 옮겨가면서 유망한 곳 찾기
            if adjacent(x): # 행, 열, 대각선 체크함수 true이면 백트래킹 안하고 계속 진행
                dfs(x+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    queen = [0] * N # 퀸이 몇 번째 줄에 몇 번째 칸에 있는지
    result = 0
    dfs(0)
    print(f"#{tc} {result}")