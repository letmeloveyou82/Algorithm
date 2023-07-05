str = input()
explosion_str = input()

stack = []
ex_len = len(explosion_str)
for i in range(len(str)):
    stack.append(str[i])
    if "".join(stack[-ex_len:]) == explosion_str:
        for _ in range(ex_len):
            stack.pop()
            
if stack:
    print("".join(stack))
else:
    print("FRULA")