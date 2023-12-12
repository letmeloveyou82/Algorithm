N = int(input())
record = list(map(int, input().split()))
answer = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == record[i] and answer[j] == 0:
            answer[j] = i+1
            break
        elif answer[j] == 0:
            cnt += 1

print(' '.join(map(str, answer)))