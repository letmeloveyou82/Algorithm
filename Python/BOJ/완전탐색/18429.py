from itertools import permutations

n, k = map(int, input().split())
kit = list(map(int, input().split()))
count = 0

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

for case in list(permutations(kit, n)):
    weight = 500
    for i in case:
        if weight + i - k < 500:
            count += 1
            break
        else:
            weight = weight + i - k

print(factorial(n)-count)
    