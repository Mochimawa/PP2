#Программа на Python, которая соответствует строке, за которой следует ноль или более '.'a''b'
import re

def match_zero_or_more_ab(text):
    pattern = r'ab.*' # 'a' затем 'b' затем ноль или более любых символов
    if re.search(pattern, text):
        return "Найдено совпадение"
    else:
        return "Совпадение не найдено"

print(match_zero_or_more_ab("ac"))
print(match_zero_or_more_ab("ab"))
print(match_zero_or_more_ab("abbbb"))
print(match_zero_or_more_ab("abcde"))