from collections import defaultdict
import math

def solution(fees, records):
    car_dict = defaultdict(list) # 차량 번호를 key로, 입차 및 출차한 시각 리스트를 value로 갖는 dict
    car_result = defaultdict(int) # 차량 번호를 key로, 계산한 주차요금을 value로 갖는 dict
    for record in records:
        time, car_num, do = record.split()
        car_dict[car_num].append(time)
        
    for key in car_dict.keys():
        value_list = list(car_dict[key])
        n = len(value_list)
        total_min = 0
        if n % 2 == 1:
            value_list.append('23:59')
        for i in range(0, n, 2):
            in_h, in_m = value_list[i].split(':')
            out_h, out_m = value_list[i+1].split(':')
            total_min += (int(out_h)*60+int(out_m)) - (int(in_h)*60+int(in_m))
        pay = fees[1]
        if total_min > fees[0]:
            pay += math.ceil((total_min - fees[0]) / fees[2])*fees[3]
        car_result[key] += pay
        
    answer = list(car_result.items())
    answer = sorted(answer, key=lambda x:x[0])
    answer = [answer[i][1] for i in range(len(answer))]
    
    return answer