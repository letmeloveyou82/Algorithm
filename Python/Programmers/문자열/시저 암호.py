def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        else:
            # A(65), Z(90), a(97), z(122)
            if (i.isupper() and ord(i)+n > 90) or (i.islower() and ord(i)+n > 122):
                answer += chr(ord(i)+n-26) # 알파벳 개수 26개
                continue
            answer += chr(ord(i)+n)
    return answer