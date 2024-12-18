def solution(survey, choices):
    answer = ''
    p_type = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    score = [3, 2, 1, 0, 1, 2, 3]
    for i in range(len(survey)):
        if 1 <= choices[i] <= 3:
            p_type[survey[i][0]] += score[choices[i]-1]
        elif 5 <= choices[i] <= 7:
            p_type[survey[i][1]] += score[choices[i]-1]
    
    for i in ["RT", "CF", "JM", "AN"]:
        if p_type[i[0]] >= p_type[i[1]]:
            answer += i[0]
        else:
            answer += i[1]
    return answer