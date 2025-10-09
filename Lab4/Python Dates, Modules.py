#Задание 1: вычитание 5 дней из текущей даты
import datetime

today = datetime.date.today()
result = today - datetime.timedelta(days=5)
print("Дата пять дней назад:", result)

#Задание 2: вчера, сегодня, завтра
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Вчера:", yesterday)
print("Сегодня:", today)
print("Завтра:", tomorrow)

#Задание 3: убрать микросекунды
import datetime

now = datetime.datetime.now()
print("До:", now)
print("После:", now.replace(microsecond=0))

#Задание 4: разница между двумя датами в секундах
import datetime

date1 = datetime.datetime(2025, 10, 1, 12, 0, 0)
date2 = datetime.datetime(2025, 10, 9, 12, 0, 0)

diff = (date2 - date1).total_seconds()
print("Разница в секундах:", diff)
