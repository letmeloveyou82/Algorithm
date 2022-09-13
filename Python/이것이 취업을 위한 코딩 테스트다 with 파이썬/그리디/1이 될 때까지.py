# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
    if n == 1: # n이 1이 되면 반복문 탈출
        break
    elif n % k == 0: # n이 k로 나누어떨어지는 수라면 n을 k로 나눈 몫으로 업데이트
        n = n // k
        result += 1
    else : # n이 1도 아니고, n이 k로 나누어떨어지는 수가 아니라면 1씩 빼기
        n -= 1
        result += 1

print(result)