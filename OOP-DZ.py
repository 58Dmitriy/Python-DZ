# # Задание 1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimetr(self):
#         return 2 * (self.width * self.height)
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#     def perimetr(self):
#         return 4 * self.side
#
# rect = Rectangle(4,5)
# print("Периметр прямоугольника:", rect.perimetr())
# print("Площадь прямоугольника:", rect.area())
#
# sq = Square(3)
# print("Площадь квадрата: ", sq.area())
# print("Периметр квадрата: ", sq.perimetr())

# Задача №2
# class Person:
#     name = None
#     age = None
#     gender = None
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def introduce(self):
#         print(f"Имя: {self.name} | Возраст: {self.age} | Пол: {self.gender}")
#
# class Employee(Person):
#     salary = None
#     position = None
#
#     def __init__(self, salary, position, name, age, gender):
#         self.salary = salary
#         self.position = position
#         super().__init__(name, age, gender)
#
#     def work(self):
#         print(f"Имя: {self.name} | Возраст: {self.age} | Пол: {self.gender}"
#               f" | Должность: {self.position} | Зарплата: {self.salary}")
#
# employee1 = Employee(100, "Тестировщик", "Дмитрий", 26, "М")
# employee1.work()








