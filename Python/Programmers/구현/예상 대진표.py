def solution(n,a,b):
    answer = -1
    cnt = n
    while cnt > 0:
        cnt //= 2
        answer += 1

    # 절반 잘라서 봤을 때 다른 쪽이면 무조건 최대 answer가 정답
    n //= 2
    if (a <= n and b > n) or (b <= n and a > n):
        return answer
        
    # 절반 잘라서 봤을 때 같은 쪽이면 언제 만나는지 확인
    cnt = 0
    while n >= 2 and a != b:
        if a % 2 == 1:
            a += 1
        if b % 2 == 1:
            b += 1
        a //= 2
        b //= 2
        cnt += 1
    return cnt