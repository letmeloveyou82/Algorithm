def solution(record):
    message = []
    answer = []
    user_dict = dict()
    
    for r in record:
        m = list(r.split())
        if m[0] == 'Enter':
            user_dict[m[1]] = m[2]
            message.append([m[1], "님이 들어왔습니다."])
        elif m[0] == 'Leave':
            message.append([m[1], "님이 나갔습니다."])
        elif m[0] == 'Change':
            user_dict[m[1]] = m[2]
        
    for i in range(len(message)):
        answer.append(str(user_dict[message[i][0]])+message[i][1])
    return answer