def solution(name, yearning, photo):
    answer = []
    score_dict = dict()
    for i in range(len(name)):
        score_dict[name[i]] = yearning[i]
    
    for p in photo:
        score = 0
        for i in range(len(p)):
            if score_dict.get(p[i]) != None:
                score += score_dict[p[i]]
        answer.append(score)
    return answer