def chaifen(n):
    result_lst = []
    for i in range(1,n):
        if n % i == 0:
            result_lst.append(i)
    return result_lst
def is_wanshu(n):
    if sum(chaifen(n)) == n:
        return True
    else:
        return False

m, n = map(int, input().split())
for i in range(m,n+1):
    if is_wanshu(i):
        print(f"{i} = "+" + ".join([str(m) for m in chaifen(i)]))

#优化后
def chaifen(n):
    result_lst = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result_lst.append(i)
            if i != 1 and i != n // i:
                result_lst.append(n // i)
    return result_lst

def is_wanshu(n):
    return sum(chaifen(n)) == n

m, n = map(int, input().split())
found = False
for i in range(m, n + 1):
    if is_wanshu(i):
        found = True
        print(f"{i} = " + " + ".join(map(str, sorted(chaifen(i)))))
if not found:
    print("None")
        