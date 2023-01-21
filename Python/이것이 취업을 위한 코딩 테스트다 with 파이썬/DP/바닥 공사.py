n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796 # 결과값이 굉장히 커질 수 있기 때문에 문제에서 796796으로 나눈 나머지를 출력하라고 하는 것

# 계산된 결과 출력
print(d[n])