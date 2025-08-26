import sys

input = sys.stdin.readline
N = input().rstrip()
min_odd, max_odd = float('inf'), 0

def count_odd(numbers: str):
    cnt = 0
    for i in numbers:
        if int(i) % 2 == 1:
            cnt += 1
    return cnt

def solution(numbers, cnt):
    global max_odd, min_odd
    if len(numbers) == 1:
        min_odd = min(min_odd, cnt)
        max_odd = max(max_odd, cnt)
    elif len(numbers) == 2:
        tmp = str(int(numbers[0])+int(numbers[1]))
        solution(tmp, cnt + count_odd(tmp))
    else:
        for i in range(len(numbers)-2):
            for j in range(i+1, len(numbers)-1):
                a = numbers[:i+1]
                b = numbers[i+1:j+1]
                c = numbers[j+1:]
                tmp = str(int(a)+int(b)+int(c))
                solution(tmp, cnt + count_odd(tmp))

solution(N, count_odd(N))
print(min_odd, max_odd)