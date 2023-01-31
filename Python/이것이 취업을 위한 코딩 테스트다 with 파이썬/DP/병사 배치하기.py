n = int(input()) # 병사의 수
fighting_power = list(map(int, input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
fighting_power.reverse()

dp = [1] * n # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if fighting_power[j] < fighting_power[i]:
            dp[i] = max(dp[i], dp[j]+1)

# 열외시켜야 하는 병사의 최소 수를 출력
print(n-max(dp))
