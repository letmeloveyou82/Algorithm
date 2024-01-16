import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
first_word = input().rstrip()
answer = 0

for _ in range(N-1):
    first_word_component = Counter(first_word)
    now_word = input().rstrip()
    now_word_component = Counter(now_word)
    if first_word_component == now_word_component:
        answer += 1
    else:
        similar_word = True
        first_word_component.subtract(now_word_component)
        diff = list(first_word_component.values())
        for i in diff: # 한 문자 교체해도 비슷한 단어 안 되는 경우
            if i <= -2 or i >= 2:
                similar_word = False
                break
        if diff.count(1) >= 2 or diff.count(-1) >= 2: # 한 문자 더하거나 빼도 비슷한 단어 안 되는 경우
            similar_word = False
        if similar_word:
            answer += 1
print(answer)