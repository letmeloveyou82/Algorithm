N, K, P, X = map(int, input().split())

led = ['1111110','0110000','1101101','1111001','0110011',
       '1011011','1011111','1110000','1111111','1111011']

answer = 0
arr = []

# 자릿수 맞춰주기
x = list(str(X).zfill(K))

# i -> j로 숫자 바꿀 때 반전시켜야 하는 LED 개수 계산
for i in range(10):
    arr.append([])
    for j in range(10):
        if i == j:
            arr[i].append(0)
        else:
            l_cnt = 0
            for l in range(7):
                if led[i][l] != led[j][l]:
                    l_cnt += 1
            arr[i].append(l_cnt)

for i in range(1, N+1):
    if i == X:
        continue
    cnt = 0
    num = list(str(i).zfill(K))

    for j in range(K): # K 자리수
        a = int(x[j])
        b = int(num[j])
        cnt += arr[a][b]
    if cnt <= P:
        answer += 1
print(answer)