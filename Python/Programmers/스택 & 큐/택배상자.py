def solution(order):
    answer = 0
    sub = []
    box = 1

    for target in order:
        while box <= len(order) and box < target:
            sub.append(box)
            box += 1 
            
        if box == target:
            answer += 1
            box += 1
        elif sub and sub[-1] == target:
            sub.pop()
            answer += 1
        else:
            break
            
    return answer