import sys
input = sys.stdin.readline

L, C = map(int, input().split())
chars = sorted(list(input().split()))

def dfs(start, password, v_cnt, c_cnt): # 시작 idx, 암호, 모음 개수, 자음 개수
    if len(password) == L:
        if v_cnt >= 1 and c_cnt >= 2:
            print(password)
        return
    
    tmp = password
    for i in range(start, C):
        tmp += chars[i]
        if chars[i] == 'a' or chars[i] =='e' or chars[i] == 'i' or chars[i] == 'o' or chars[i] == 'u':
            dfs(i+1, tmp, v_cnt+1, c_cnt)
        else:
            dfs(i+1, tmp, v_cnt, c_cnt+1)
        tmp = tmp[0:len(tmp)-1]

dfs(0, "", 0, 0)
