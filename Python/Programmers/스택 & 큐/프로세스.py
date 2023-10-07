from collections import deque
def solution(priorities, location):
    answer = 0
    waiting = deque([])
    for idx, p in enumerate(priorities):
        waiting.append([idx, p])

    while waiting:
        idx, x = waiting.popleft()
        x_is_first = True
        for i in range(len(waiting)):
            if waiting[i][1] > x:
                waiting.append([idx, x])
                x_is_first = False
                break
        if x_is_first:
            answer += 1
            if idx == location:
                return answer