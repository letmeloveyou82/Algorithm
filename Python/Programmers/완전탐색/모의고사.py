def solution(answers):
    answer = []
    correct_cnt = [[0, 1], [0, 2], [0, 3]]
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if p1[i%5] == answers[i]:
            correct_cnt[0][0] += 1
        if p2[i%8] == answers[i]:
            correct_cnt[1][0] += 1
        if p3[i%10] == answers[i]:
            correct_cnt[2][0] += 1
            
    correct_cnt = sorted(correct_cnt, key=lambda x:(-x[0], x[1]))
    answer.append(correct_cnt[0][1])
    for i in range(2):
        if correct_cnt[0][0] == correct_cnt[i+1][0]:
            answer.append(correct_cnt[i+1][1])
        
    return answer