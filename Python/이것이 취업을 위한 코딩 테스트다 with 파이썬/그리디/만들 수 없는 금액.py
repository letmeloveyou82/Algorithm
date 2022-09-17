coin_num = int(input())
monetary_unit = list(map(int, input().split()))
monetary_unit.sort()
min = 1
if 1 in monetary_unit:
    for i in monetary_unit:
        if min < i:
            break
        min += i
        
print(min)