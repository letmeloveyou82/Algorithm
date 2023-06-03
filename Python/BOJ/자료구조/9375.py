import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    clothes_dict = {}
    for i in range(n):
        name, type = map(str, input().split())
        if clothes_dict.get(type) != None:
            clothes_dict[type].append(name)
        else:
            clothes_dict[type] = [name]
    result = 1 # 경우의 수 계산할 변수
    for j in clothes_dict:
        result *= (len(clothes_dict[j])+1) # 의상 종류를 착용하지 않아도 경우 +1
    print(result - 1) # 아예 의상을 입지 않는 경우 -1
