def solution(a, b, n):
    # a : 빈 병 개수
    # b : 받는 개수
    
    answer = 0
    while n >= a:
        q = n // a
        coke = q*b
        
        answer += coke
        n = n - q*a + coke
    return answer