from collections import deque
def solution(progresses, speeds):
    remain_day = deque([])
    for i in range(len(progresses)):
        day = 0
        while progresses[i] < 100: 
            progresses[i] += speeds[i]
            day += 1
        remain_day.append(day)

    result = []
    remember = 0
    while remain_day:
        if len(remain_day) == len(progresses):
            remember = remain_day.popleft()
        elif remember <= remain_day[0]:
            remember = remain_day.popleft()
        else:
            remain_day.popleft()
        result.append(remember)

    count_result = {}
    for i in result:
        count_result[i] = count_result.get(i, 0) + 1
    return list(count_result.values())