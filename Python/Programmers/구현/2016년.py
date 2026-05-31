def solution(a, b):
    now = 5
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    for i in range(a-1):
        now += day[i]
    now += b
    
    return days[now%7-1]