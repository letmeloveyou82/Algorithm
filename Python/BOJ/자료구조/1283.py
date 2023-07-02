import sys
input = sys.stdin.readline

n = int(input()) # 옵션의 개수
shortcut_key = []

def specify_shortcut(word, shortcut_key):
    first_letter_idx = []
    # 단어의 첫 글자의 인덱스들을 저장
    for i in range(len(word)):
        if i == 0 and word[i] != ' ':
            first_letter_idx.append(i)
        if word[i-1] == ' ' and word[i] != ' ':
            first_letter_idx.append(i)
    # 1. 단어의 첫 글자 중 단축키로 아직 지정되지 않은 게 있다면 그 알파벳을 단축키로 지정
    for i in first_letter_idx:
        if word[i] != ' ' and word[i].upper() not in shortcut_key and word[i].lower() not in shortcut_key:
            shortcut_key.append(word[i]) # 단축키 리스트에 해당 알파벳 추가
            word[i] = '['+word[i]+']' # 단축키로 지정된 알파벳은 좌우에 [] 괄호 씌워줌
            return word # 단축키 지정하면 함수 종료 
    # 2. 모든 단어 첫 글자가 이미 지정되어 있다면, 왼쪽에서부터 차례대로 알파벳을 보면서 단축키로 지정 안 된 것이 있다면 단축키로 지정
    for i in range(len(word)):
        if word[i] != ' ' and word[i].upper() not in shortcut_key and word[i].lower() not in shortcut_key:
            shortcut_key.append(word[i])
            word[i] = '['+word[i]+']'
            return word
        
for _ in range(n):
    word = list(input().rstrip())
    result = specify_shortcut(word, shortcut_key)
    if result == None:
        print("".join(word))
    else:
        print("".join(result))