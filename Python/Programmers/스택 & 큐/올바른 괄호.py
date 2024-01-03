def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0 and i == ')':
            return False
        if i == '(':
            stack.append('(')
        if i == ')' and stack[-1] == '(':
            stack.pop()

    return False if len(stack) != 0 else True