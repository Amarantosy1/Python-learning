import math
pi = math.pi
error = float(input())
sum_series = 0
n = 1
while True:
    sum_series += 1/n**2
    if math.sqrt(6*sum_series) - pi < error:
        break
    n += 1
print("{:.6f}".format(sum_series))
