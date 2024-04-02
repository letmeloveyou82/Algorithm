from collections import deque
def solution(cacheSize, cities):
    cache_q = deque()
    time = 0
    
    if cacheSize == 0:
        return len(cities)*5
    
    for city in cities:
        find_city = False
        for i in range(len(cache_q)):
            if cache_q[i] == city.upper():
                time += 1
                cache_q.remove(cache_q[i])
                cache_q.append(city.upper())
                find_city = True
                break
        
        if not find_city:
            time += 5
            if len(cache_q) == cacheSize:
                cache_q.popleft()
            cache_q.append(city.upper())
        
    return time