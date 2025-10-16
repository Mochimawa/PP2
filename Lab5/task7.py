#Программа на Python для преобразования строки змейки в строку верблюжьего падежа.
import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    # Делаем первую букву первой части строчной, а остальные прописными
    return components[0] + ''.join(x.title() for x in components[1:])

print(snake_to_camel("hello_world_example"))
print(snake_to_camel("another_test_string"))