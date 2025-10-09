#Задание 1: генератор квадратов чисел до N
def generate_squares(n):
    for i in range(n+1):
        yield i ** 2

n = int(input("Введите число N: "))
for square in generate_squares(n):
    print(square, end=" ")

#Задание 2: четные числа от 0 до n через запятую
def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input("Введите n: "))
print(",".join(str(i) for i in even_numbers(n)))

#Задание 3: числа, кратные 3 и 4, от 0 до n
def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Введите n: "))
for num in divisible_by_3_and_4(n):
    print(num)

#Задание 4: квадраты всех чисел от a до b
def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2

a = int(input("Введите a: "))
b = int(input("Введите b: "))
for val in squares(a, b):
    print(val)

#Задание 5: генератор, возвращающий числа от n до 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Введите n: "))
for i in countdown(n):
    print(i)

