from collections import Counter
alpha = input()
count = Counter(alpha.upper()).most_common()

if len(count) == 1 or count[0][1] != count[1][1]:
    print(count[0][0])
else:
    print("?")
