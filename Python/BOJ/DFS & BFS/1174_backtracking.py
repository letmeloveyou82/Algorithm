import sys
input = sys.stdin.readline

N = int(input())
decrease_num = []

def dfs(n, tmp):
    if len(tmp) == n:
        decrease_num.append(tmp)
        return

    for i in range(0, 10):
        if tmp == "" or i < int(tmp[-1]):
            tmp += str(i)
            dfs(n, tmp)
            tmp = tmp[:-1]

# 십진법으로 표기할 수 있는 숫자 최대는 10자리
for n in range(1, 11):
    dfs(n, "")

if len(decrease_num) < N:
    print(-1)
else:
    print(int(decrease_num[N - 1]))
