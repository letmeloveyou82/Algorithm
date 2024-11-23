def solution(s):
    answer = []
    for str in s:
        cnt, idx, stack = 0, 0, ""
        while idx < len(str): # 110 찾기
            if str[idx] == "0" and stack[-2:] == "11":
                stack = stack[:-2]
                cnt += 1 
            else:
                stack += str[idx]
            idx += 1
        
        idx = stack.find("111") # 110이 빠진 str에서 111 찾기
        if idx == -1: # 0 뒤에 110 반복해 붙이기
            idx = stack.rfind('0')
            stack = stack[:idx+1] + "110"*cnt + stack[idx+1:]
        else: # 111 앞에 110 반복해 붙이기
            stack = stack[:idx] + "110"*cnt + stack[idx:]
        answer.append(stack)
    return answer