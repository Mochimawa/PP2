#Программа на Python для разделения строки на прописные буквы.
import re

def split_on_uppercase(text):
    # Используем re.findall с lookahead для разделения перед каждой заглавной буквой,
    # но без включения самой заглавной буквы в разделитель.
    # Или более простой способ:
    return re.findall(r'[A-Z][a-z]*', text)

print(split_on_uppercase("SplitMeByCapitalLetters"))
print(split_on_uppercase("AnotherExampleString"))