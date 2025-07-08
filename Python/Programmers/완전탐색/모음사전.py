from itertools import product

def solution(word):
    vowel = ['A', 'E', 'I', 'O', 'U']
    word_list = []
    
    for i in range(1, 6):
        for case in list(product(vowel, repeat=i)):
            word_list.append("".join(case))
    word_list.sort()
    
    return word_list.index(word)+1