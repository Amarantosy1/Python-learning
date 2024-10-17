#计算水仙花数
def sum_pow_list(lst, n):
    result = 0
    for i in lst:
        i = int(i)
        result += pow(i,n)
    return result
          
n = int(input())
num_lst = []
result = 0
for i in range(pow(10,n-1),pow(10,n)):  
    num_split = list(str(i))
    if sum_pow_list(num_split, n) == i:
        num_lst.append(i)
        
for x in num_lst:
    print(x)