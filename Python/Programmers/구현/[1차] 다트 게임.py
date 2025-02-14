def solution(dartResult):
    score = []
    matching_dict = {"S" : 1, "D" : 2, "T" : 3}
    n = ""
    for i in dartResult:
        if i.isdigit():
            n += i
        elif i == "S" or i == "D" or i == "T":
            n = int(n) ** matching_dict[i]
            score.append(n)
            n = ""
        elif i == "*":
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == "#":
            score[-1] = score[-1] * -1
            
    return sum(score)