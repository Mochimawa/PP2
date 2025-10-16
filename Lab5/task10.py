#Программа на Python для преобразования заданной строки верблюжьего регистра в змейку.
import re

def camel_to_snake(camel_str):
    # Вставляем подчеркивание перед каждой заглавной буквой,
    # а затем преобразуем всю строку в нижний регистр.
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

print(camel_to_snake("camelCaseString"))
print(camel_to_snake("AnotherExampleString"))