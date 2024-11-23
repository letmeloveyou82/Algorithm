import sys

def set_key(word):
    # 단어 첫글자들 확인
    idx = [0]
    for i in range(len(word)):
        if word[i] == ' ':
            idx.append(i+1)
    for j in idx:
        if shortcut_key.get(word[j].upper()) == None:
            shortcut_key[word[j].upper()] = 1
            return word[:j]+"["+word[j]+"]"+word[j+1:]

    # 왼쪽부터 오른쪽까지 확인
    for i in range(len(word)):
        if word[i] != ' ' and shortcut_key.get(word[i].upper()) == None:
            shortcut_key[word[i].upper()] = 1
            return word[:i]+"["+word[i]+"]"+word[i+1:]
    
    return word

input = sys.stdin.readline
N = int(input())
words = list(input().rstrip() for _ in range(N))
shortcut_key = dict()

for word in words:
    print(set_key(word))