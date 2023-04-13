n = int(input()) # 우리의 크기
d = [1] * (n+1) # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d[1] = 3
if n == 1:
    print(d[1])
else:
    for i in range(2, n+1):
        d[i] = (d[i-1]*2+d[i-2]) % 9901
    print(d[n])
