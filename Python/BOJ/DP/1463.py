n = int(input())
d = [1] * (n+1)
d[1] = 0
if n == 1:
    print(d[1])
elif n == 2 or n == 3:
    print(1)
else:
    d[2] = 1
    d[3] = 1
    for i in range(4, n+1):
        possible = []
        if i % 3 == 0:
            possible.append(d[i//3])
        if i % 2 == 0:
            possible.append(d[i//2])
        possible.append(d[i-1])
        d[i] += min(possible)
    print(d[n])