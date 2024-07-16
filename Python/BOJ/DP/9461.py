import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    P = [1] * 101
    P[4] = 2
    P[5] = 2

    if N <= 5:
        print(P[N])
    else:
        for i in range(6, N+1):
            P[i] = P[i-1] + P[i-5]
        print(P[N])
