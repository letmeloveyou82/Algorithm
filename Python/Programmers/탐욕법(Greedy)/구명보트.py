def solution(people, limit):
    answer = 0
    people.sort()
    i1 = 0
    i2 = len(people)-1
    visited = [False] * (len(people))

    while i1 < i2:
        while i1 < i2:
            if not visited[i1] and not visited[i2] and people[i1] + people[i2] <= limit:
                visited[i1] = True
                visited[i2] = True
                break
            i2 -= 1
        answer += 1
        visited[i1] = True
        i1 += 1
        
    for v in visited:
        if not v:
            answer += 1
    return answer