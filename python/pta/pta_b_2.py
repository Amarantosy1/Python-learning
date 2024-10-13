n = input()
num_list = list(n)
sum_num = 0
for i in num_list:
    sum_num += int(i)
sum_num_str = str(sum_num)
pinyin_map = {
    '0': 'ling',
    '1': 'yi',
    '2': 'er',
    '3': 'san',
    '4': 'si',
    '5': 'wu',
    '6': 'liu',
    '7': 'qi',
    '8': 'ba',
    '9': 'jiu'
}

sum_num_list = [pinyin_map[digit] for digit in sum_num_str]

result = ' '.join(sum_num_list)
print(result)