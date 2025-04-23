from collections import deque
def solution(plans):
    def minute_time(str):
        h, m = map(int, str.split(":"))
        return h*60 + m
    
    answer = []
    plans.sort(key=lambda x:minute_time(x[1]))
    plans = deque([[name, minute_time(start), int(playtime)] for name, start, playtime in plans])
    stack = [] # stack (name, 남은 playtime)
    current_time = plans[0][1]
    
    while plans:
        name, start, playtime = plans.popleft()
        # 이전 과제 있으면 먼저 처리
        while stack and current_time < start:
            prev_name, remain_time = stack.pop()
            time_gap = start - current_time
            
            # 멈춰둔 과제 모두 처리 가능
            if remain_time <= time_gap:
                current_time += remain_time
                answer.append(prev_name)
            else: # 다 못 끝내면 남은 시간들로만 진행하고 다시 push 
                remain_time -= time_gap
                stack.append([prev_name, remain_time])
                current_time = start
                break # 새 과제 시작해야 해서 멈춤
        
        # 새 과제 시작
        stack.append([name, playtime])
        current_time = start
    
    # 남아 있는 멈춘 과제 처리
    while stack:
        name, _ = stack.pop()
        answer.append(name)
        
    return answer