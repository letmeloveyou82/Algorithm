from collections import Counter

def solution(points, routes):
    def get_path(route):
        idx = 0
        path = []
        for i in range(len(route)-1):
            sx, sy = spots[route[i]-1]
            ex, ey = spots[route[i+1]-1]
            # x좌표 맞추기
            while sx != ex:
                path.append((sx, sy, idx))
                if sx < ex:
                    sx += 1
                else:
                    sx -= 1
                idx += 1
            # y좌표 맞추기
            while sy != ey:
                path.append((sx, sy, idx))
                if sy < ey:
                    sy += 1
                else:
                    sy -= 1
                idx += 1
        path.append((sx, sy, idx))
        return path
    
    spots = [i for i in points]
    second = []
    
    for route in routes:
        second.extend(get_path(route))
    answer = 0
    tmp = Counter(second)
    for i in tmp.values():
        if i >= 2:
            answer += 1
            
    return answer