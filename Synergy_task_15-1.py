# ============================================
# Урок №15. ООП - Задания 1-2 (упрощённая версия)
# ============================================

# -------------------- Задание 1 --------------------
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Autobus(Transport):
    pass


bus1 = Autobus("Renaul Logan", 180, 12)
print(f"Название автомобиля: {bus1.name} Скорость: {bus1.max_speed} Пробег: {bus1.mileage}")


# -------------------- Задание 2 --------------------
class Transport2:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"


class Autobus2(Transport2):
    def seating_capacity(self, capacity=50):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


bus2 = Autobus2("Renaul Logan", 180, 12)
print(bus2.seating_capacity())