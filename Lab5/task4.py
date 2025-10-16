#Программа на Python, чтобы найти последовательности одной прописной буквы, за которой следуют строчные буквы.
import re

def find_capital_followed_by_lowercase(text):
    pattern = r'[A-Z][a-z]+'
    matches = re.findall(pattern, text)
    return matches

print(find_capital_followed_by_lowercase("HelloWorld PythonProgram ASimpleTest"))
print(find_capital_followed_by_lowercase("lowercase text"))