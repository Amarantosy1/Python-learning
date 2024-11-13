def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
while True:
    n=int(input())
    if n%2==0 and n>=6:
        break
for p in range(2, int(n/2)):
    if is_prime(p) and is_prime(n - p):
        print("{} = {} + {}".format(n, p, n - p))
        break