import sys
input = sys.stdin.readline

m = int(input())
s = set([])
for _ in range(m):
    now = input().split()
    if now[0] == "add" and int(now[1]) not in s:
        s.add(int(now[1]))
    elif now[0] == "remove" and int(now[1]) in s:
        s.remove(int(now[1]))
    elif now[0] == "check":
        if int(now[1]) in s:
            print(1)
        else:
            print(0)
    elif now[0] == "toggle":
        if int(now[1]) in s:
            s.remove(int(now[1]))
        else:
            s.add(int(now[1]))
    elif now[0] == "all":
        s = set([i for i in range(1, 21)])
    elif now[0] == "empty":
        s = set()
        