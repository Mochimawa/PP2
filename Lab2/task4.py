#Python Tuples - Кортежи
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Изменить значения кортежа
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Добавить элемент
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Добавить кортеж в кортеж 
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Удалить элементы
#Примечание: удалять элементы из кортежа нельзя
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#Или вы можете полностью удалить кортеж:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
