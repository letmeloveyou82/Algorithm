import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

if max(visitors) == 0:
    print("SAD")
else:
    value = sum(visitors[0:X])
    max_value = value
    cnt = 1
    # 슬라이딩 윈도우 진행
    for i in range(X, N):
        value += visitors[i]
        value -= visitors[i-X]
        if value > max_value:
            max_value = value
            cnt = 1
        elif value == max_value:
            cnt += 1
    print(max_value)
    print(cnt)