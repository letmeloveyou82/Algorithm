def solution(s, skip, index):
    answer = ''
    skip_set = set(skip)
    
    for ch in s:
        cur = ord(ch)
        moved = 0
        
        while moved < index:
            cur += 1
            if cur > ord('z'):
                cur = ord('a')
            if chr(cur) in skip_set:
                continue
            moved += 1
        answer += chr(cur)
        
    return answer