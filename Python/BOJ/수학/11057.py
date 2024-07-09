N = int(input())
result = 1
for i in range(10, 10+N):
    result *= i
for j in range(N, 0, -1):
    result //= j
print(result%10007)