
# Урок №14. Рекурсия


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_list(lst, index=0):
    """Рекурсивный вывод списка"""
    if index >= len(lst):
        print("Конец списка")
        return
    print(lst[index])
    print_list(lst, index + 1)

# Запуск
print_list(my_list)