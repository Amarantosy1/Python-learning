N = int(input())
result = sum([i/(2*i-1) if i %2 == 1 else -i/(2*i-1) for i in range(1,N+1)])
print("{0:.3f}".format(result))