def solution(sticker):
    answer = 0
    n = len(sticker)
    if n == 1:
        return sticker[0]
    dp = [0 for _ in range(n)] # 맨 앞 스티커 사용했다고 가정
    dp2 = [0 for _ in range(n)] # 맨 앞 스티커를 사용하지 않았다고 가정
    
    dp[0] = sticker[0]
    dp[1] = sticker[0]
    
    dp2[0] = 0
    dp2[1] = sticker[1]
    
    for i in range(2, n-1):
        dp[i] = max(dp[i-1], dp[i-2]+sticker[i])
    
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])
    
    return max(max(dp), max(dp2))