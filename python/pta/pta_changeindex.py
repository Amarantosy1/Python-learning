def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors
        

n = int(input())
if is_prime(n):
    print(f"{n}是素数")
else:
    print(f"{n}=",end="")
    factors = prime_factors(n)
    print("*".join(map(str, factors)))