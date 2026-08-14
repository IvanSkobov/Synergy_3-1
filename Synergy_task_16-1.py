# Урок №16. Классы и объекты

# Задание №1: Класс Касса

class CashRegister:
    """Класс для работы с кассой"""

    def __init__(self):
        """Конструктор - создаём кассу с 0 деньгами"""
        self.money = 0

    def top_up(self, X):
        """
        Пополнить кассу на X
        X - сумма пополнения (должна быть положительной)
        """
        if X <= 0:
            print("Ошибка: сумма пополнения должна быть положительной!")
            return False

        self.money += X
        print(f"Касса пополнена на {X}. Текущий баланс: {self.money}")
        return True

    def count_1000(self):
        """
        Выводит сколько целых тысяч осталось в кассе
        Возвращает количество тысяч
        """
        thousands = self.money // 1000
        print(f"В кассе {thousands} целых тысяч")
        return thousands

    def take_away(self, X):
        """
        Забрать X из кассы
        Если денег недостаточно - выбрасывает ошибку
        """
        if X <= 0:
            print("Ошибка: сумма должна быть положительной!")
            return False

        if X > self.money:
            raise ValueError(f"Недостаточно денег! В кассе {self.money}, запрошено {X}")

        self.money -= X
        print(f"Из кассы забрано {X}. Текущий баланс: {self.money}")
        return True

    def get_balance(self):
        """Возвращает текущий баланс кассы"""
        return self.money

    def __str__(self):
        """Строковое представление кассы"""
        return f"Касса: {self.money} руб."



# Задание №2: Класс Черепашка


class Turtle:
    """Класс для управления черепашкой"""

    def __init__(self, x=0, y=0, s=1):
        """
        Конструктор черепашки
        x - начальная позиция по горизонтали
        y - начальная позиция по вертикали
        s - количество клеток за ход (шаг)
        """
        self.x = x
        self.y = y
        self.s = s
        self.moves_count = 0  # Счётчик сделанных ходов

    def go_up(self):
        """Перемещает черепашку вверх на s клеток"""
        self.y += self.s
        self.moves_count += 1
        print(f"Вверх -> позиция ({self.x}, {self.y})")

    def go_down(self):
        """Перемещает черепашку вниз на s клеток"""
        self.y -= self.s
        self.moves_count += 1
        print(f"Вниз -> позиция ({self.x}, {self.y})")

    def go_left(self):
        """Перемещает черепашку влево на s клеток"""
        self.x -= self.s
        self.moves_count += 1
        print(f"Влево -> позиция ({self.x}, {self.y})")

    def go_right(self):
        """Перемещает черепашку вправо на s клеток"""
        self.x += self.s
        self.moves_count += 1
        print(f"Вправо -> позиция ({self.x}, {self.y})")

    def evolve(self):
        """Увеличивает шаг (s) на 1"""
        self.s += 1
        print(f"Эволюция! Шаг увеличен до {self.s}")

    def degrade(self):
        """
        Уменьшает шаг (s) на 1
        Если шаг станет ≤ 0 - выбрасывает ошибку
        """
        if self.s - 1 <= 0:
            raise ValueError(f"Невозможно уменьшить шаг! Текущий шаг: {self.s}")

        self.s -= 1
        print(f"Деградация! Шаг уменьшен до {self.s}")

    def count_moves(self, x2, y2):
        """
        Возвращает минимальное количество действий (ходов),
        за которое черепашка сможет добраться до позиции (x2, y2)
        от текущей позиции.

        Алгоритм:
        1. Вычисляем разницу по x и y
        2. Каждый ход перемещает на s клеток в одном направлении
        3. Минимальное количество ходов = max(ceil(Δx/s), ceil(Δy/s))
        """
        # Вычисляем расстояние по осям
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        # Если шаг s = 0, то черепашка не может двигаться
        if self.s <= 0:
            raise ValueError(f"Шаг черепашки равен {self.s}, движение невозможно!")

        # Вычисляем количество ходов для каждой оси
        # Используем целочисленное деление с округлением вверх
        moves_x = (dx + self.s - 1) // self.s  # ceil(dx / s)
        moves_y = (dy + self.s - 1) // self.s  # ceil(dy / s)

        # Минимальное количество ходов = максимум из moves_x и moves_y
        min_moves = max(moves_x, moves_y)

        print(f"От ({self.x}, {self.y}) до ({x2}, {y2})")
        print(f"Расстояние по X: {dx}, по Y: {dy}, шаг: {self.s}")
        print(f"Минимальное количество ходов: {min_moves}")

        return min_moves

    def get_position(self):
        """Возвращает текущую позицию черепашки"""
        return (self.x, self.y)

    def get_step(self):
        """Возвращает текущий шаг черепашки"""
        return self.s

    def get_total_moves(self):
        """Возвращает общее количество совершённых ходов"""
        return self.moves_count

    def __str__(self):
        """Строковое представление черепашки"""
        return f"Черепашка: позиция ({self.x}, {self.y}), шаг = {self.s}, сделано ходов: {self.moves_count}"



