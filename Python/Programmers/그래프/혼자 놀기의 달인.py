def solution(cards):
    answer = []
    visited = [False] * len(cards)

    def open(idx):
        cnt = 0
        while not visited[idx]:
            visited[idx] = True
            cnt += 1
            idx = cards[idx]-1
        return cnt
    
    for i in range(len(cards)):
        cnt = open(i)
        if cnt > 0:
            answer.append(cnt)

    if len(answer) == 1:
        return 0
    
    answer.sort(reverse=True)
    
    return answer[0] * answer[1]