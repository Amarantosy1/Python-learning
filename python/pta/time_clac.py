start_time = int(input())
hour = start_time//3600
min = (start_time%3600)//60
second = (start_time%3600)%60
print("{0:}小时{1:}分{2:}秒".format(hour,min,second))