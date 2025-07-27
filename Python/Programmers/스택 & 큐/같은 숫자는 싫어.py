from collections import deque

def solution(arr):
    answer = []
    q = deque(arr)
    while q:
        x = q.popleft()
        while q:
            if x == q[0]:
                q.popleft()
            else:
                break
        answer.append(x)
        
    return answer