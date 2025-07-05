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

# def triangle_area(a, b, c):
#     p = a + b + c
#     pp = p / 2
#     s = round(math.sqrt((pp * (pp - a) * (pp - b) * (pp - c))), 3)
#     return p, s
#
# tr1 = (triangle_area(5, 7, 10))
# tr2 = (triangle_area(3, 4, 5))
# print(f"Сумма периметра треугольника: {tr1[0]} + {tr2[0]} = {tr1[0] + tr2[0]}")
# print(f"Сумма площадь треугольника: {tr1[1]} + {tr2[1]} = {tr1[1] + tr2[1]}")

# Задача №13

# def trapeciz_p_s(a, b, h):
#     side =math.sqrt(((a - b) / 2) ** 2 + h ** 2)
#     p = round(a + b +  2 * side, 2)
#     s = round((a + b) / 2 * h, 2)
#     return p, s
#
# t1 = trapeciz_p_s(4,10, 3)
# t2 = trapeciz_p_s(6,15, 5)
# print(f"Сумма периметра трапеций: {t1[0]} + {t2[0]} = {t1[0] + t2[0]}")
# print(f"Сумма периметра трапеций: {t1[1]} + {t2[1]} = {t1[1] + t2[1]}")

# Задача №14

# def circle_area(r):
#     s = round(3.141592654 * r ** 2, 3)
#     return s
#
# def rectangular_area(a, b):
#     s = a * b
#     return s
#
# def triangle_area (a, h):
#     s = (a * h) / 2
#     return s
#
# print("1 - круг")
# print("2 - прямоугольник")
# print("3 - треугольник")
# figura = input(f"Выберите фигуру, площадь которой хотите найти: ")
# if figura == "1":
#     r = float(input("Введите радиус круга"))
#     print(circle_area(r))
# elif figura == "2":
#     a = float(input("Введите сторону a для прямоугольника"))
#     b = float(input("Введите сторону a для прямоугольника"))
#     print(rectangular_area(a, b))
# elif figura == "2":
#     a = float(input("Введите сторону треугольника"))
#     h = float(input("Введите высоту треугольника"))
#     print(triangle_area(a, h))
# else:
#     print("Введена ошибочная команда")

# Задача №16

# def drawing(n, s):
#     for i in range(1, n + 1):
#         print(s * n)
#
# print(drawing(5, "w" ))

# или
# def drawing(n, s):
#     for _ in range(n):
#         print(n * s)
#
# side = int(input("Введите сторону квадрата: "))
# symbol = input("Введите символ: ")
# drawing(side, symbol)

# Задача №17
# def dividers(n):
#     for i in range(1, int((n/2) + 1)):
#         if n % i == 0:
#             print(i, end=" ")
#     print()
#
# while True:
#     print("0 - остановить программу")
#     command = int(input("Введите команду 0 для остановки, иначе введите целое число: "))
#     if command == 0:
#         break
#     dividers(command)

# Задача №21
# def average_assessment(a, b, c, d, e):
#     assessment = [a, b, c, d, e]
#     assessment_min = min(assessment)
#     assessment_max = max(assessment)
#     av_as = (sum(assessment) - assessment_max - assessment_min) / 3
#     print(av_as)
#
# average_assessment(10,20,30,40,50)

# Задача №19

# def PointInRect (x,y,x1,y1,x2,y2):
#     return x1 <= x <= x2 and y2 <= y<= y1
#
# x = int(input("Введите координату Х исходной точки: "))
# y = int(input("Введите координату У исходной точки: "))
#
# x1 = int(input("Введите координату Х левого верхнего угла прямоугольника: "))
# y1 = int(input("Введите координату У левого верхнего угла прямоугольника: "))
# x2 = int(input("Введите координату Х правого нижнего угла прямоугольника: "))
# y2 = int(input("Введите координату У правого нижнего угла прямоугольника: "))
#
# print(PointInRect(x,y,x1,y1,x2,y2))

# Задача №20
# def s_l(x1, y1, x2, y2):
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2)  ** 0.5
#
# def tri_area(a, b, c):
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5
#
# def pointintriangle(px, py, x1, y1, x2, y2, x3, y3):
#     # Стороны исходного треугольника АБС
#     a = s_l(x1, y1, x2, y2)
#     b = s_l(x2, y2, x3, y3)
#     c = s_l(x1, y1, x2, y2)
#     area_abc = tri_area(a, b, c)
#
#     # Стороны исходного треугольника PAB
#     a1 = s_l(px, py, x1, y1)
#     b1 = s_l(px, py, x2, y2)
#     c1 = s_l(x1, y1, x3, y3)
#     area_pab = tri_area(a1, b1, c1)
#
#     # Стороны исходного треугольника PBC
#     a2 = s_l(px, py, x2, y2)
#     b2 = s_l(px, py, x3, y3)
#     c2 = s_l(x2, y2, x3, y3)
#     area_pbc = tri_area(a2, b2, c2)
#
#     # Стороны исходного треугольника PCA
#     a3 = s_l(px, py, x3, y3)
#     b3 = s_l(px, py, x1, y1)
#     c3 = s_l(x3, y3, x1, y1)
#     area_pca = tri_area(a3, b3, c3)
#
#     total_area = area_pab + area_pbc + area_pbc
#
#     return abs(total_area - area_abc) < 1e-5
#
# print(pointintriangle(1,1,0,0,4,0,0,3))


# Задача ДЗ
# def fibonachi(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonachi(n-1) + fibonachi(n-2)
#
# n = int(input("Введите номер числа Фибоначчи: "))
# print(f"{n} - е число Фибоначчи: ", fibonachi(n))

