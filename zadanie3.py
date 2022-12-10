#!/usr/bin/python3
'''
Заполнить два случайных набора чисел. Вывести оба набора. Указать какие элементы:
1) входят одновременно в оба;
2) входят только в первое, но не входят во второе;
3) входят только во второе, но не входят в первое;
4) входят в первое или во второе, но не в оба из них одновременно.
'''
import random

set1 = {random.randint(0,100) for i in range(100)}
set2 = {random.randint(0,100) for i in range(100)}

print(f'1) Числа, входящие одновременно в оба набора {set1.intersection(set2)}')
print(f'2) Числа, которые входят только в первое множество, но не входят во второе {set1.difference(set2)}')
print(f'3) Числа, которые входят только во второе множество, но не входят в первое {set2.difference(set1)}')
print(f'4) Числа, которые входят в первое или во второе, но не в оба из них одновременно {set1.symmetric_difference(set2)}')