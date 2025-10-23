#task 1
from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5]
result = reduce(operator.mul, numbers, 1)
print("Произведение всех чисел:", result)

#task 2
text = "Hello World"
uppercase_count = sum(1 for c in text if c.isupper())
lowercase_count = sum(1 for c in text if c.islower())
print("Прописные буквы:", uppercase_count)
print("Строчные буквы:", lowercase_count)

#task 3
def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_palindrome("А роза упала на лапу Азора"))

#task 4
import math
import time

n = 25100
delay_ms = 2123

time.sleep(delay_ms / 1000)
print(f"Square root of {n} after {delay_ms} miliseconds is {math.sqrt(n)}")

#task 5
t = (True, 1, "non-empty", [1])
print(all(t))

