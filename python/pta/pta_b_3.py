def find_max(lst):
    max_value = lst[0]
    max_index = 0
    for index, value in enumerate(lst):
        if value > max_value:
            max_value = value
            max_index = index
    return [max_index, max_value]

def find_min(lst):
    min_value = lst[0]
    min_index = 0
    for index, value in enumerate(lst):
        if value < min_value:  # Fix comparison operator to find minimum
            min_value = value
            min_index = index
    return [min_index, min_value]

def get_max(dic):
    name_lst = [key for key in dic]
    lesson_lst = [value[0] for value in dic.values()]  # Fix to use dic.values()
    grade_lst = [int(value[1]) for value in dic.values()]  # Fix to use dic.values()
    max_list = find_max(grade_lst)
    result_list = []
    result_list.append(name_lst[int(max_list[0])])
    result_list.append(lesson_lst[int(max_list[0])])  # Fix index to use max_list[0]
    result = ' '.join(result_list)
    return result

def get_min(dic):
    name_lst = [key for key in dic]
    lesson_lst = [value[0] for value in dic.values()]  # Fix to use dic.values()
    grade_lst = [int(value[1]) for value in dic.values()]  # Fix to use dic.values()
    min_list = find_min(grade_lst)
    result_list = []
    result_list.append(name_lst[int(min_list[0])])
    result_list.append(lesson_lst[int(min_list[0])])  # Fix index to use min_list[0]
    result = ' '.join(result_list)
    return result

n = int(input())
name_ls_grd = dict()
while n > 0:
    a = input().split()
    name_ls_grd.update({a[0]: a[1:]})
    a.clear()
    n -= 1

print(get_max(name_ls_grd))
print(get_min(name_ls_grd))