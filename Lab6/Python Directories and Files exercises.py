#task 1
import os

path = ' '

print("Директории:")
print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

print("Файлы:")
print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

print("Все элементы:")
print(os.listdir(path))


#task 2
import os

path = ' '

print(" ", os.path.exists(path))
print(" ", os.access(path, os.R_OK))
print(" ", os.access(path, os.W_OK))
print(" ", os.access(path, os.X_OK))


#task 3
import os

path = 'файл.txt'

if os.path.exists(path):
    print("Имя файла:", os.path.basename(path))
    print("Каталог:", os.path.dirname(path))
else:
    print("Путь не существует.")


#task 4
file_path = 'example.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    count = sum(1 for line in file)
    print("Количество строк:", count)


#task 5
data = ['яблоко', 'банан', 'вишня']

with open('output.txt', 'w', encoding='utf-8') as file:
    for item in data:
        file.write(item + '\n')

#task 6
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'w') as file:
        file.write(f"Это файл {letter}.txt")


#task 7
source = 'source.txt'
destination = 'destination.txt'

with open(source, 'r', encoding='utf-8') as src, open(destination, 'w', encoding='utf-8') as dst:
    dst.write(src.read())


#task 8
import os

file_path = 'удалить_это.txt'

if os.path.exists(file_path) and os.access(file_path, os.W_OK):
    os.remove(file_path)
    print("Файл удален.")
else:
    print("Нет доступа или файл не существует.")
