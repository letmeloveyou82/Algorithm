def solution(s):
    answer = 0
    
    def correct(str):
        stack = []
        for i in str:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
                continue
            if len(stack) == 0 and (i == ')' or i == ']' or i == '}'):
                return False
            elif len(stack) != 0:
                if (stack[-1] == '(' and i == ')') or (stack[-1] == '[' and i == ']') or (stack[-1] == '{' and i == '}'):
                    stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False
        
    for i in range(0, len(s)):
        if correct(s[i:]+s[0:i]):
            answer += 1
        
    return answer