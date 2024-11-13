M, N = map(int, input().split())
matrix = []
n = 0
for _ in range(M):
    a = input().split()
    matrix.append([int(i) for i in a])

for i in range(1, M - 1):
    for j in range(1, N - 1):
        if matrix[i][j] > matrix[i - 1][j] and matrix[i][j] > matrix[i + 1][j] and matrix[i][j] > matrix[i][j - 1] and matrix[i][j] > matrix[i][j + 1]:
            print(matrix[i][j], i + 1, j + 1)
            n = 1

if n == 0:
    print("None", M, N)