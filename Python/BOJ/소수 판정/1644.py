N = int(input())

# 1. N보다 작거나 같은 소수들을 prime_num 리스트에 담아둔다.
nums = [True for i in range(N+1)]
prime_num = []

# 에라토스테네스의 체 알고리즘
for i in range(2, int(N**(1/2))+1):
    if nums[i] == True:
        j = 2
        while i * j <= N:
            nums[i*j] = False
            j += 1

for i in range(2, N+1):
    if nums[i]:
        prime_num.append(i)

# 2. 투포인터 사용해 합이 N인 경우 result에 +1 한다.
result = 0
left, right = 0, 0
now = 0

while left < len(prime_num):
    while now < N and right < len(prime_num):
        now += prime_num[right]
        right += 1
    if now == N:
        result += 1
    now -= prime_num[left]
    left += 1

print(result)