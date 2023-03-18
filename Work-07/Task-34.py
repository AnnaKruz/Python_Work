# Задача 34:  Винни-Пух попросил Вас посмотреть,
# есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам
text = ('пара-ру-рам рам-пам-папам па-ра-па-да')


def char(list_1):
    count = 0
    for i in list_1:
        if i in 'аяуюоеёэиы':
            count += 1
    return count


def same_by(text):
    text = text.split()
    for i in range(len(text)-1):
        if char(text[i]) != char(text[i+1]):
            return 'Пам парам'
    return 'Парам пам-пам'


print(same_by(text))
