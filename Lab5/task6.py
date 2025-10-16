#Программа на Python для замены всех вхождений пробела, запятой или точки на двоеточие.
import re

def replace_space_comma_dot(text):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', text)

print(replace_space_comma_dot("Hello World, how are you. I'm fine"))