a = input()
num_list = list(a)
if num_list[1] == '0' and num_list[2] == '0':
    print(num_list[0])
elif num_list[2] == '0' and num_list[1] != '0':
    num_list.reverse()
    print(''.join(num_list[1:]))
else:
    num_list.reverse()
    print(''.join(num_list))
    