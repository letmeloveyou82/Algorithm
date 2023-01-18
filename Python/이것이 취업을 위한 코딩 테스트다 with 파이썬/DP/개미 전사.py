n = int(input()) # 정수 N을 입력받기
food_warehouse = list(map(int, input().split())) # 모든 식량 정보 입력받기

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = food_warehouse[0]
d[1] = max(food_warehouse[0], food_warehouse[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+food_warehouse[i])

# 계산된 결과 출력
print(d[n-1])