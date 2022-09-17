s = list(input())
all_change_0_count = 0
all_change_1_count = 0

if s[0] == '0':
    all_change_1_count += 1
else:
    all_change_0_count += 1
    
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            all_change_1_count += 1
        else :
            all_change_0_count += 1
print(min(all_change_0_count, all_change_1_count))