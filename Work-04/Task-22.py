# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 списка.
# 1 строка - первый список через пробел.
# 2 строка - второй список через пробел.


def getNumber(list_1, list_2):
    list_3 = []
    for i in list_1:
        for j in list_2:
            if i == j:
                list_3.append(i)
    return list_3


list_1 = input().split()
list_2 = input().split()
list_3 = getNumber(list_1, list_2)
print(*sorted(set(list_3)))
