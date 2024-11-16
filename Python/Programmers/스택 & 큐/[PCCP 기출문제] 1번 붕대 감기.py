from collections import deque

def solution(bandage, health, attacks):
    now = health
    success_cnt = 0
    last_attack_time = attacks[-1][0]
    attacks = deque(attacks)
    attack_time, damage = attacks.popleft()
    
    for t in range(last_attack_time+1):
        if t != attack_time:
            now += bandage[1]
            if now > health:
                now = health
            success_cnt += 1
            if success_cnt == bandage[0]:
                now += bandage[2]
                if now > health:
                    now = health
                success_cnt = 0
        else:
            now -= damage
            if now <= 0:
                return -1
            success_cnt = 0
            if attacks:
                attack_time, damage = attacks.popleft()
    return now