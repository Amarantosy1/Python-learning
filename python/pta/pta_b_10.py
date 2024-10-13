def salary_calc(s, standard):
    if s < 40:
        result = s * standard
    else:
        result = 40 * standard + 1.5 * standard * (s - 40)
    return float(result)

a = input().split()
age = int(a[0])
work_hour = int(a[1])
if age >= 5:
    standard = 50
    result = salary_calc(work_hour, standard)
else:
    standard = 30
    result = salary_calc(work_hour, standard)
print("{:.2f}".format(result))