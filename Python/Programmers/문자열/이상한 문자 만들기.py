def solution(s):
    answer = ''
    s = s.split(' ')
    for i in s:
        for j in range(len(i)):
            if j % 2 == 1: # 홀수
                answer += i[j].lower()
            else:
                answer += i[j].upper()
        answer += ' '
        
    return answer[:-1]