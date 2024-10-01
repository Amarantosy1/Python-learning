start_time,flow_time= input().split()
flow_time = int(flow_time)
increase_hour_1 = flow_time//60 
if start_time[0] == '0':
    start_time = start_time[1:]
    int(start_time)
    increase_min = start_time + flow_time
    if increase_min < 60:
        result = increase_min
        str(result)
        print("0"+result)
    elif increase_min >= 60:
        increase_hour_2 = increase_min//60
        result_min = increase_min%60
        str(increase_hour_2)
        str(result_min)
        print(increase_hour_2 + result_min)
elif start_time[0] != '0':
    if len(start_time) == 3:
        start_hour = start_time[0]
        int(start_hour)
        start_min = start_time[1:]
        increase_min = flow_time%60
        if start_min[0] == '0':
            start_min = start_min[1:]
            int(start_min)
            result_min = start_min + increase_min
            if result_min < 60:
                str(result_min)
                str(start_hour)
                print(start_hour+result_min)
            elif result_min >= 60:
                result_hour = start_hour + result_min//60
                result_min = result_min % 60
                str(result_hour)
                str(result_min)
                print(result_hour + result_min)
        #elif start_min[0] != '0':




        