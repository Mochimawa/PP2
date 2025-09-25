#Python Loops while,for
# Выполняется, пока условие истинно
counter = 3
while counter > 0:
    print(f"Запуск через {counter}...")
    counter = counter - 1 # Уменьшаем счетчик
print("Старт!")


# for loop (цикл "для")
# Перебирает элементы в последовательности
fruits = ["Яблоко", "Груша", "Апельсин"]
for fruit in fruits:
    print(f"На складе есть: {fruit}")