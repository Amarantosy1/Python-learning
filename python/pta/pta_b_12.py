fomula = input().split(' ')
a = int(fomula[0])
b = int(fomula[2])
notation = fomula[1]
if notation == '+':
    print(a+b)
elif notation == '-':
    print(a-b)
elif notation == '*':
    print(a*b)
elif notation == '%':
    print(a%b)
elif notation == '/':
    print(int(a/b))
else:
    print("ERROR")
