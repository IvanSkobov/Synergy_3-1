#Задание 1

s = input("Введите строку: ")

# Проверяем, является ли строка палиндромом
if s == s[::-1]:
    print("yes")
else:
    print("no")


#Задание 2

s = input("Введите строку: ")

result = ""
i = 0

while i < len(s):
    if s[i] == ' ':
        result += ' '
        # Пропускаем все следующие пробелы
        while i < len(s) and s[i] == ' ':
            i += 1
    else:
        result += s[i]
        i += 1

print(result)