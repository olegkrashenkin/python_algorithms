# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint

lst = []
while len(lst) != 10:
    lst.append(randint(-100, 100))
lst_copy = lst.copy()
print(f'Cписок:\n'
      f'{lst}\n'
      f'{"-" * 40}\n'
      f'Вариант 1(через pop()):')
for i in range(1, 3):
    print(f'{i} наименьший элемент: {lst.pop(lst.index(min(lst)))}')
lst_copy.sort()
print(f'\nВариант 2(через sort()):')
for i in range(2):
    print(f'{i + 1} наименьший элемент: {lst_copy[i]}')

