lower,upper = input().split()
lower,upper = int(lower),int(upper)
if lower <= upper & upper <= 100:
    for i in range(lower,upper, 2):
        print("fahr celsius")
        print(i,"{0:>6.1f}".format(5*(i-32)/9))
else:
    print("Invalid")