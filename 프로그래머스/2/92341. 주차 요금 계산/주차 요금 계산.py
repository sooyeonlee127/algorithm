import math
def countFee(time, fees):
    if time <= fees[0]:
        return fees[1]
    else:
        pay = math.ceil((time - fees[0]) / fees[2])
        pay *= fees[3]
        pay += fees[1]
        return pay 

def solution(fees, records):
    answer = []
    car_dict = dict()
    for rec in records:
        record = list(map(str, rec.split(' ')))
        time_list = list(map(str, record[0].split(':')))
        time = int(time_list[0])*60 + int(time_list[1])
        if record[1] not in car_dict:
            car_dict[record[1]] = [time]
        else:
            car_dict[record[1]].append(time)
    for car in car_dict:
        if len(car_dict[car]) % 2 == 0: continue
        car_dict[car].append(23*60+59)
    
    sorted_car = sorted(list(car_dict.keys()))
    for car in sorted_car:
        result = 0
        for i in range(0, len(car_dict[car])-1, 2):
            result += car_dict[car][i+1] - car_dict[car][i]
        answer.append(countFee(result, fees))
            
    return answer