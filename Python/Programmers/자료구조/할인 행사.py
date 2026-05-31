from collections import defaultdict, Counter

def solution(want, number, discount):
    answer = 0
    want_dict = defaultdict(int)
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
        
    for i in range(0, len(discount)-9):
        c = Counter(discount[i:i+10])
        if want_dict == c:
            answer += 1
    return answer