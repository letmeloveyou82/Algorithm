from collections import deque
def solution():
    while True:
        for i in range(1, 6):
            if num[-1] <= 0:
                num[-1] = 0
                return
            num[0] -= i
            x = num.popleft()
            num.append(x)

for _ in range(1, 11):
    test_case = int(input())
    num = deque(list(map(int, input().split())))
    solution()
    result = ""
    for i in num:
        result += str(i) + " "
    result.rstrip()
    print(f"#{test_case} {result}")