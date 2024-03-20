def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    # 시작시간과 끝시간 초단위로 변환
    start_time = h1*3600 + m1*60 + s1
    end_time = h2*3600 + m2*60 + s2
    
    # next기준으로 계산할 것이라 포함되지 않는 시작시간 00시, 12시 미리 카운팅
    if start_time == 0*3600 or start_time == 12*3600:
        answer += 1
        
    while start_time < end_time:
        h = start_time / 120 % 360
        m = start_time / 10 % 360
        s = start_time * 6 % 360
        
        # 다음 위치가 360도 아닌 0도로 계산되어 카운팅에 포함되지 않는 경우 방지
        nh = 360 if (start_time + 1) / 120 % 360 == 0 else (start_time + 1) / 120 % 360
        nm = 360 if (start_time + 1) / 10 % 360 == 0 else (start_time + 1) / 10 % 360
        ns = 360 if (start_time + 1) * 6 % 360 == 0 else (start_time + 1) * 6 % 360
        
        if s < h and ns >= nh:
            answer += 1
        if s < m and ns >= nm:
            answer += 1
        # 시침/분침과 동시에 겹쳤을 때 중복 카운팅 제외
        if ns == nh and nh == nm:
            answer -= 1
        
        start_time += 1
    
    return answer