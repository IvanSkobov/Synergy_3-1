

import collections



# Задание №1


def factorial(n):
    """Функция для вычисления факториала числа n"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def task1():
    print("\n" + "=" * 50)
    print("Задание №1: Факториалы")
    print("=" * 50)

    try:
        # Вводим число
        n = int(input("Введите натуральное число: "))

        if n < 1:
            print("Ошибка: введите натуральное число (>= 1)")
            return

        # Вычисляем факториал введённого числа
        fact_n = factorial(n)
        print(f"Факториал числа {n} = {fact_n}")

        # Создаём список факториалов от fact_n до 1
        result_list = []
        for i in range(fact_n, 0, -1):
            result_list.append(factorial(i))

        print(f"Список факториалов от {fact_n} до 1:")
        print(result_list)

    except ValueError:
        print("Ошибка: введите целое число!")



# Задание №2


# Исходный словарь pets
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}


def get_pet(ID):
    """Функция для получения информации о питомце по ID"""
    if ID in pets:
        return pets[ID]
    else:
        return False


def get_suffix(age):
    """Функция для получения правильного окончания слова 'год'"""
    last_two = age % 100
    last_digit = age % 10

    if 11 <= last_two <= 19:
        return "лет"
    elif last_digit == 1:
        return "год"
    elif 2 <= last_digit <= 4:
        return "года"
    else:
        return "лет"


def pets_list():
    """Функция для отображения всего списка питомцев"""
    if not pets:
        print("Список питомцев пуст!")
        return

    print("\nСписок всех питомцев:")
    print("-" * 40)
    for ID, pet_dict in pets.items():
        for name, info in pet_dict.items():
            animal = info["Вид питомца"]
            age = info["Возраст питомца"]
            owner = info["Имя владельца"]
            suffix = get_suffix(age)
            print(f"ID: {ID} - Это {animal} по кличке \"{name}\". "
                  f"Возраст: {age} {suffix}. Владелец: {owner}")
    print("-" * 40)


def create():
    """Функция для создания новой записи о питомце"""
    print("\n--- Создание новой записи ---")

    # Получаем последний ID
    if pets:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1
    else:
        new_id = 1

    # Запрашиваем информацию
    name = input("Введите имя питомца: ")
    animal_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")

    # Добавляем в словарь
    pets[new_id] = {
        name: {
            "Вид питомца": animal_type,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }

    print(f"Запись с ID {new_id} успешно создана!")


def read():
    """Функция для отображения информации о питомце"""
    print("\n--- Просмотр информации о питомце ---")

    try:
        ID = int(input("Введите ID питомца: "))
        pet = get_pet(ID)

        if pet is False:
            print(f"Питомец с ID {ID} не найден!")
            return

        # Выводим информацию
        for name, info in pet.items():
            animal = info["Вид питомца"]
            age = info["Возраст питомца"]
            owner = info["Имя владельца"]
            suffix = get_suffix(age)
            print(f"\nЭто {animal} по кличке \"{name}\". "
                  f"Возраст питомца: {age} {suffix}. "
                  f"Имя владельца: {owner}")

    except ValueError:
        print("Ошибка: ID должен быть числом!")


def update():
    """Функция для обновления информации о питомце"""
    print("\n--- Обновление информации о питомце ---")

    try:
        ID = int(input("Введите ID питомца для обновления: "))
        pet = get_pet(ID)

        if pet is False:
            print(f"Питомец с ID {ID} не найден!")
            return

        # Показываем текущую информацию
        for name, info in pet.items():
            print(f"\nТекущая информация о питомце:")
            print(f"Имя: {name}")
            print(f"Вид: {info['Вид питомца']}")
            print(f"Возраст: {info['Возраст питомца']}")
            print(f"Владелец: {info['Имя владельца']}")

            print("\nВведите новые данные (оставьте пустым, чтобы не менять):")

            new_name = input(f"Новое имя (было: {name}): ")
            new_animal = input(f"Новый вид (был: {info['Вид питомца']}): ")
            new_age = input(f"Новый возраст (был: {info['Возраст питомца']}): ")
            new_owner = input(f"Новый владелец (был: {info['Имя владельца']}): ")

            # Обновляем только те поля, которые были изменены
            if new_name:
                # Если имя меняется, нужно создать новый ключ
                new_pet_info = {
                    "Вид питомца": info["Вид питомца"] if not new_animal else new_animal,
                    "Возраст питомца": info["Возраст питомца"] if not new_age else int(new_age),
                    "Имя владельца": info["Имя владельца"] if not new_owner else new_owner
                }
                # Удаляем старую запись и добавляем с новым именем
                del pets[ID][name]
                pets[ID][new_name] = new_pet_info
            else:
                # Обновляем существующие поля
                if new_animal:
                    pets[ID][name]["Вид питомца"] = new_animal
                if new_age:
                    pets[ID][name]["Возраст питомца"] = int(new_age)
                if new_owner:
                    pets[ID][name]["Имя владельца"] = new_owner

            print("Информация успешно обновлена!")

    except ValueError:
        print("Ошибка: возраст должен быть числом!")


def delete():
    """Функция для удаления записи о питомце"""
    print("\n--- Удаление записи о питомце ---")

    try:
        ID = int(input("Введите ID питомца для удаления: "))
        pet = get_pet(ID)

        if pet is False:
            print(f"Питомец с ID {ID} не найден!")
            return

        # Показываем информацию о питомце, который будет удалён
        for name, info in pet.items():
            print(f"\nВы собираетесь удалить питомца:")
            print(f"Имя: {name}")
            print(f"Вид: {info['Вид питомца']}")
            print(f"Возраст: {info['Возраст питомца']}")
            print(f"Владелец: {info['Имя владельца']}")

        confirm = input("\nВы уверены, что хотите удалить эту запись? (да/нет): ")

        if confirm.lower() == "да":
            del pets[ID]
            print(f"Запись с ID {ID} успешно удалена!")
        else:
            print("Удаление отменено.")

    except ValueError:
        print("Ошибка: ID должен быть числом!")


def task2():
    """Главная функция для работы с ветеринарной клиникой"""
    print("\n" + "=" * 50)
    print("Задание №2: Ветеринарная клиника (CRUD)")
    print("=" * 50)

    print("\nДоступные команды:")
    print("  create - создать новую запись")
    print("  read   - просмотреть информацию о питомце")
    print("  update - обновить информацию о питомце")
    print("  delete - удалить запись о питомце")
    print("  list   - показать всех питомцев")
    print("  stop   - завершить программу")
    print("-" * 50)

    while True:
        command = input("\nВведите команду: ").strip().lower()

        if command == 'stop':
            print("Программа завершена. До свидания!")
            break
        elif command == 'create':
            create()
        elif command == 'read':
            read()
        elif command == 'update':
            update()
        elif command == 'delete':
            delete()
        elif command == 'list':
            pets_list()
        else:
            print("Неизвестная команда. Попробуйте снова.")


# ============================================
# Запуск всех заданий
# ============================================

if __name__ == "__main__":
    task1()
    task2()

