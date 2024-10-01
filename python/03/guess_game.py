import random
answer_number = random.randint(0,100)
count_number = 0
while True:
    a = int(input("输入一个0到100的整数"))
    count_number += 1
    if a == answer_number:
        break
    elif a < answer_number:
        print("小啦！")
    else:
        print("大啦！")
print("猜中啦，你用了{}次".format(count_number))