import math

def solution(progresses, speeds):
    answer = []
    day = math.ceil((100 - progresses[0]) / speeds[0])
    cnt = 1
    for i in range(1, len(progresses)):
        need_days = math.ceil((100 - progresses[i]) / speeds[i])
        if need_days <= day:
            cnt += 1
        else:
            day = need_days
            answer.append(cnt)
            cnt = 1
        
        if i == len(progresses)-1:
            answer.append(cnt)

    return answer