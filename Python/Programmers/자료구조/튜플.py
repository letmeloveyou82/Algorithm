from collections import defaultdict

def solution(s):
    answer = []
    s = s[2:len(s)-2]
    s = s.split("},{")
    s_dict = defaultdict(int)
    for i in s:
        for j in list(map(int, i.split(','))):
            s_dict[j] += 1
    now = len(s_dict)
    while now > 0:
        for key in s_dict.keys():
            if s_dict[key] == now:
                answer.append(key)
                now -= 1
    return answer