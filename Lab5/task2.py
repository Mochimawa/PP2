#Программа на Python, которая соответствует строке, за которой следует от двух до трех '.'a''b'
import re

def match_two_to_three_ab(text):
    pattern = r'ab{2,3}' # 'a' затем 'b' от двух до трех раз
    if re.search(pattern, text):
        return "Найдено совпадение"
    else:
        return "Совпадение не найдено"

print(match_two_to_three_ab("abb"))
print(match_two_to_three_ab("abbb"))
print(match_two_to_three_ab("ab"))
print(match_two_to_three_ab("abbbb"))