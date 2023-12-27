def solution(routes):
    answer = 0
    routes.sort(key=lambda x : x[1])
    camera = -30001
    for i, j in routes:
        if i <= camera:
            continue
        else:
            answer += 1
            camera = j
    return answer