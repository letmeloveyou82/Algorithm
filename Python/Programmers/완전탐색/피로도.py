from itertools import permutations
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    max_answer = -1
    
    for i in list(permutations(dungeons, n)):
        cnt = 0
        temp_k = k
        for min_required_fatigue, consumed_fatigue in i:
            if temp_k >= min_required_fatigue:
                temp_k -= consumed_fatigue
                cnt += 1
            else:
                break
        if max_answer < cnt:
            max_answer = cnt
        if max_answer == n:
            return n
        
    return max_answer