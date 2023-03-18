def degree_two_numbers(a, b):
    if b == 0:
        return 1
    return a * degree_two_numbers(a, b-1)


a = int(input())
b = int(input())
print(degree_two_numbers(a, b))
