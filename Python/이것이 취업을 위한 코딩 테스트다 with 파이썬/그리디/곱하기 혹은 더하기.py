s = list(map(int, input()))

max = s[0]

for i in range(1, len(s)):
    if s[i] <= 1 or max <= 1:
        max += s[i]
    else:
        max *= s[i]

print(max)