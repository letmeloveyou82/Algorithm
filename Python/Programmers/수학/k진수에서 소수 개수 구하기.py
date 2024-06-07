# 10진수를 k진수로 변환 
def convert(n, k):
    s = ""
    while n:
        s += str(n % k)
        n //= k
    return s[::-1]

# 소수 판별
def is_prime_number(num):
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0: 
            return False
        i += 1
    return True
    
def solution(n, k):
    answer = 0
    num = convert(n, k)
    num = num.split('0')
    for i in num:
        if i != '' and is_prime_number(int(i)):
            answer += 1
    return answer