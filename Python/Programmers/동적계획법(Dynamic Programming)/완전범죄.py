def solution(info, n, m):
    MAX = 120
    dp = [[False] * MAX for _ in range(MAX)]
    dp[0][0] = True # 아무도 훔치지 않은 초반 상태
    
    item_count = len(info)
    
    for traceA, traceB in info:
        # 도둑이 훔친 상황은 계속해서 갱신되므로 새로운 DP 테이블을 만들며 초기화함
        next_dp = [[False] * MAX for _ in range(MAX)]
        
        for a in range(n):
            for b in range(m):
                # 기존 DP 테이블이 False라면 해당 숫자는 체크 안 해도 되서 넘김
                if not dp[a][b]:
                    continue
                
                if a + traceA < n:
                    next_dp[a + traceA][b] = True
                if b + traceB < m:
                    next_dp[a][b + traceB] = True
                
        dp = [row[:] for row in next_dp]
    
    for a in range(n):
        for b in range(m):
            if dp[a][b]:
                return a
        
    return -1