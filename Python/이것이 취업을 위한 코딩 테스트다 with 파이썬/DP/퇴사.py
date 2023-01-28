n = int(input()) # 전체 상담 개수
array = []
for _ in range(n):
    array.append(list(map(int, input().split()))) # 각 상담의 기간, 금액 입력받기

dp = [0] * (n+1) # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
max_value = 0

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):
    time = array[i][0]+i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(array[i][1] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)