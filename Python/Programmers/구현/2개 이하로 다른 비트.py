def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
            continue

        number_bin = '0' + bin(num)[2:]
        number_bin = number_bin[:number_bin.rindex('0')] + '10' + number_bin[number_bin.rindex('0')+2:]
        answer.append(int(number_bin, 2))
        
    return answer