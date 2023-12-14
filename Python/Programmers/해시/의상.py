from collections import defaultdict

def solution(clothes):
    answer = 1

    clothes_dict = defaultdict(list)
    for sample, category in clothes:
        clothes_dict[category].append(sample)

    for key in clothes_dict.keys():
        answer *= len(clothes_dict[key]) + 1

    answer -= 1
    return answer