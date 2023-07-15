def solution(participant, completion):
    participant.sort() # 오름차순 정렬
    completion.sort() # 오름차순 정렬
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]