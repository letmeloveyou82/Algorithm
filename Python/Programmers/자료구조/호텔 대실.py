import heapq

def solution(book_time):

    # 분 단위로 변환하는 함수
    def to_min(time_str):
        h, m = map(int, time_str.split(":"))
        return h * 60 + m
        
    book_time = sorted(book_time, key=lambda x : x[0])

    q = []
    for start, end in book_time:
        s = to_min(start)
        e = to_min(end) + 10
        
        # 가장 빨리 비는 방의 마지막 시간이 다음 예약 시작 시각보다 작거나 같으면 재사용
        if q and q[0] <= s:
            heapq.heappop(q)
        
        heapq.heappush(q, e)
        
    return len(q)