# sales1 = float(input("Введите уровень продаж первого менеджера: "))
# sales2 = float(input("Введите уровень продаж второго менеджера: "))
# sales3 = float(input("Введите уровень продаж третьего менеджера: "))
#
# # Расчёт ЗП первого менеджера
# if sales1 <= 500:
#     salary1 = 200 + sales1 * 0.03
# elif sales1 <= 1000:
#     salary1 = 200 + sales1 * 0.05
# else:
#     salary1 = 200 + sales1 * 0.08
#
# # Расчёт ЗП второго менеджера
# if sales2 <= 500:
#     salary2 = 200 + sales2 * 0.03
# elif sales2 <= 1000:
#     salary2 = 200 + sales2 * 0.05
# else:
#     salary2 = 200 + sales2 * 0.08
#
# # Расчёт ЗП третьего менеджера
# if sales3 <= 500:
#     salary3 = 200 + sales3 * 0.03
# elif sales3 <= 1000:
#     salary3 = 200 + sales3 * 0.05
# else:
#     salary3 = 200 + sales3 * 0.08
# # Определяем лучшего менеджера
# best_salary = max(sales1, sales2, sales3)
# if best_salary == sales1:
#     salary1 += 200
#     best = 1
# elif best_salary == sales2:
#     salary2 += 200
#     best = 2
# else:
#     salary3 += 200
#     best = 3
#
# print(f"Зарплата первого менеджера: {salary1}")
# print(f"Зарплата второго менеджера: {salary2}")
# print(f"Зарплата третьего менеджера: {salary3}")
# print(f"Лучший менеджер: {best}")




# year = int(input("Введите год: "))
# month = int(input("Введите номер месяца (1-12): "))
# if month == 2:
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print("29 дней")
#     else:
#         print("28 дней")
# elif month in [1, 3, 5, 7, 8, 10, 12]:
#     print("31 дней")
# elif month in [4, 6, 9, 11]:
#     print("30 дней")
# else:
#     print("Некорректный номер месяца")

# n = int(input('Введите n: '))
# for i in range(1, 11):
#     print(f'{n} * {i} = {n*i}')

# print("Введите три целых числа")
# q = int(input("Первое число: "))
# w = int(input("Второе число: "))
# e = int(input("Третье число: "))
# spisok = [q, w, e]
# new_spisok = []
# for i in spisok:
#     if i > 5:
#         new_spisok.append(i)
# new_spisok.sort()
# print(new_spisok)


vowels = ["а", "у", "о", "и", "э", "ы", "я", "ю", "е", "ё"]
a = input("Введите любой текст: ")
counter = 0
for i in a:
    if i in vowels:
        counter += 1
print(counter)