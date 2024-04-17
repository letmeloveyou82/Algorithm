from collections import deque
def solution(queue1, queue2):
    answer = -1
    max_len_queue1 = len(queue1)*2
    max_len_queue2 = len(queue2)*2
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    check1 = False
    max_cnt = 0
    
    while True:
        if max_cnt == 600000:
            return -1
        max_cnt += 1
        answer += 1
        if sum_q1 == sum_q2:
            break
        elif sum_q1 < sum_q2:
            x = q2.popleft()
            sum_q2 -= x
            q1.append(x)
            sum_q1 += x
        else:
            x = q1.popleft()
            sum_q1 -= x
            q2.append(x)
            sum_q2 += x
        if len(q1) == max_len_queue1 or len(q2) == max_len_queue2:
            check1 = True
        if check1 and (len(q1) == len(queue1) or len(q2) == len(queue2)):
            return -1
    return answer