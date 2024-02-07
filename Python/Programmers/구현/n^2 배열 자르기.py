def solution(n, left, right):
    array_1d = []
    value = 0
    
    for i in range(left, right+1):
        x = i // n
        y = i % n
        if y <= x:
            value = x+1
        else:
            value = y+1
        array_1d.append(value)
        
    return array_1d