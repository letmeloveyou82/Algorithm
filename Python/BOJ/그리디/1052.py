n, k = map(int, input().split()) # 갖고 있는 물병 수 n, 한 번에 옮길 수 있는 물병 수 k

# 할 수 있는 만큼 물 합침
now_max_liter = 1 # 현재 물병안에 있는 물의 양 중 가장 많은 물의 양
remain_bottle = [] # 물 합칠 수 있는 거 최대한 합치고 남은 물병
while n > 1: 
    without_a_pair = n % 2
    if without_a_pair == 1: # 짝이 없는 물병이 있으면
        remain_bottle.append(now_max_liter) # 현재 가장 최대인 물의 양을 리스트에 추가
    n = n // 2 # 합칠 거 합친 물병 수로 업데이트
    now_max_liter *= 2 # 합쳤으니 가장 많은 물의 양 업데이트
remain_bottle.append(now_max_liter) # 최종적으로 가장 많은 물의 양도 남은 물병 리스트에 추가

# 물병을 얼만큼 사야하는지 고려
buy_bottle = 0 # 사야하는 물병 수
remain_bottle_len = len(remain_bottle) # 남은 물병 리스트 개수
considering_buy = remain_bottle[0:remain_bottle_len-k+1] # 물병을 살지 말지 고려해야 되는 물병들 리스트
for i in range(len(considering_buy)):
    if i == len(considering_buy)-1: 
        break
    target_quantity = considering_buy[i+1] # 만들고자 하는 목표 물의 양
    while target_quantity > considering_buy[i]:
        target_quantity = target_quantity // 2
        buy_bottle += target_quantity # 2로 나눈 몫만큼 물병을 구매
    considering_buy[i+1] = considering_buy[i+1]*2 # 합칠 수 있으니 합쳤다는 의미로 물의 양 2배로 늘려줌
print(buy_bottle)
