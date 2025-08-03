import sys

words = sys.stdin.readline().rstrip()
n = len(words)
result = ["" for _ in range(n)]

def solution(input_words, start_idx):
    global result
    if input_words == "":
        return

    min_char = min(input_words)
    min_char_idx = input_words.index(min_char)

    result[start_idx+min_char_idx] = min_char
    print("".join(result))

    solution(input_words[min_char_idx+1:], start_idx+min_char_idx+1)
    solution(input_words[:min_char_idx], start_idx)

solution(words, 0)