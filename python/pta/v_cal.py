x, y, z = input().split()
x = float(x.strip())
y = float(y.strip())
z = float(z.strip())
v = x*y*z
result = v/1000000
print("{0:.3f}吨".format(result))