#Программа на Python, которая соответствует строке, за которой следует что угодно, оканчивающаяся на '.'a''b'
import re

def match_any_ending_ab(text):
    pattern = r'.*ab$'
    if re.search(pattern, text):
        return "Найдено совпадение"
    else:
        return "Совпадение не найдено"

print(match_any_ending_ab("blablab"))
print(match_any_ending_ab("xyzab"))
print(match_any_ending_ab("ab"))
print(match_any_ending_ab("abc"))