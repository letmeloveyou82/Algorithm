def solution(number, limit, power):
    answer = 0
    divisor = [] # 약수의 개수 저장
    
    # 숫자마다 약수 개수 구하기
    for i in range(1, number+1):
        cnt = 0
        for j in range(1, int(i**0.5)+1): # √i까지만 확인
            if i % j == 0:
                if j * j == i: 
                    cnt += 1 # 제곱수면 약수 1개만 추가
                else: 
                    cnt += 2 # j와 i//j 두 개 추가
        divisor.append(cnt)
    
    # 제한수치 초과인지 확인
    for d in divisor:
        if d > limit:
            answer += power
        else:
            answer += d
            
    return answer