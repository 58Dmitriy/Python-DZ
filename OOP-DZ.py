# Задача №1

# class Rectangle:
#     width = None
#     height = None
#     perimeter = None
#     area = None
#
#     def __init__(self, width, height,):
#         self.width = width
#         self.height = height
#
#     def get_info(self):
#         print(f"Ширина: {self.width} | Высота: {self.height} | Периметр: {self.perimeter} | Площадь: {self.area}")
#
#     def perimeter(self, width, height):
#         self.width = width
#         self.height = height
#         self.perimeter = (width + height) * 2
#
#     def area(self, width, height):
#         self.width = width
#         self.height = height
#         self.area = width * height
#
# class Square(Rectangle):
# # Как удалить предыдущие атрибуты, если класс наследует атрибуты
#
# f1 = Rectangle(10, 5)
# f1.perimeter(10, 5)
# f1.area(10, 5)
# f1.get_info()

# Задача №2
class Person:
    name = None
    age = None
    gender = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Имя: {self.name} | Возраст: {self.age} | Пол: {self.gender}")

class Employee(Person):
    salary = None
    position = None

    def __init__(self, salary, position, name, age, gender):
        self.salary = salary
        self.position = position
        super().__init__(name, age, gender)

    def work(self):
        print(f"Имя: {self.name} | Возраст: {self.age} | Пол: {self.gender}"
              f" | Должность: {self.position} | Зарплата: {self.salary}")

employee1 = Employee(100, "Тестировщик", "Дмитрий", 26, "М")
employee1.work()







