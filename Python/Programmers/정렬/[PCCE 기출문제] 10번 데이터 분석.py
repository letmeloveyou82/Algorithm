def solution(data, ext, val_ext, sort_by):
    condition = {"code": 0, "date" : 1, "maximum" : 2, "remain" : 3}
    answer = []
    for i in range(len(data)):
        if data[i][condition[ext]] < val_ext:
            answer.append(data[i])
    return sorted(answer, key=lambda x: x[condition[sort_by]])