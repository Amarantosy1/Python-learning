num = input()
numlist = list(num)
new_list=[]
while numlist:
    num_1 = numlist.pop()
    new_list.append(num_1)
if numlist[0] != '0':
    print(new_list.join())