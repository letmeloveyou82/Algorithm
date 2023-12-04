import heapq

def solution(operations):
    min_heap = []
    max_heap = []

    for i in operations:
        op, data = i.split( )
        if op == 'I':
            heapq.heappush(min_heap, int(data))
            heapq.heappush(max_heap, (-1 * int(data), int(data)))
        elif op == 'D' and len(min_heap) > 0:
            if data == '1':
                max_value = heapq.heappop(max_heap)[1]
                min_heap.remove(max_value)
            elif data == '-1':
                min_value = heapq.heappop(min_heap)
                max_heap.remove((-1 * min_value, min_value))
    if len(min_heap) > 0:
        return [max_heap[0][1], min_heap[0]]
    else:
        return [0, 0]