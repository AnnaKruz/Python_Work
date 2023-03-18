# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# pytest -v tests\test_30.py

def arithmetic_progression(first: int,
                           diff: int,
                           quantity: int) -> list[int]:
    arr = []
    for i in range(1, quantity + 1):
        arr.append(first + diff*(i - 1))
    return arr
