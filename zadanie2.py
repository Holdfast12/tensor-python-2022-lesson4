#!/usr/bin/python3
#Создать словарь цветов, в котором ключ - название или кодировка цвета; значение - кортеж из rgb этого цвета.

colors = {'red': (255, 0, 0), 'green': (0, 128, 0), 'black': (0, 0, 0)}

print(f'Словарь цветов: {colors}')

l = list(map(lambda n: n, (input('\nВведите числа списка для сортировки через пробел: ').split())))
print(l)