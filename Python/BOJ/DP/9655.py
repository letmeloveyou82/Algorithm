n = int(input()) # 돌의 개수
d = [0] * 1001 # 앞서 계산된 결과를 저장하기 위한 DP 테이블(이기는 사람) 초기화
# n = 1
d[1] = 1 # 상근 win 

# n = 2
d[2] = 2 # 창영 win

# n = 3 
d[3] = 1 # 상근 win

for i in range(4, n+1):
    d[i] = d[i-3]
    if d[i] == 1:
        d[i] = 2
    else:
        d[i] = 1

if d[n] == 1:
    print("SK")
elif d[n] == 2:
    print("CY")