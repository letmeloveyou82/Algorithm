import sys
input = sys.stdin.readline
str1 = input().rstrip()
str2 = input().rstrip()

prev = [0] * (len(str2)+1)
answer = 0

for i in range(len(str1)):
    tmp = [0] * (len(str2)+1)
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            tmp[j+1] = prev[j] + 1
    answer = max(max(tmp), answer)
    prev = tmp[:]

print(answer)