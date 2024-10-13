def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def modulus(a, b):
    return a % b

def divide(a, b):
    if b == 0:
        return "ERROR"
    return a // b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '%': modulus,
    '/': divide
}

try:
    fomula = input().split(' ')
    a = int(fomula[0])
    b = int(fomula[2])
    notation = fomula[1]

    if notation in operations:
        result = operations[notation](a, b)
        print(result)
    else:
        print("ERROR")
except (ValueError, IndexError):
    print("ERROR")