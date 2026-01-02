def solution(keymap, targets):
    answer = []
    char_dict = dict()
    
    # 목표 문자열 작성을 위해 최소 눌러야 하는 키 횟수 구하는 함수
    def find_target_cnt(target):
        ans = 0
        for t in target:
            find_char = char_dict.get(t)
            if find_char == None:
                return -1 # 작성 불가일 때는 -1 리턴
            else:
                ans += find_char
        return ans 
    
    for k in keymap:
        for i in range(len(k)):
            previous = char_dict.get(k[i])
            if previous == None:
                # 추가
                char_dict[k[i]] = i+1
            else:
                # 최소 값으로 value 수정
                char_dict[k[i]] = min(previous, i+1)
    
        
    for target in targets:
        answer.append(find_target_cnt(target))
        
    return answer