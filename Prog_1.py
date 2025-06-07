text = input("Введите текст: ")
repetitions = input("Введите слово для поиска: ")
only_letters = ""
vowels = "а, у, о, и, э, ы, я, ю, е, ё"
consonants = "б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ"
count_v = 0
count_c = 0
v = []
c = []
# Оставляет только буквы (именно здесь .lower() чтобы дальше
# самое длинное слово могло быть выведено как в оригинальном тексте)
for letter in text.lower():
    if letter.isalpha():
        only_letters += letter

# Считаем гласные и согласные
for vowel in only_letters:
    if vowel in vowels:
        count_v += 1
        v += vowel
for consonant in only_letters:
    if consonant in consonants:
        count_c += 1
        c += consonant

print(f"Гласных букв: {count_v}")
print(f"Согласных букв: {count_c}")

# Находим максимально длинное слово и выводим его
words = text.split(" ")
print(f"Самое длинное слово: {(max(words, key=len))}")

#Вывод искомого слова и количество раз встреч его повторений
print(f"Слово {repetitions} встречается: {text.count(repetitions)} раз(а)")

print("__________________________")
print(only_letters)
print(v)
print(c)
print(words)








