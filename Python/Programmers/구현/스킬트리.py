def solution(skill, skill_tree):
    answer = 0
    for i in skill_tree:
        tmp = ''
        for z in i:
            if z in skill:
                tmp += z
        if tmp == skill[0:len(tmp)]:
            answer += 1
    return answer