def solution(n, w, num):
    answer = 0
    stack = [[] for _ in range(w)]
    right = True
    idx = 0
    check_idx = 0
    for i in range(1, n+1):
        stack[idx].append(i)
        if i == num:
            check_idx = idx
        if right :
            if idx == w-1:
                right = False
                continue
            idx += 1
        else:
            if idx == 0:
                right = True
                continue
            idx -= 1

    while num != stack[check_idx].pop():
        answer += 1
    return answer+1
