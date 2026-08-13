#Задание №1

# Вводим количество чисел
N = int(input("Введите количество чисел: "))

zero_count = 0

# Используем цикл for
for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    if num == 0:
        zero_count += 1

print(f"Количество нулей: {zero_count}")


#Задание №2

X = int(input("Введите натуральное число: "))

count = 0
i = 1

while i <= X:
    if X % i == 0:
        count += 1
    i += 1

print(f"Количество делителей числа {X}: {count}")


#Задание №3

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

# Находим первое чётное число на отрезке
if A % 2 == 0:
    start = A
else:
    start = A + 1

# Собираем все чётные числа с шагом 2
even_numbers = []
for i in range(start, B + 1, 2):
    even_numbers.append(str(i))

print(" ".join(even_numbers))