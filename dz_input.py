import sys

def users_info():
    user_info = dict(user_name=name, user_age=age, user_response=like_prog)
    # Ниже лежащий блок для проверки полученных значений в словаре
    print(user_info)
    print(user_info.keys())
    print(user_info.values())

print("Привет, пользователь! Расскажи о себе")
while True:
    name = input("Как тебя зовут? ")
    if len(name) != 0:
        break
    print("Обязательно скажи как тебя зовут, чтобы мы смогли продолжить!")
print(f"Приятно познакомиться, {name} ")

while True:
    age = input(f"{name}, сколько тебе лет? Введи возраст цифрой: ")
    if len(age) != 0:
        break
age = int(age)
delta_age = abs(26 - age)
if age < 26:
    print(f"Здорово! Ты младше меня на {delta_age} лет(год(а)")
elif age == 26:
    print(f"{name}, мы с тобой ровестники. Мне тоже 26 лет")
elif age > 26:
    print(f"Здорово! Ты старше меня на {delta_age} лет(года)")

while True:
    like_prog = input(f"{name}, любишь ли ты программировать? " 
                  f"Ответь \"Да\" или \"Нет\": ")
    if len(like_prog) != 0:
        break
    print("Обязательно дай ответ, чтобы мы могли продолжить!")
if like_prog.upper() == "ДА":
    print(f"Отлично, {name}!")
    print("Значит нам по пути.")
elif like_prog.upper() == "НЕТ":
    print(f"{name},очень печально это слышать.")
    print("Значит нам не по пути( ")
    users_info()
    sys.exit()

print(f"{name}, теперь, когда мы познакомились, давай выполним пример: (x > y - 2)")
while True:
    x = input("Введи переменную x: ")
    if len(x) != 0:
        break
    print("Обязательно введи переменную!")
x = int(x)
while True:
    y = input("Теперь введи переменную y: ")
    if len(y) != 0:
        break
    print("Обязательно введи переменную!")
y = int(y)
primer = ( x > y - 2)
print(f"Результат примера: {primer}")
print("Продолжение следует в следующих сериях...")

users_info()
