import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
words = list(input().rstrip() for _ in range(N))

first_word = words[0]
first_word_cnt = Counter(first_word)
answer = 0

for i in range(1, N):
    target_cnt = Counter(words[i])
    diff = first_word_cnt - target_cnt
    reverse_diff = target_cnt - first_word_cnt

    total_diff = sum(diff.values()) + sum(reverse_diff.values())
    len_diff = abs(len(first_word) - len(words[i]))

    if len_diff > 1:
        continue

    if len_diff == 0 and total_diff == 0: # 같은 구성을 가진 경우
        answer += 1
    elif len_diff == 0 and total_diff == 2: # 글자 하나 다른 경우
        answer += 1
    elif len_diff == 1 and total_diff == 1: # 글자 하나 추가 또는 삭제
        answer += 1

print(answer)
