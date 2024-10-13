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