import heapq

def solution(n, k, enemy):  
    heap = [] # 최대힙 쓰려고 - 형태로 저장
    
    for round_idx, e in enumerate(enemy): 
        n -= e
        heapq.heappush(heap, -e)
        
        if n < 0:
            if k == 0:
                return round_idx 
            k -= 1
            n += -heapq.heappop(heap)
        
    return len(enemy) # 모든 라운드를 막을 수 있는 경우