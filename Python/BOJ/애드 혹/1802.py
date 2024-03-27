import sys
input = sys.stdin.readline
T = int(input())

def solution(paper):
    now = paper
    while len(now) >= 3:
        next_tmp = []
        for i in range(1, len(now), 2):
            next_tmp.append(now[i])
            if (now[i - 1] == '0' and now[i + 1] == '0') or (now[i - 1] == '1' and now[i + 1] == '1'):
                return False
        now = next_tmp
    return True


for _ in range(T):
    paper = list(input().rstrip())
    if len(paper) == 1:
        print("YES")
    elif len(paper) > 1:
        if solution(paper):
            print("YES")
        else:
            print("NO")