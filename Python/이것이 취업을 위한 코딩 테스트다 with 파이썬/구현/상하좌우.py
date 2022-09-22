n = int(input())
plan = list(input().split())
x = 1
y = 1

for i in plan:
    if i == 'L' and y > 1:
        y = y-1
    elif i == 'R' and y < n:
        y = y+1
    elif i == 'U' and x > 1:
        x = x-1
    elif i == 'D' and x < n:
        x = x+1

print(x,y)