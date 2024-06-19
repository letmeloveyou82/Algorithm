import math

def solution(n, stations, w):
    answer = 0
    no_spread = [] # 전파 전달이 안 되는 구간 길이 저장
    for i in range(1, len(stations)):
        no_spread.append((stations[i]-w-1)-(stations[i-1]+w))
        
    no_spread.append(stations[0]-w-1) # 맨앞
    no_spread.append(n-(stations[-1]+w)) # 맨뒤
    
    for i in no_spread:
        if i <= 0:
            continue
        else:
            answer += math.ceil(i/(2*w+1))
            
    return answer