# 5) Простые числа
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def filter_prime(lst):
    return [x for x in lst if is_prime(x)]


# 6) Граммы -> унции
def grams_to_ounces(g):
    return g * 28.3495231


# 7) F -> C
def f_to_c(f):
    return (5/9) * (f - 32)


# 8) Куры и кролики
def solve(heads, legs):
    for c in range(heads+1):
        r = heads - c
        if 2*c + 4*r == legs:
            return c, r


# 9) Перестановки
from itertools import permutations
def all_perm(s):
    return [''.join(p) for p in permutations(s)]


# 10) Реверс слов
def rev_words(s):
    return ' '.join(s.split()[::-1])


# 11) has_33
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False


# 12) spy_game
def spy_game(nums):
    code = [0,0,7]
    for n in nums:
        if code and n == code[0]:
            code.pop(0)
    return not code


# 13) Объем сферы
def sphere_vol(r):
    import math
    return (4/3) * math.pi * r**3


# 14) Уникальные элементы
def unique(lst):
    res = []
    for x in lst:
        if x not in res: res.append(x)
    return res


# 15) Палиндром
def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


# 16) Гистограмма
def histogram(lst):
    for x in lst:
        print("*" * x)


# 17) Игра
import random
def guess_game():
    name = input("Name: ")
    num = random.randint(1,20)
    g = 0
    while True:
        guess = int(input("Guess: "))
        g += 1
        if guess < num: print("Too low")
        elif guess > num: print("Too high")
        else:
            print(f"Good job, {name}! {g} guesses")
            break
