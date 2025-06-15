import math
# ДЗ от 07.06.2022

# user_name = input("Введите ваше имя: ")
# character_count = []
# clean_name = []
#
# def greet_and_count():
#     print(f"Привет, {user_name}! Добро пожаловать!")
#     print(f"В твоем имени {character_count} символ(ов) (без учета пробелов).")
#
# normal = []
# words = user_name.split()
# for word in words:
#     clean_name = "".join([symbol for symbol in word if symbol.isalpha()])
#     normal.append(clean_name)
#
# string = "".join(normal)
# character_count = len(string)
#
# greet_and_count()

# Задача №1
# def print_lines(n):
#     print("-" * n)
#     print("-" * n)
#
# n = int(input("Введите число повторений: "))
# print_lines(n)

# Задача №2
# def print_lines(n):
#     if n < 2:
#         print("Ширина должна быть не менее 2-х")
#     print("o" * n)
#     print("o" + " " * (n - 2))
#     print("o" * n)
#
# n = int(input("Введите число повторений: "))
# print_lines(n)

# Задача №3
# def print_lines(n):
    # print("o" * (n - 4))
    # print("o" * (n - 3))
    # print("o" * (n - 2))
    # print("o" * (n - 1))
    # print("o" * n)
# или
#     for i in range(1, n + 1):
#         print("o" * i)

# n = int(input("Введите число повторений: "))
# print_lines(n)

# Задача №4
# Напишите функцию, которая вычисляет среднее
# арифметическое пяти целых чисел

# def srefarif(a, b, c, d, e):
#     srednee = round((a + b + c + d + e) / 5)
#     print(f"Среднее арифметическое пяти числе {a, b, c, d, e} равняется {srednee}")
#
# a = int(input("Введите первое целое число: "))
# b = int(input("Введите второе целое число: "))
# c = int(input("Введите третье целое число: "))
# d = int(input("Введите четвёртое целое число: "))
# e = int(input("Введите пятое целое число: "))
# srefarif(a, b, c, d, e)

# Задача №5
# Напишите функцию, которая находит количество
# цифр в десятичной записи числа

# def f ():
#     global n
#     counter_d = 0
#     while n > 9:
#         n = n // 10
#         counter_d += 1
#     print(f"В записи находится {counter_d} цифр в десятичной записи числа")
#
# n = int(input("Введите целое число: "))
# f()

# Задача №7
# Найти периметр треугольника, заданного координатами своих вершин.
# (Определить функцию для расчета длины отрезка по координатам его вершин.)

# def side_lengths ():
#     global ab
#     global bc
#     global ca
#     xa = int(input("Введите координату х вершины А: "))
#     ya = int(input("Введите координату y вершины А: "))
#     xb = int(input("Введите координату х вершины B: "))
#     yb = int(input("Введите координату y вершины B: "))
#     xc = int(input("Введите координату х вершины C: "))
#     yc = int(input("Введите координату y вершины C: "))
#     ab = round(math.sqrt(((xb - xa) ** 2 + (yb - ya) ** 2)), 2)
#     bc = round(math.sqrt(((xc - xb) ** 2 + (yc - yb) ** 2)), 2)
#     ca = round(math.sqrt(((xc - xa) ** 2 + (yc - ya) ** 2)), 2)
#
# def triangle_perimeter():
#     global ab
#     global bc
#     global ca
#     global p
#     p = round(ab + bc + ca, 2)
#
# ab = 0
# bc = 0
# ca = 0
# p = 0
# side_lengths()
# triangle_perimeter()
# print(f"Длина стороны AB {ab} ед.,\n"
#       f"длина стороны BC {bc} ед.,\n"
#       f"длина стороны CA {ca} ед.")
# print(f"Периметр треугольника ABC {p} ед.")

# Задача №8
# def is_prime(n):
#     # spisok = []
#     if n < 2: return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
#
# primer = []
# for i in range (100, 1000):
#     if is_prime(i):
#         primer.append(i)
# print(primer)

# Задача №9

# Задача №10
# numbers = [356, 485, 100000, 99, 447, 12, 6]
# print(max(numbers))

# Задача №11
# def exchange(a, c):
#     b = d = 0
#     b  = a
#     d = c
#     return b, d
# print(exchange(5, 20))

# Задача №12

def triangle_area(a, b, c):
    p = a + b + c
    pp = p / 2
    s = round(math.sqrt((pp * (pp - a) * (pp - b) * (pp - c))), 3)
    return f"Периметр = {p}, площадь = {s}"

print(triangle_area(5, 7, 9))
print(triangle_area(3, 4, 5))
