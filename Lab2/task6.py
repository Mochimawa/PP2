#Python Dictionaries
"""
Словари используются для хранения значений данных в парах ключ:значение.

Словарь — это упорядоченная*, изменяемая и не допускающая дубликатов коллекция.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Словари не могут иметь два элемента с одинаковым ключом:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Вывести количество элементов в словаре:
print(len(thisdict))

#Типы данных String, int, boolean и list:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#Доступ к элементам словаря можно получить, указав его ключевое имя в квадратных скобках:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#Внесите изменения в исходный словарь и увидите, что список значений также обновился:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#Вы можете изменить значение конкретного элемента, указав его ключевое имя
#Метод update()обновит словарь элементами из заданного аргумента