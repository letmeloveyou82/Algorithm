from collections import deque
def solution(msg):
    answer = []
    word_dict = dict()
    for i in range(65, 91):
        word_dict[chr(i)] = i-64
    index_num = 27
    message = deque(msg)

    while message:
        w = message.popleft()
        while w in word_dict and message:
            w += message.popleft()
        n = len(w)
        if w in word_dict:
            answer.append(word_dict[w])
            continue
        if w[:n-1] in word_dict:
            answer.append(word_dict[w[:n-1]])
        if w not in word_dict:
            word_dict[w] = index_num
            index_num += 1
        message.appendleft(w[-1])

    return answer