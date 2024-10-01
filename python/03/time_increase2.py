start_time, flow_time = input().split()
hour_flow_time = int(flow_time)//60
min_flow_time = int(flow_time)%60
if len(start_time) == 3:
    start_hour = int(start_time[0])
    start_min = start_time[1:]
    if start_min[0] == '0':
        start_min = int(start_min[1:])
        result_min = int(min_flow_time) + int(start_min)
    elif start_min [0] != '0':
        start_min = int(start_min)
        result_min = int(min_flow_time) + int(start_min)


elif len(start_time) == 4:
    start_hour = int(start_time[0:2])
    start_min = start_time[2:]
    if start_min[0] == '0':
        start_min = int(start_min[1:])
        result_min = int(min_flow_time) + int(start_min)
    elif start_min [0] != '0':
        start_min = int(start_min)
        result_min = int(min_flow_time) + int(start_min)

min_to_hour = result_min//60
result_hour = int(hour_flow_time) + int(start_hour) + int(min_to_hour)
result_min_2 = result_min%60
print(str(result_hour)+"{0:02}".format(result_min_2))
