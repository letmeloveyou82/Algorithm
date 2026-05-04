def solution(babbling):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]
    
    # 발음할 수 있는 단어인지 확인
    def check(b):
        prev = "" # 바로 직전에 사용한 발음
        i = 0 # 현재 검사 위치
        
        while i < len(b):
            found = False
            
            for p in possible:
                if b.startswith(p, i) and p != prev:
                    i += len(p)
                    prev = p
                    found = True
                    break
            
            if not found:
                return False
        
        return True
                    
    for i in babbling:
        if check(i):
            answer += 1
    return answer