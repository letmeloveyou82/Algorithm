def solution(numbers):
    numbers_str = list(map(str, numbers)) # int -> str
    answer = ''
    new_numbers = sorted(numbers_str, reverse=True, key=lambda x:(x*4)[:4])
    answer = "".join(new_numbers)
    if answer[0] == '0': # 주어진 정수가 0만 있는 경우
        return '0' # 0 하나만 리턴
    else:
        return answer