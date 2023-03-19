# Задача 36: На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран получившийся кортеж.
# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# ((house, дом), (car, машина), (men, человек), (tree, дерево))

text = ('house=дом car=машина men=человек tree=дерево')

print(text)

# text = tuple(str(item.split('=')) for item in text.split(' '))
text = tuple(map(lambda x: x.split(),
                 (map(lambda x: x.replace('=', ' '), text.split()))))

# text = input().split()
# result = tuple(map(lambda x: tuple(x.split("="), text)))
# print(result)

print(text)
print(type(text))
