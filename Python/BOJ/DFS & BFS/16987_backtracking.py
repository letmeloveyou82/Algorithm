import sys

def cnt_break_eggs(eggs):
    cnt = 0
    for e in eggs:
        if e[0] <= 0:
            cnt += 1
    return cnt

def solution(depth):
    global result
    if depth == N:
        result = max(result, cnt_break_eggs(eggs))
        return
    if eggs[depth][0] <= 0:
        solution(depth+1)
    else:
        is_broken = True
        for i in range(N):
            if depth != i and eggs[i][0] > 0:
                is_broken = False
                eggs[depth][0] -= eggs[i][1]
                eggs[i][0] -= eggs[depth][1]
                solution(depth+1)
                eggs[depth][0] += eggs[i][1]
                eggs[i][0] += eggs[depth][1]
        if is_broken:
            solution(N)

input = sys.stdin.readline
N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
result = 0
solution(0)
print(result)