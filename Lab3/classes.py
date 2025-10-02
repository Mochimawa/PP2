#1. Класс - это как чертеж, по которому мы создаем объекты (вещи)
class StringManipulator:
    # Конструктор: что делать, когда создаем объект.
    def __init__(self):
        # Сохраняем строку внутри объекта. Изначально она пустая.
        self.my_string = ""

    # Метод 1: Получить строку от пользователя
    def getString(self):
        # Функция input() читает то, что вводит пользователь
        self.my_string = input("Введите что-нибудь: ")

    # Метод 2: Вывести строку в верхнем регистре
    def printString(self):
        # .upper() - это встроенная функция Python, которая делает все буквы большими
        print(self.my_string.upper())

# --- Как использовать ---
# s = StringManipulator() # Создаем объект (экземпляр класса)
# s.getString()           # Вызываем метод для ввода строки
# s.printString()         # Вызываем метод для вывода

#2. Базовый класс для всех фигур
class Shape:
    # Конструктор: устанавливает начальную "длину" и "площадь" (по умолчанию 0)
    def __init__(self, length=0):
        self.length = length

    # Метод для расчета площади. В базовом классе он просто печатает 0.
    def area(self):
        print("Площадь фигуры Shape (по умолчанию): 0")
        return 0

# Класс Square (Квадрат), который НАСЛЕДУЕТСЯ от Shape
class Square(Shape):
    # Конструктор: вызываем конструктор родителя (Shape)
    def __init__(self, length):
        # super() вызывает метод из родительского класса
        super().__init__(length)

    # Переопределяем метод area(). Теперь он считает площадь квадрата.
    def area(self):
        # Площадь = длина * длина
        square_area = self.length * self.length
        print("Площадь Квадрата:", square_area)
        return square_area

# --- Как использовать ---
# s = Square(5) # Создаем квадрат со стороной 5
# s.area()      # Выведет: Площадь Квадрата: 25

#3. Класс Rectangle (Прямоугольник), который НАСЛЕДУЕТСЯ от Shape
class Rectangle(Shape):
    # Конструктор: принимает длину (length) и ширину (width)
    def __init__(self, length, width):
        # Сначала вызываем конструктор родителя для длины
        super().__init__(length)
        # А теперь добавляем ширину, которая есть только у прямоугольника
        self.width = width

    # Переопределяем метод area(). Теперь он считает площадь прямоугольника.
    def area(self):
        # Площадь = длина * ширина
        rectangle_area = self.length * self.width
        print("Площадь Прямоугольника:", rectangle_area)
        return rectangle_area

# --- Как использовать ---
# r = Rectangle(10, 5) # Длина 10, Ширина 5
# r.area()             # Выведет: Площадь Прямоугольника: 50

#4. Для вычисления расстояния нам нужна математическая функция 'квадратный корень'
import math

class Point:
    # Конструктор: точка имеет координаты x и y
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Метод 1: Показать координаты
    def show(self):
        print(f"Координаты: ({self.x}, {self.y})")

    # Метод 2: Изменить координаты
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"Точка перемещена.")

    # Метод 3: Расстояние до другой точки
    def dist(self, other_point):
        # Формула расстояния: корень((x2-x1)^2 + (y2-y1)^2)
        
        # Разница по X
        dx = self.x - other_point.x
        # Разница по Y
        dy = self.y - other_point.y
        
        # Квадратный корень суммы квадратов
        distance = math.sqrt(dx**2 + dy**2)
        return distance

# --- Как использовать ---
# p1 = Point(3, 4)
# p2 = Point(0, 0)
# p1.show() # (3, 4)
# print("Расстояние между p1 и p2:", p1.dist(p2)) # 5.0

#5.
class Account:
    # Конструктор: владелец и начальный баланс
    #Банковский счет
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Метод 1: Внести деньги (депозит)
    def deposit(self, amount):
        # Проверяем, что сумма положительная
        if amount > 0:
            self.balance += amount # Увеличиваем баланс
            print(f"Депозит {amount} KZT. Новый баланс: {self.balance} KZT")
        else:
            print("Нельзя внести отрицательную сумму!")

    # Метод 2: Снять деньги
    def withdraw(self, amount):
        # Проверяем, что на счету достаточно денег
        if amount > self.balance:
            print("ОШИБКА: Недостаточно средств! Баланс:", self.balance)
            return False # Возвращаем False, чтобы показать, что операция не удалась
        elif amount > 0:
            self.balance -= amount # Уменьшаем баланс
            print(f"Снятие {amount} KZT. Новый баланс: {self.balance} KZT")
            return True
        else:
            print("Нельзя снять отрицательную сумму!")
            return False

# --- Как использовать ---
# acc = Account("Алихан", 100)
# acc.deposit(50)      # +50. Баланс 150
# acc.withdraw(70)     # -70. Баланс 80
# acc.withdraw(1000)   # ОШИБКА: Недостаточно средств!


