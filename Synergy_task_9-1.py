
# Задание №1


def task1():
    print("\n" + "=" * 50)
    print("Задание №1: Количество различных чисел")
    print("=" * 50)

    try:
        N = int(input("Введите количество чисел: "))

        if N < 1 or N > 100000:
            print("Ошибка: N должно быть от 1 до 100000")
            return

        numbers = list(map(int, input("Введите числа через пробел: ").split()))

        if len(numbers) != N:
            print(f"Ошибка: введите ровно {N} чисел!")
            return

        # Используем множество для подсчёта уникальных чисел
        unique_count = len(set(numbers))
        print(f"Количество различных чисел: {unique_count}")

    except ValueError:
        print("Ошибка: введите целые числа!")



# Задание №2


def task2():
    print("\n" + "=" * 50)
    print("Задание №2: Количество общих чисел в двух списках")
    print("=" * 50)

    try:
        # Вводим первый список чисел
        print("Введите первый список чисел через пробел:")
        list1 = list(map(int, input().split()))

        # Вводим второй список чисел
        print("Введите второй список чисел через пробел:")
        list2 = list(map(int, input().split()))

        # Находим пересечение множеств
        set1 = set(list1)
        set2 = set(list2)
        intersection = set1 & set2  # или set1.intersection(set2)

        # Выводим количество общих чисел
        print(f"Количество чисел, присутствующих в обоих списках: {len(intersection)}")

        if intersection:
            print(f"Общие числа: {sorted(intersection)}")

    except ValueError:
        print("Ошибка: введите целые числа!")



# Задание №3


def task3():
    print("\n" + "=" * 50)
    print("Задание №3: Проверка повторений в последовательности")
    print("=" * 50)

    try:
        # Вводим последовательность чисел
        numbers = list(map(int, input("Введите числа через пробел: ").split()))

        # Множество для хранения уже встреченных чисел
        seen = set()

        print("\nРезультаты проверки:")
        for num in numbers:
            if num in seen:
                print("YES")
            else:
                print("NO")
                seen.add(num)

    except ValueError:
        print("Ошибка: введите целые числа!")


# ============================================
# Запуск всех заданий
# ============================================

if __name__ == "__main__":
    task1()
    task2()
    task3()

    print("\n" + "=" * 50)
    print("Все задания выполнены!")
    print("=" * 50)