import sys
input = sys.stdin.readline

num = input().rstrip()

now = 0
idx = 0

while True:
    now += 1
    for s in str(now):
        if num[idx] == s:
            idx += 1
            if idx >= len(num):
                print(now)
                exit(0)