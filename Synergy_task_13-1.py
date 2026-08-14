
# Урок №13.


import random

ROWS, COLS = 10, 10

# Генерация матриц с помощью list comprehension
matrix_1 = [[random.randint(-100, 100) for _ in range(COLS)] for _ in range(ROWS)]
matrix_2 = [[random.randint(-100, 100) for _ in range(COLS)] for _ in range(ROWS)]

# Сложение матриц с помощью вложенных генераторов
matrix_3 = [[matrix_1[i][j] + matrix_2[i][j] for j in range(COLS)] for i in range(ROWS)]

# Вывод матриц
print("Матрица 1:")
for row in matrix_1:
    print(" ".join(f"{num:>6}" for num in row))

print("\nМатрица 2:")
for row in matrix_2:
    print(" ".join(f"{num:>6}" for num in row))

print("\nМатрица 3 (сумма):")
for row in matrix_3:
    print(" ".join(f"{num:>6}" for num in row))