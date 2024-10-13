def find_extreme(lst, find_max=True):
    if find_max:
        extreme_index, extreme_value = max(enumerate(lst), key=lambda x: x[1])
    else:
        extreme_index, extreme_value = min(enumerate(lst), key=lambda x: x[1])
    return [extreme_index, extreme_value]

def get_extreme(dic, find_max=True):
    name_lst = list(dic.keys())
    lesson_lst = [value[0] for value in dic.values()]
    grade_lst = [int(value[1]) for value in dic.values()]
    extreme_list = find_extreme(grade_lst, find_max)
    result_list = [name_lst[extreme_list[0]], lesson_lst[extreme_list[0]]]
    return ' '.join(result_list)

n = int(input())
name_ls_grd = {}
for _ in range(n):
    a = input().split()
    name_ls_grd[a[0]] = a[1:]

print(get_extreme(name_ls_grd, find_max=True))
print(get_extreme(name_ls_grd, find_max=False))