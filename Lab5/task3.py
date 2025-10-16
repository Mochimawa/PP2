#Программа на Python для поиска последовательностей строчных букв, соединенных символом подчеркивания.
import re

def find_lowercase_with_underscore(text):
    pattern = r'[a-z]+_[a-z]+'
    matches = re.findall(pattern, text)
    return matches

print(find_lowercase_with_underscore("hello_world python_program another_example"))
print(find_lowercase_with_underscore("no_underscore_here"))