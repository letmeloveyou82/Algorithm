from math import lcm

def solution(signals):
    limit = 1
    
    # 주기들의 최소공배수 구함
    for G, Y, R in signals:
        limit = lcm(limit, G+Y+R)
    
    for t in range(1, limit+1):
        ok = True
        
        for G, Y, R in signals:
            cycle = G+Y+R
            pos = (t-1) % cycle # 현재 시간 t가 신호등의 한 주기 안에서 몇 번째 위치인지
            
            # 초록 : 0 ~ G-1
            # 노랑 : G ~ G+Y-1
            # 빨강 : G+Y ~ cycle-1
            if not (G <= pos < G+Y):
                ok = False
                break
                
        if ok:
            return t
            
    return -1