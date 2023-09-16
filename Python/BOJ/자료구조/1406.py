import sys
input = sys.stdin.readline
str1 = list(input().rstrip())
str2 = []

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == "L":
        # 커서 왼쪽으로 한 칸 옮김
        if str1:
            str2.append(str1.pop())
    elif command[0] == "D":
        # 커서 오른쪽으로 한 칸 옮김
        if str2:
            str1.append(str2.pop()) 
    elif command[0] == "B":
        # 커서 왼쪽에 있는 문자 삭제함
        if str1:
            str1.pop()
    else:
        # command[1]라는 문자를 커서 왼쪽에 추가함
        str1.append(command[1])

str1.extend(reversed(str2))
print("".join(str1))