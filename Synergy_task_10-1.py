
# Задание 1
print("Задание 1: Ветеринарная клиника")
pets = {}

name = input("Введите имя питомца: ")
animal_type = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя владельца: ")

pets[name] = {
    "Вид питомца": animal_type,
    "Возраст питомца": age,
    "Имя владельца": owner
}

# Вывод информации
for pet_name, pet_info in pets.items():
    animal = pet_info["Вид питомца"]
    age = pet_info["Возраст питомца"]
    owner = pet_info["Имя владельца"]

    # Определяем окончание
    if 11 <= age % 100 <= 19:
        age_word = "лет"
    elif age % 10 == 1:
        age_word = "год"
    elif 2 <= age % 10 <= 4:
        age_word = "года"
    else:
        age_word = "лет"

    print(f"Это {animal} по кличке \"{pet_name}\". Возраст питомца: {age} {age_word}. Имя владельца: {owner}")

# Задание 2
print("\nЗадание 2: Словарь со степенями")
my_dict = {}

for num in range(10, -6, -1):
    my_dict[num] = num ** num

for key, value in my_dict.items():
    print(f"{key}: {value}")