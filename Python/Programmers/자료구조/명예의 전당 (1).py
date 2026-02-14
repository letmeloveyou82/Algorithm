def solution(k, score):
    answer = []
    min_score = []
    
    for s in score:
        if len(answer) < k:
            answer.append(s)
        else:
            for idx in range(k):
                if s > answer[idx]:
                    answer.insert(idx, s)
                    break
            answer = answer[:k]
            
        answer.sort(reverse=True)
        min_score.append(answer[-1])

    return min_score