# Дополнительный класс: Улучшенная черепашка


class SmartTurtle(Turtle):
    """Улучшенная черепашка с дополнительными методами"""

    def go_to(self, x2, y2):
        """
        Перемещает черепашку в указанную позицию
        Использует минимальное количество ходов
        """
        # Получаем минимальное количество ходов
        min_moves = self.count_moves(x2, y2)

        # Определяем направление движения
        dx = x2 - self.x
        dy = y2 - self.y

        # Перемещаемся с учётом минимального количества ходов
        # Двигаемся по диагонали, где это возможно
        for _ in range(min_moves):
            # Проверяем, нужно ли двигаться по X
            if dx > 0:
                self.go_right()
                dx -= self.s
            elif dx < 0:
                self.go_left()
                dx += self.s

            # Проверяем, нужно ли двигаться по Y
            if dy > 0:
                self.go_up()
                dy -= self.s
            elif dy < 0:
                self.go_down()
                dy += self.s

        print(f"Достигли позиции ({x2}, {y2}) за {min_moves} ходов")



# Тестирование заданий


def test_cash_register():
    """Тестирование класса Касса"""
    print("\n" + "=" * 60)
    print("Тестирование класса Касса (Задание №1)")
    print("=" * 60)

    # Создаём кассу
    cash = CashRegister()
    print(cash)

    # Пополняем кассу
    cash.top_up(500)
    cash.top_up(1500)

    # Считаем тысячи
    cash.count_1000()

    # Забираем деньги
    cash.take_away(300)

    # Пытаемся забрать больше, чем есть
    try:
        cash.take_away(2000)
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Ещё раз считаем тысячи
    cash.count_1000()

    print(f"Итоговый баланс: {cash.get_balance()}")


def test_turtle():
    """Тестирование класса Черепашка"""
    print("\n" + "=" * 60)
    print("Тестирование класса Черепашка (Задание №2)")
    print("=" * 60)

    # Создаём черепашку
    turtle = Turtle(0, 0, 2)
    print(turtle)

    # Двигаемся
    turtle.go_up()
    turtle.go_right()
    turtle.go_down()
    turtle.go_left()

    # Изменяем шаг
    turtle.evolve()
    print(turtle)

    turtle.go_up()
    turtle.go_right()

    # Считаем минимальное количество ходов до цели
    turtle.count_moves(10, 5)

    # Пытаемся уменьшить шаг
    try:
        turtle.degrade()
        turtle.degrade()
        turtle.degrade()  # Здесь должна быть ошибка
    except ValueError as e:
        print(f"Ошибка: {e}")

    print(turtle)


def test_smart_turtle():
    """Тестирование улучшенной черепашки"""
    print("\n" + "=" * 60)
    print("Тестирование улучшенной черепашки")
    print("=" * 60)

    # Создаём улучшенную черепашку
    smart = SmartTurtle(0, 0, 3)
    print(smart)

    # Перемещаемся в указанную позицию
    smart.go_to(10, 7)
    print(smart)


def test_turtle_scenarios():
    """Дополнительные сценарии тестирования черепашки"""
    print("\n" + "=" * 60)
    print("Дополнительные сценарии тестирования")
    print("=" * 60)

    # Сценарий 1: Черепашка с большим шагом
    print("\nСценарий 1: Большой шаг")
    t1 = Turtle(0, 0, 5)
    print(f"Минимальные ходы до (10, 10): {t1.count_moves(10, 10)}")  # 2 хода

    # Сценарий 2: Черепашка с маленьким шагом
    print("\nСценарий 2: Маленький шаг")
    t2 = Turtle(0, 0, 1)
    print(f"Минимальные ходы до (10, 10): {t2.count_moves(10, 10)}")  # 10 ходов

    # Сценарий 3: Черепашка уже на месте
    print("\nСценарий 3: Уже на месте")
    t3 = Turtle(5, 5, 2)
    print(f"Минимальные ходы до (5, 5): {t3.count_moves(5, 5)}")  # 0 ходов

    # Сценарий 4: Разные координаты
    print("\nСценарий 4: Разные координаты")
    t4 = Turtle(-3, 2, 3)
    print(f"Минимальные ходы до (7, -5): {t4.count_moves(7, -5)}")



# Основная программа


def main():
    print("=" * 60)
    print("Урок №16. Классы и объекты")
    print("=" * 60)

    # Тестируем кассу
    test_cash_register()

    # Тестируем черепашку
    test_turtle()

    # Тестируем улучшенную черепашку
    test_smart_turtle()

    # Дополнительные тесты
    test_turtle_scenarios()

    print("\n" + "=" * 60)
    print("Все тесты завершены!")
    print("=" * 60)


if __name__ == "__main__":
    main()