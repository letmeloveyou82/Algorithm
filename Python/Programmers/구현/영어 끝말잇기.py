def solution(n, words):
    talk = [words[0]]
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in talk or len(words[i]) == 1:
            return [i%n+1, i//n+1]
        talk.append(words[i])
    return [0, 0]