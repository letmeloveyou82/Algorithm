def find_clock_num(lst):
    clock_candidate = []
    clock_candidate.append(int(lst[0]+lst[1]+lst[2]+lst[3]))
    clock_candidate.append(int(lst[1]+lst[2]+lst[3]+lst[0]))
    clock_candidate.append(int(lst[2]+lst[3]+lst[0]+lst[1]))
    clock_candidate.append(int(lst[3]+lst[0]+lst[1]+lst[2]))
    return sorted(clock_candidate)[0]

nums = input().split()
cnt = 0

clock_num = find_clock_num(nums)
for i in range(1111, clock_num+1):
    tmp = list(str(i))
    if find_clock_num(tmp) == i:
        cnt += 1
print(cnt)