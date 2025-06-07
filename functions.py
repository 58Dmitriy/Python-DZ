# ДЗ от 07.06.2022

user_name = input("Введите ваше имя: ")
character_count = []
clean_name = []

def greet_and_count():
    print(f"Привет, {user_name}! Добро пожаловать!")
    print(f"В твоем имени {character_count} символ(ов) (без учета пробелов).")

normal = []
words = user_name.split()
for word in words:
    clean_name = "".join([symbol for symbol in word if symbol.isalpha()])
    normal.append(clean_name)

string = "".join(normal)
character_count = len(string)

greet_and_count()