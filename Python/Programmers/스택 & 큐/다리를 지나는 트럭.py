from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_weight = 0 # 다리 위 트럭 무게
    waiting = deque(truck_weights) # 대기 트럭 큐
    bridge = deque([0 for _ in range(bridge_length)]) # 다리 길이만큼 0으로 채운다.
    
    while len(waiting) or bridge_weight > 0: # 대기 트럭이 있거나 이동 중인 트럭이 있는 동안
        removed_truck = bridge.popleft() # 다리에서 하나 제거
        bridge_weight -= removed_truck
        
        if len(waiting) and bridge_weight + waiting[0] <= weight: # 새 트럭이 다리에 올라갈 수 있으면
            new_truck = waiting.popleft()
            bridge_weight += new_truck
            bridge.append(new_truck) # 대기 트럭에서 하나 빼서 다리에 올림
        else: # 새 트럭이 다리에 올라갈 수 없으면
            bridge.append(0) # 오른쪽에 0 삽입해서 다리 길이 유지
        
        time += 1
    return time