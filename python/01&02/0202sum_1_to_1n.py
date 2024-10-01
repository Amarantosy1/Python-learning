n = int(input("输入一个正整数："))
print(sum([1/i if i %2 == 1 else -1/i for i in range(1, n) ]))

