test_num = 1

while True:
    n = int(input())
    if n == 0:
        break
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    dp = [[0] * 3 for _ in range(n)]
    
    # 초기 설정
    dp[0][1] = grid[0][1]
    dp[0][2] = dp[0][1] + grid[0][2]
    dp[1][0] = dp[0][1] + grid[1][0]
    dp[1][1] = min(dp[0][1], dp[0][2], dp[1][0]) + grid[1][1]
    dp[1][2] = min(dp[0][1], dp[0][2], dp[1][1]) + grid[1][2]

    for i in range(2, n):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + grid[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0]) + grid[i][1]
        dp[i][2] = min(dp[i-1][1], dp[i-1][2], dp[i][1]) + grid[i][2]
    print(str(test_num)+". "+str(dp[n-1][1]))
    test_num += 1
