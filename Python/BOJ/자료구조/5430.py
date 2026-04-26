import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    p = list(input().rstrip())
    n = int(input())
    x = input().rstrip()[1:-1]

    if x == '':
        arr = deque()
    else:
        arr = deque(x.split(','))

    is_reversed = False
    error = False

    for cmd in p:
        if cmd == "R":
            is_reversed = not is_reversed
        else:
            if not arr:
                error = True
                break
            if is_reversed:
                arr.pop()
            else:
                arr.popleft()

    if error:
        print("error")
    else:
        if is_reversed:
            arr.reverse()

        print("[" + ",".join(arr) + "]")