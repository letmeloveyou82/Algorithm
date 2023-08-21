import sys
input = sys.stdin.readline
for _ in range(int(input())):
    w = list(input().rstrip())
    k = int(input())

    # 각 문자의 개수를 세는 딕셔너리
    count_char_dict = {}

    # 각 문자 개수 세기
    for char in w:
        count_char_dict[char] = count_char_dict.get(char, 0) + 1
    
    check = False
    max_answer = -1
    min_answer = len(w)

    # 특정 문자열의 위치 index를 저장하는 딕셔너리
    check_dict = {}
    
    # k개 이상인 문자들의 index 위치 저장
    for i in range(len(w)):
        if count_char_dict[w[i]] < k:
            continue
        check = True
        # 해당 문자열을 key로 하고 
        check_dict[w[i]] = check_dict.get(w[i], []) + [i]
    
    # 딕셔너리를 돌면서
    for key, value_list in check_dict.items():
        # 인덱스 번호 바탕으로 최대, 최소 갱신
        for i in range(len(value_list)-k+1):
            max_answer = max(max_answer, value_list[i+k-1] - value_list[i] + 1)
            min_answer = min(min_answer, value_list[i+k-1] - value_list[i] + 1)
    
    if check:
        print(min_answer, max_answer)
    else:
        print(-1)