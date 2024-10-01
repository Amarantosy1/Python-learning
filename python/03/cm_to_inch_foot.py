cm = int(input())
a = (float(cm)/30.48)
test_num = a%1
if test_num < 5/6:
    foot = int(a)
    inch = round(test_num*12)
elif test_num >= 5/6:
    foot = int(a)+1
    inch = round(test_num*12-10)
print(foot,inch)
