from collections import deque

def n_plus_one(d1, d2, target):
    for c in d1:
        if target - c in d2:
            d1.remove(c)
            d2.remove(target-c)
            return True
    return False

def solution(coin, cards):
    turn = 1
    n = len(cards)
    my_card = [cards[i] for i in range(0, n//3)]
    cards = deque(cards[n//3:])
    pending = [] # 보류 중인 카드
    
    while coin >= 0 and cards:
        pending.append(cards.popleft())
        pending.append(cards.popleft())
        
        if n_plus_one(my_card, my_card, n+1):
            pass
        elif coin >= 1 and n_plus_one(my_card, pending, n+1):
            coin -= 1
        elif coin >= 2 and n_plus_one(pending, pending, n+1):
            coin -= 2
        else:
            break
        turn += 1

    return turn