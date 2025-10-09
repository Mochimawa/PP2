#Задание 1: градусы → радианы
import math

degree = float(input("Введите градусы: "))
radian = math.radians(degree)
print("Радианы:", radian)

#Задание 2: площадь трапеции
height = float(input("Высота: "))
base1 = float(input("Первая основа: "))
base2 = float(input("Вторая основа: "))
area = (base1 + base2) * height / 2
print("Площадь трапеции:", area)

#Задание 3: площадь правильного многоугольника
import math

n = int(input("Количество сторон: "))
s = float(input("Длина стороны: "))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print("Площадь многоугольника:", round(area, 2))

#Задание 4: площадь параллелограмма
base = float(input("Основание: "))
height = float(input("Высота: "))
area = base * height
print("Площадь параллелограмма:", area)
