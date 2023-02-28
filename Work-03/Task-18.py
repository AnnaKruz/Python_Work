# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n)
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

n = int(input())
list_1 = [randint(1, n) for i in range(n)]
print(list_1)

x = int(input())
number = 0
list_2 = []

for i in range(len(list_1)):
    if x > list_1[i]:
        temp = x - list_1[i]
        list_2.append(temp)
    else:
        temp = list_1[i] - x
        list_2.append(temp)

for i in range(len(list_2) - 1):
    if list_2[i] < list_2[i+1]:
        number = list_1[i]
print(number)
