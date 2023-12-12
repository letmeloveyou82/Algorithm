n, k = map(int, input().split())
num = [True for i in range(n+1)]

def solution():
    count = 0
    for i in range(2, n+1):
        if num[i]:
            j = 1
            while i*j <= n:
                if num[i*j]:
                    num[i*j] = False
                    count += 1
                    if count == k:
                        print(i * j)
                        return
                j += 1
                
solution()