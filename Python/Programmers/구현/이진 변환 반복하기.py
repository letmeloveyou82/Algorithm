def solution(s):
    n = 0
    zero_total = 0
    
    while True:
        if s == '1':
            break
        n += 1
        s_zero_cnt = s.count('0')
        zero_total += s_zero_cnt
        s = bin(len(s)-s_zero_cnt)[2:]
        
    return [n, zero_total]