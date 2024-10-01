import math
pi = math.pi
e = math.e
change_num = 35/180
x = float(input())
result = math.sin(change_num*pi)+(pow(e,x)-15*x)/math.sqrt(pow(x,4)+1)-math.log(7*x)
print("f({0:})={1:.3f}".format(x,result))