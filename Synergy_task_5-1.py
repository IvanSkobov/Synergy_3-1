#Урок №5 Задание 1

# Вводим целое число
try:
    num = int(input("Введите целое число: "))

    # Проверяем число и формируем описание
    if num == 0:
        description = "нулевое число"
    elif num > 0:
        if num % 2 == 0:
            description = "положительное четное число"
        else:
            description = "положительное нечетное число"
    else:  # num < 0
        if num % 2 == 0:
            description = "отрицательное четное число"
        else:
            description = "отрицательное нечетное число"

    print(description)

except ValueError:
    print("Ошибка: пожалуйста, введите целое число!")



#Урок №5 Задание 2

# Вводим слово
word = input("Введите слово из маленьких латинских букв: ")

# Проверяем, что все буквы - маленькие латинские
if not word.islower() or not word.isalpha():
    print("Ошибка: введите слово только из маленьких латинских букв!")
else:
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_counts = {v: 0 for v in vowels}

    vowel_count = 0
    consonant_count = 0

    for letter in word:
        if letter in vowels:
            vowel_count += 1
            vowel_counts[letter] += 1
        else:
            consonant_count += 1

    print(f"Гласных: {vowel_count}")
    print(f"Согласных: {consonant_count}")

    for v in vowels:
        print(f"{v}: {vowel_counts[v] if vowel_counts[v] > 0 else False}")


#Урок №5 Задание 3

# Вводим данные
X = float(input("Введите минимальную сумму инвестиций (X): "))
A = float(input("Введите сумму Майкла (A): "))
B = float(input("Введите сумму Ивана (B): "))

# Проверяем условия
can_mike = A >= X
can_ivan = B >= X
can_together = A + B >= X

if can_mike and can_ivan:
    print(2)
elif can_mike:
    print("Mike")
elif can_ivan:
    print("Ivan")
elif can_together:
    print(1)
else:
    print(0)