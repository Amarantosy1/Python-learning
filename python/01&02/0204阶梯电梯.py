x = int(input("输入用电量："))
if x < 0:
    print("Invalid Value")
elif x >= 0 & x <=50:
    cost = x*0.53
    print("cost = {0:.2f}".format(cost))
else:
    cost = 50*0.53 + (x-50)*0.58
    print("cost = {0:.2f}".format(cost))
    