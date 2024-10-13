a = input().split()
j = a[2]
count = 0
for i in [a[0], a[1]]:
    if i == j:
        count += 1
if count == 0:
    print("C")
elif count == 1:
    if a[0] == j:
        print("B")
    else:
        print("A")

#优化
a = input().split()
j = a[2]

# 使用列表切片获取需要比较的元素
elements_to_compare = a[:2]

# 使用 count 方法计算 j 在 elements_to_compare 中出现的次数
count = elements_to_compare.count(j)

if count == 0:
    print("C")
elif count == 1:
    if a[0] == j:
        print("B")
    else:
        print("A")