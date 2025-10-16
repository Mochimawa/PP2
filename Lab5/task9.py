#Программа на Python для вставки пробелов между словами, начинающимися с заглавных букв.
import re

def insert_spaces_between_caps(text):
    # Вставляем пробел перед каждой заглавной буквой, за которой не следует ничего,
    # кроме как другая заглавная буква или конец строки.
    # Это позволяет избежать добавления пробела перед первой заглавной буквой,
    # если она не является началом нового слова (например, в CamelCase).
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

print(insert_spaces_between_caps("HelloWorldFromPython"))
print(insert_spaces_between_caps("ThisIsATestString"))