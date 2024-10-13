def find_extreme(lst, find_max=True):
    extreme_value = lst[0]
    extreme_index = 0
    for index, value in enumerate(lst):
        if (find_max and value > extreme_value) or (not find_max and value < extreme_value):
            extreme_value = value
            extreme_index = index
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