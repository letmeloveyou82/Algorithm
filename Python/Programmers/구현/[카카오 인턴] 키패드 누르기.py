def solution(numbers, hand):
    answer = ''
    # 0123456789*# 순서
    keypad = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 2]]
    
    left_thumb, right_thumb = 10, 11
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            left_thumb = i
        elif i in [3, 6, 9]:
            answer += "R"
            right_thumb = i
        elif i in [2, 5, 8, 0]:
            d1 = abs(keypad[i][0]-keypad[left_thumb][0]) + abs(keypad[i][1]-keypad[left_thumb][1])
            d2 = abs(keypad[i][0]-keypad[right_thumb][0]) + abs(keypad[i][1]-keypad[right_thumb][1])
            if d1 < d2:
                answer += "L"
                left_thumb = i
            elif d1 == d2:
                answer += hand[0].upper()
                if hand == "left":
                    left_thumb = i
                else:
                    right_thumb = i
            else:
                answer += "R"
                right_thumb = i
    return answer