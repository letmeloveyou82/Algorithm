def solution(cap, n, deliveries, pickups):
    def zero_cut(box_list):
        for i in range(n-1, -1, -1):
            if box_list[i] != 0:
                break
            box_list.pop()
        return box_list

    def box_move(box_list, original_cap):
        cap = original_cap
        while box_list:
            if box_list[-1] == 0:
                box_list.pop()
                continue
            if cap == 0:
                break
            box_list[-1] -= 1
            cap -= 1
        return box_list
    
    answer = 0
    deliveries = zero_cut(deliveries)
    pickups = zero_cut(pickups)

    while deliveries or pickups:
        max_go = max(len(deliveries), len(pickups))
        deliveries = box_move(deliveries, cap)
        pickups = box_move(pickups, cap)
        answer += max_go*2
        
    return answer