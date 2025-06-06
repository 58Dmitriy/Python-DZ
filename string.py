# Импорт для 5 задачи
from itertools import permutations

# Задание № 1
# Напишите программу, которая принимает строку от пользователя и выводит ее в обратном порядке.
# string = input("Введи текст: ")
# print(string[::-1])


# Задание № 2
# Напишите программу, которая принимает две строки и проверяет,
# являются ли они анаграммами (то есть состоят из одних и тех же символов в любом порядке).

# q = input("Введи текст 1: ").lower()
# w = input("Введи текст 2: ").lower()
# if sorted(q) == sorted(w):
#     print(True)
# else:
#     print(False)

# Задание № 3
# Напишите программу, которая принимает строку
#и подсчитывает количество гласных и согласных букв в ней.

# vowels = ["а", "у", "о", "и", "э", "ы", "я", "ю", "е", "ё"]
# text = input("Введите любой текст: ").lower()
# counter_1 = 0
# counter_2 = 0
# for i in text:
#     if i in vowels:
#         counter_1 += 1
#     else:
#         counter_2 += 1
# print(f"{counter_1} гласных букв")
# print(f"{counter_2} согласных букв")

# Задание № 4
# Напишите программу, которая принимает строку и проверяет,
# является ли она палиндромом (то есть одинаково читается в обоих направлениях).

# e = input("Введите любой текст: ").lower().replace(" ", "")
# e_2 = e [::-1]
# if e == e_2:
#     print(f"Слово {e} является палиндромом")
# else:
#     print(f"Слово {e} НЕ является палиндромом")

# Задание № 5
# Напишите программу, которая принимает строку и выводит на экран все перестановки ее символов.

# p = input("Введите любой текст: ")
# spisok = list(p)
# n = len(spisok)
# index = 0
# stack = [(spisok, 0)]
#
# while index < len(stack):
#     current, l = stack[index]
#     index +=1
#
#     if l == n - 1:
#         print("".join(current))
#     else:
#         i = n - 1
#         while i >= l :
#             temp = current[:]
#             temp[l], temp[i] = temp[i], temp[l]
#             stack.append((temp, l + 1))
#             i -= 1

# Решение через импорт permutations
# p = input("Введите любой текст: ")
# perm = permutations(p)
# for z in perm:
#     print("".join(z))

# Задание № 6
# Напишите программу, которая принимает строку и удаляет из нее все пробелы.
# r = input("Введите любой текст: ")
# print(r.replace(" ", ""))

# Задание № 7
# Напишите программу, которая принимает строку и выводит на экран самое длинное слово в ней.
# t = input("Введите любой текст: ")
# t_2 = t.split(" ")
# print(max(t_2, key=len))

# Задание № 8
# Напишите программу, которая принимает строку и заменяет каждое вхождение определенного слова на другое слово.
# y = input("Введите любой текст: ").lower()
# zamenit = input("Введите слово, которое хотите заменить: ").lower()
# alternativa = input("Введите слово, на которое хотите заменить: ")
# print(y.replace(zamenit, alternativa))

# Задание № 9
# Напишите программу, которая принимает строку и проверяет,
# является ли она панграммой (то есть содержит все буквы алфавита).
# u = input("Введите любой текст: ").lower()
# alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# while True:
#     for i in alphabet.isa and i in u:
#         print(f"{u} является панграммой")
#     else:
#         print(f"{u} НЕ является панграммой")

# Задание № 10
# Напишите программу, которая принимает строку
# и возвращает новую строку, в которой каждое слово начинается с заглавной буквы.
# o = input("Введите любой текст: ")
# print(o.title())