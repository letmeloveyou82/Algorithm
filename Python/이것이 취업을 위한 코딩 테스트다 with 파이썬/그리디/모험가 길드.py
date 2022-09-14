n = int(input())
fear = list(map(int, input().split()))

fear.sort()
group_count = 0
tmp_adventurer = 0

for i in range(n):
    tmp_adventurer += 1
    if tmp_adventurer >= fear[i]:
        group_count += 1
        tmp_adventurer = 0
    
print(group_count)