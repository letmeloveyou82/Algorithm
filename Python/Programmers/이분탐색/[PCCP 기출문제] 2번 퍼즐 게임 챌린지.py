def solution(diffs, times, limit):
    max_level = max(diffs)
    left, right = 1, max_level
    answer = max_level
    
    while left < right:
        level = (left+right)//2
        time = times[0]
        for i in range(1, len(diffs)):
            k = 0
            if level < diffs[i]:
                k = diffs[i] - level 
            time += (times[i] + times[i-1]) * k + times[i]
        
        if time <= limit:
            right = level
            answer = level
        else:
            left = level + 1
            
    return answer