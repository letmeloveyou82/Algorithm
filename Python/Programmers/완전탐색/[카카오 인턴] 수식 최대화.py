from itertools import permutations
from collections import deque

def operation(n1, n2, op):
    if op == '+':
        return str(int(n1)+int(n2))
    if op == '-':
        return str(int(n1)-int(n2))
    if op == '*':
        return str(int(n1)*int(n2))
    
def calculate(exp, op):
    array = []
    tmp = ""
    for i in exp:
        if i.isdigit():
            tmp += i
        else:
            array.append(tmp)
            array.append(i)
            tmp = ""
    array.append(tmp)

    for o in op:
        stack = []
        array = deque(array)
        while len(array) != 0:
            tmp = array.popleft()
            if tmp == o:
                stack.append(operation(stack.pop(), array.popleft(), o))
            else:
                stack.append(tmp)
        array = stack
    return abs(int(array[0]))

def solution(expression):
    op = ['+', '-', '*']
    op = list(permutations(op, 3))
    result = []
    for i in op:
        result.append(calculate(expression, i))
    return max(result)