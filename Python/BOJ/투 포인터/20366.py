import sys
input = sys.stdin.readline

N = int(input())
H = sorted(list(map(int, input().split())))
diff = float('inf')

for i in range(N-3):
    for j in range(i+3, N):
        fix = H[i] + H[j]
        left, right = i+1, j-1
        while left < right:
            now = H[left] + H[right]
            if abs(now-fix) < diff:
                diff = abs(now-fix)

            if now < fix:
                left += 1
            elif now > fix:
                right -= 1
            else:
                print(0)
                sys.exit(0)

print(diff)