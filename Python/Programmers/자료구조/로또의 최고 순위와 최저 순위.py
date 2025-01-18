def solution(lottos, win_nums):
    answer = [0, 0]
    unknown_cnt = lottos.count(0)
    if unknown_cnt == 6:
        return [1, 6]
    
    correct_cnt = len(set(lottos) & set(win_nums))
    if correct_cnt == 6:
        return [1, 1]
    
    if correct_cnt <= 1:
        correct_cnt = 1
        
    answer[1] = 7-correct_cnt 
    answer[0] = 7-(correct_cnt+unknown_cnt)

    return answer