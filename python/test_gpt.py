def calc(mat, m, reverse=False):
    result1 = 0
    for i in range(m):
        if reverse:
            result1 += int(mat[i][m - 1 - i])
        else:
            result1 += int(mat[i][i])
    return result1

n = int(input())
matrix = []
for _ in range(n):
    added_lst = input().split()
    matrix.append(added_lst)

a = calc(matrix, n)
b = calc(matrix, n, reverse=True)
if n % 2 != 0:
    result = a + b - int(matrix[n // 2][n // 2])
else:
    result = a + b
print("{:.2f}".format(result))
