from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    count = sorted(counter.values(), reverse=True)
    
    total = 0
    for idx, c in enumerate(count):
        total += c
        if k <= total:
            return idx+1
        
    return len(count)