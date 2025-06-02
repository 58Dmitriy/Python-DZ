import math
# Ввод значения от пользователя и преобразование в число
# b = int(input('Введи 2 число: '))
# a = int(input('Введи 1 число: '))
# print("a = ", a) # Вывод переменной a
# print("a = ", b) # Вывод переменной b
# print("Сумма: ", a+b) # Вывод суммы двух переменных (a+b)
#
# """
# Третье занятие
# по Python
# """
#
# a = 5
# b = 0
# c = -10
# d = 500000
# e = 600_000_000
# print(a, b, c, d, e)
#
# Дробные числа
#
# a = 3.5
# b = 0.0
# c = -5.6
# d = 500_000.000_003
# e = 4.5e2
# print(a, b, c, d, e)
#
# # Логический тип данных
# print(bool(0))
# print(bool(-5))
# print(bool("Привет мир"))
# print(bool(""))
# print(bool(" "))
# print(bool(False))
# print(bool(True))
# Сравнения

# print(2 == "2")
# print(4 < 5)
# print(5 <= 5)
# print(5 >= 5)
# print(10 >= 5)
# print(10 <= 5)
# print(1 < 5 < 10)
#
# x = 5
# a = 1
# b = 10
# print(a > x < b)
#
# # Списки (list)
# my_List = ["Строка", 57, 5.5, True]
# print(my_List)
# print(my_List[3])
# print(my_List[2:4])
# print(my_List[2:])

# # Кортежи (tuples)
# my_Tuple = (78, 89.9, True, False, "Строчка")
# print(my_Tuple)
# print(my_Tuple[0])
# print(my_Tuple[4])
# print(my_Tuple[2:5])
# print(my_Tuple[1:])

# # Словари (dictionary)
# my_Dict = {"name": "Дмитрий", "role": "QA", 123: "test", 456: 10.5 }
# print(my_Dict["name"])
# print(my_Dict[123])
# print(my_Dict[456])
# print(my_Dict.keys())
# # print(my_Dict.values())
# # # print(my_Dict[0]) # будет ошибка, так как нет ключа 0
#
# my_Dict = {
#     "name_2": "Дмитрий",
#     "role": "QA",
#     123: "test",
#     456: 10.5
# }
# print(my_Dict)
# print(my_Dict.keys())
# print(my_Dict.values())
#
# # Множества (Sets)
# my_List = [1, 2, 3, 2, 4, 5, 6, 1, 7]
# my_Set = set(my_List)
# print(my_Set)
#
# my_List = ["Добрый", "добрый", "день", "день"] # верхний и нижний регистры это разные вещи
# my_Set = set(my_List)
# print(my_Set)
#
# # Преобразование данных
# a = 5.67
# a = int(a)
# print(a)
#
# a = str(a)
# print(a+"5")
# a = float(a)
# print(a)
#
# a = "Привет мир!"
# print(a[3]) # Обращение по индексам к строкам
# a = list(a)
# print(a)
# a = set(a)
# print(a)
#
# print(ord("A"))
# print(chr(1072))
#
# print(f"\\u{ord("a"):04x}") # Юникод кодировка

# a = 5
# b = 10
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)

# Математические функции math
# print(math.ceil(5.7)) # Округляет в большую сторону
# print(math.ceil(5.2))
# print(math.floor(5.2)) # Округляет в меньшую сторону
# print(math.floor(5.8))
# print(math.sqrt(25)) # Найти квадратный корень из 25