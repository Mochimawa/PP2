#task 1
numbers = [1, 2, 3, 4]
product = 1
for num in numbers:
    product *= num


#task 2
s = input("Введите строку: ")
upper = 0
lower = 0

for c in s:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1

print(upper)
print(lower)


#task 3
s = input("Введите строку: ")
if s == s[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")

#task 4
import time
import math
import time


x = int(input())
ms = int(input())

time.sleep(ms / 1000)
print(f"Square root of {x} after {ms} miliseconds is {math.sqrt(x)}")

#task 5
t = (True, 1, "text")
print(all(t))


