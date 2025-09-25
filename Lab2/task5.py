#Python sets
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Примечание: наборы не упорядочены, поэтому вы не можете быть уверены в том, в каком порядке будут отображаться элементы.
#Элементы набора неизменяемы, то есть мы не можем изменить элементы после создания набора.
#В наборах не может быть двух предметов с одинаковым значением.
#Примечание: значения True и 1считаются одинаковыми значениями в наборах и рассматриваются как дубликаты

#Чтобы определить, сколько предметов в наборе, используйте len() функцию.
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Элементы набора могут иметь любой тип данных:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#Доступ к элементам набора невозможно получить, ссылаясь на индекс или ключ.
#Но вы можете перебрать элементы набора с помощью for цикла 
#или проверить, присутствует ли указанное значение в наборе, 
#с помощью inключевого слова.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

  thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Добавьте элемент в набор, используя add() метод:
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Чтобы добавить элементы из другого набора в текущий набор, используйте update() метод.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Чтобы удалить элемент из набора, используйте метод remove()или discard().
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#Удалите случайный элемент, используя pop() метод:
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

"""
Методы union()и update()объединяют все элементы из обоих наборов.

Метод intersection()сохраняет ТОЛЬКО дубликаты.

Метод difference()сохраняет элементы из первого набора, которых нет в другом наборе(ах).

Метод symmetric_difference()сохраняет все элементы, КРОМЕ дубликатов.
"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#Python frozenset
"""
frozensetявляется неизменяемой версией набора.

Как и множества, он содержит уникальные, неупорядоченные и неизменяемые элементы.

В отличие от множеств, элементы не могут быть добавлены или удалены из frozenset.
"""
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))