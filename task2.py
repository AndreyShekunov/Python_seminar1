# Задача 2: Напишите программу, которая на вход принимает 5 чисел
# и находит максимальное из них.
# Нпример:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

lst = [78, 55, 36, 90, 2]
greatest = lst[0]
for i in range(1, len(lst)):
    if lst[i] > greatest:
        greatest = lst[i]
print(f'Максимальное число = {greatest}')