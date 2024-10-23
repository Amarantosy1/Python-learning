def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())
for p in range(2, int(N/2)):
    if is_prime(p) and is_prime(N - p):
        print("{} = {} + {}".format(N, p, N - p))
        break